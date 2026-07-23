[CmdletBinding()]
param(
    [string]$CodexSkillsDir,
    [switch]$Force
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$SkillsRoot = Join-Path $RepoRoot "skills"

$ActiveSkills = @(
    "aigc-image",
    "aigc-video",
    "aigc-vfx-combat",
    "aigc-project-context",
    "aigc-prompt-rewrite"
)

$RetiredSkills = @(
    "aigc-image-edit-prompt",
    "aigc-image-reverse-prompt",
    "aigc-visual-diagnose",
    "aigc-vibe-creating-prompt",
    "aigc-seedance-prompt",
    "aigc-script-context",
    "aigc-natural-language-prompt",
    "aigc-creative-director",
    "aigc-project-planner",
    "aigc-shot-diagnosis-pipeline",
    "aigc-workflow-router",
    "aigc-shot-diagnose",
    "cinematic-storyboard-enhancer",
    "seedance-prompt-master"
)

if (-not $CodexSkillsDir) {
    if ($env:CODEX_HOME) {
        $CodexSkillsDir = Join-Path $env:CODEX_HOME "skills"
    } else {
        $CodexSkillsDir = Join-Path $HOME ".codex\skills"
    }
}

function Get-DirectoryEntry {
    param(
        [Parameter(Mandatory = $true)][string]$Directory,
        [Parameter(Mandatory = $true)][string]$Name
    )

    return Get-ChildItem -LiteralPath $Directory -Force -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -eq $Name } |
        Select-Object -First 1
}

function Get-NormalizedPath {
    param([Parameter(Mandatory = $true)][string]$Path)

    $Resolved = Resolve-Path -LiteralPath $Path -ErrorAction SilentlyContinue
    if ($Resolved) {
        $Path = $Resolved.Path
    }
    $Full = [IO.Path]::GetFullPath($Path)
    return $Full.TrimEnd([char[]]@([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar))
}

function Get-LinkTargetPath {
    param(
        [Parameter(Mandatory = $true)]$Item,
        [Parameter(Mandatory = $true)][string]$EntryPath
    )

    $Target = $Item.Target
    if ($Target -is [array]) {
        $Target = $Target[0]
    }
    if (-not $Target) {
        return $null
    }
    if (-not [IO.Path]::IsPathRooted($Target)) {
        $Target = Join-Path (Split-Path -Parent $EntryPath) $Target
    }
    return Get-NormalizedPath -Path $Target
}

function Test-SamePath {
    param(
        [string]$Left,
        [string]$Right
    )

    if (-not $Left -or -not $Right) {
        return $false
    }
    return [string]::Equals($Left, $Right, [StringComparison]::OrdinalIgnoreCase)
}

function Test-ReparsePoint {
    param([Parameter(Mandatory = $true)]$Item)
    return ($Item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0
}

function Remove-LinkOnly {
    param(
        [Parameter(Mandatory = $true)]$Item,
        [Parameter(Mandatory = $true)][string]$Path
    )

    if (-not (Test-ReparsePoint -Item $Item)) {
        throw "Refusing to delete a non-link entry: $Path"
    }

    try {
        [IO.Directory]::Delete($Path)
    } catch {
        [IO.File]::Delete($Path)
    }

    $Remaining = Get-DirectoryEntry -Directory (Split-Path -Parent $Path) -Name (Split-Path -Leaf $Path)
    if ($Remaining) {
        throw "Failed to remove link or junction: $Path"
    }
}

function New-BackupPath {
    param([Parameter(Mandatory = $true)][string]$Name)
    return Join-Path $BackupRoot "$Name.backup-$([Guid]::NewGuid().ToString('N'))"
}

$SkillsRootItem = Get-Item -LiteralPath $SkillsRoot -Force -ErrorAction SilentlyContinue
if (-not $SkillsRootItem -or -not $SkillsRootItem.PSIsContainer) {
    throw "Skills directory not found: $SkillsRoot"
}

# Validate the complete replacement before touching the installed set.
foreach ($Name in $ActiveSkills) {
    $Source = Join-Path $SkillsRoot $Name
    $SkillFile = Join-Path $Source "SKILL.md"
    $AgentFile = Join-Path $Source "agents\openai.yaml"
    if (-not (Test-Path -LiteralPath $SkillFile -PathType Leaf) -or -not (Test-Path -LiteralPath $AgentFile -PathType Leaf)) {
        throw "Incomplete skill: $Source"
    }
    $NamePattern = "^name:\s*$([regex]::Escape($Name))\s*$"
    if (-not (Select-String -LiteralPath $SkillFile -Pattern $NamePattern -Quiet)) {
        throw "SKILL.md name does not match directory: $Name"
    }
    if (-not (Select-String -LiteralPath $AgentFile -Pattern '^interface:\s*$' -Quiet)) {
        throw "Invalid agents/openai.yaml interface: $Name"
    }
}

New-Item -ItemType Directory -Path $CodexSkillsDir -Force | Out-Null

$BackupParent = [Environment]::GetFolderPath("Desktop")
if (-not $BackupParent) {
    $BackupParent = $HOME
}
$BackupRoot = Join-Path $BackupParent "aigc-skill-backups"
$MigrationId = [Guid]::NewGuid().ToString("N")
$ResolvedSkillsRoot = Get-NormalizedPath -Path $SkillsRoot

# Preflight every conflict before any removal or backup. Parent enumeration also sees many dangling links.
$Blocked = $false
$NeedsBackup = $false
foreach ($Name in $RetiredSkills) {
    $Path = Join-Path $CodexSkillsDir $Name
    $Item = Get-DirectoryEntry -Directory $CodexSkillsDir -Name $Name
    if (-not $Item) {
        continue
    }
    if (Test-ReparsePoint -Item $Item) {
        $Target = Get-LinkTargetPath -Item $Item -EntryPath $Path
        $Owned = $Target -and $Target.StartsWith($ResolvedSkillsRoot + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)
        if (-not $Owned -and -not $Force) {
            Write-Warning "Retired-name link points outside this repository: $Path. Re-run with -Force to remove it."
            $Blocked = $true
        }
    } elseif (-not $Force) {
        Write-Warning "Retired skill exists as a real directory: $Path. Re-run with -Force to back it up."
        $Blocked = $true
    } else {
        $NeedsBackup = $true
    }
}

foreach ($Name in $ActiveSkills) {
    $Source = Join-Path $SkillsRoot $Name
    $Destination = Join-Path $CodexSkillsDir $Name
    $ResolvedSource = Get-NormalizedPath -Path $Source
    $Existing = Get-DirectoryEntry -Directory $CodexSkillsDir -Name $Name
    if (-not $Existing) {
        continue
    }
    if (Test-ReparsePoint -Item $Existing) {
        $CurrentTarget = Get-LinkTargetPath -Item $Existing -EntryPath $Destination
        if (-not (Test-SamePath -Left $CurrentTarget -Right $ResolvedSource) -and -not $Force) {
            Write-Warning "Exists and points elsewhere: $Destination. Re-run with -Force to replace it."
            $Blocked = $true
        }
    } elseif (-not $Force) {
        Write-Warning "Exists as a real directory: $Destination. Re-run with -Force to back it up and replace it."
        $Blocked = $true
    } else {
        $NeedsBackup = $true
    }
}

if ($Blocked) {
    throw "No changes were made. Resolve the reported conflicts or re-run with -Force."
}

if ($NeedsBackup) {
    New-Item -ItemType Directory -Path $BackupRoot -Force | Out-Null
    if (-not (Test-Path -LiteralPath $BackupRoot -PathType Container)) {
        throw "Backup directory is unavailable: $BackupRoot"
    }
}

$TempLinks = @()
try {
    # Prove that all five junctions can be created before retiring anything.
    foreach ($Name in $ActiveSkills) {
        $Source = Join-Path $SkillsRoot $Name
        $TempName = ".aigc-migration-$MigrationId-$Name"
        $TempPath = Join-Path $CodexSkillsDir $TempName
        if (Get-DirectoryEntry -Directory $CodexSkillsDir -Name $TempName) {
            throw "Temporary migration path already exists: $TempPath"
        }
        New-Item -ItemType Junction -Path $TempPath -Target (Get-NormalizedPath -Path $Source) | Out-Null
        $TempLinks += $TempPath
        $TempItem = Get-DirectoryEntry -Directory $CodexSkillsDir -Name $TempName
        $TempTarget = Get-LinkTargetPath -Item $TempItem -EntryPath $TempPath
        if (-not (Test-SamePath -Left $TempTarget -Right (Get-NormalizedPath -Path $Source))) {
            throw "Temporary junction verification failed: $Name"
        }
    }

    Write-Host "Validated replacement suite: $($ActiveSkills -join ', ')"
    Write-Host "Target Codex skills directory: $CodexSkillsDir"

    # Install and verify the complete active set before retiring old names.
    for ($Index = 0; $Index -lt $ActiveSkills.Count; $Index++) {
        $Name = $ActiveSkills[$Index]
        $Source = Join-Path $SkillsRoot $Name
        $ResolvedSource = Get-NormalizedPath -Path $Source
        $Destination = Join-Path $CodexSkillsDir $Name
        $TempPath = $TempLinks[$Index]
        $Existing = Get-DirectoryEntry -Directory $CodexSkillsDir -Name $Name

        if ($Existing -and (Test-ReparsePoint -Item $Existing)) {
            $CurrentTarget = Get-LinkTargetPath -Item $Existing -EntryPath $Destination
            if (Test-SamePath -Left $CurrentTarget -Right $ResolvedSource) {
                Remove-LinkOnly -Item (Get-DirectoryEntry -Directory $CodexSkillsDir -Name (Split-Path -Leaf $TempPath)) -Path $TempPath
                Write-Host "Already linked: $Name"
                continue
            }

            $HoldName = ".aigc-previous-$MigrationId-$Name"
            $HoldPath = Join-Path $CodexSkillsDir $HoldName
            Move-Item -LiteralPath $Destination -Destination $HoldPath
            try {
                Move-Item -LiteralPath $TempPath -Destination $Destination
                $Installed = Get-DirectoryEntry -Directory $CodexSkillsDir -Name $Name
                if (-not (Test-SamePath -Left (Get-LinkTargetPath -Item $Installed -EntryPath $Destination) -Right $ResolvedSource)) {
                    throw "Active junction verification failed: $Name"
                }
                Remove-LinkOnly -Item (Get-DirectoryEntry -Directory $CodexSkillsDir -Name $HoldName) -Path $HoldPath
            } catch {
                $Failed = Get-DirectoryEntry -Directory $CodexSkillsDir -Name $Name
                if ($Failed -and (Test-ReparsePoint -Item $Failed)) {
                    Remove-LinkOnly -Item $Failed -Path $Destination
                }
                Move-Item -LiteralPath $HoldPath -Destination $Destination
                throw
            }
        } elseif ($Existing) {
            $Backup = New-BackupPath -Name $Name
            Move-Item -LiteralPath $Destination -Destination $Backup
            try {
                Move-Item -LiteralPath $TempPath -Destination $Destination
                $Installed = Get-DirectoryEntry -Directory $CodexSkillsDir -Name $Name
                if (-not (Test-SamePath -Left (Get-LinkTargetPath -Item $Installed -EntryPath $Destination) -Right $ResolvedSource)) {
                    throw "Active junction verification failed: $Name"
                }
                Write-Host "Backed up existing directory to: $Backup"
            } catch {
                $Failed = Get-DirectoryEntry -Directory $CodexSkillsDir -Name $Name
                if ($Failed -and (Test-ReparsePoint -Item $Failed)) {
                    Remove-LinkOnly -Item $Failed -Path $Destination
                }
                Move-Item -LiteralPath $Backup -Destination $Destination
                throw
            }
        } else {
            Move-Item -LiteralPath $TempPath -Destination $Destination
        }

        $Installed = Get-DirectoryEntry -Directory $CodexSkillsDir -Name $Name
        if (-not $Installed -or -not (Test-ReparsePoint -Item $Installed) -or -not (Test-SamePath -Left (Get-LinkTargetPath -Item $Installed -EntryPath $Destination) -Right $ResolvedSource)) {
            throw "Active junction verification failed: $Name"
        }
        Write-Host "Linked: $Name"
    }

    # Only now retire old names.
    foreach ($Name in $RetiredSkills) {
        $Path = Join-Path $CodexSkillsDir $Name
        $Item = Get-DirectoryEntry -Directory $CodexSkillsDir -Name $Name
        if (-not $Item) {
            continue
        }
        if (Test-ReparsePoint -Item $Item) {
            Remove-LinkOnly -Item $Item -Path $Path
            Write-Host "Removed retired skill link: $Name"
        } else {
            $Backup = New-BackupPath -Name $Name
            Move-Item -LiteralPath $Path -Destination $Backup
            Write-Host "Backed up retired skill directory to: $Backup"
        }
    }

    # Postflight.
    foreach ($Name in $ActiveSkills) {
        $Source = Join-Path $SkillsRoot $Name
        $Destination = Join-Path $CodexSkillsDir $Name
        $Item = Get-DirectoryEntry -Directory $CodexSkillsDir -Name $Name
        if (-not $Item -or -not (Test-ReparsePoint -Item $Item) -or -not (Test-SamePath -Left (Get-LinkTargetPath -Item $Item -EntryPath $Destination) -Right (Get-NormalizedPath -Path $Source))) {
            throw "Postflight failed for active skill: $Name"
        }
    }
    foreach ($Name in $RetiredSkills) {
        if (Get-DirectoryEntry -Directory $CodexSkillsDir -Name $Name) {
            throw "Postflight found a retired entry: $Name"
        }
    }

    Write-Host "Done. Five replacement skills are linked and known retired entries are absent. Restart Codex to reload them."
} finally {
    foreach ($TempPath in $TempLinks) {
        $TempName = Split-Path -Leaf $TempPath
        $TempItem = Get-DirectoryEntry -Directory $CodexSkillsDir -Name $TempName
        if ($TempItem -and (Test-ReparsePoint -Item $TempItem)) {
            Remove-LinkOnly -Item $TempItem -Path $TempPath
        }
    }
}
