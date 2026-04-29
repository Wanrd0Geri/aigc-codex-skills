[CmdletBinding()]
param(
    [string]$CodexSkillsDir,
    [switch]$Force
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$SkillsRoot = Join-Path $RepoRoot "skills"

if (-not $CodexSkillsDir) {
    if ($env:CODEX_HOME) {
        $CodexSkillsDir = Join-Path $env:CODEX_HOME "skills"
    } else {
        $CodexSkillsDir = Join-Path $HOME ".codex\skills"
    }
}

if (-not (Test-Path -LiteralPath $SkillsRoot)) {
    throw "Skills directory not found: $SkillsRoot"
}

New-Item -ItemType Directory -Path $CodexSkillsDir -Force | Out-Null

$ResolvedSkillsRoot = (Resolve-Path -LiteralPath $SkillsRoot).Path
Write-Host "Linking skills from $ResolvedSkillsRoot"
Write-Host "Target Codex skills directory: $CodexSkillsDir"

$LegacySkillNames = @(
    "aigc-workflow-router",
    "aigc-shot-diagnose",
    "cinematic-storyboard-enhancer",
    "seedance-prompt-master"
)

foreach ($LegacyName in $LegacySkillNames) {
    $LegacyPath = Join-Path $CodexSkillsDir $LegacyName
    if (-not (Test-Path -LiteralPath $LegacyPath)) {
        continue
    }

    $LegacyItem = Get-Item -LiteralPath $LegacyPath -Force
    $IsLegacyReparsePoint = ($LegacyItem.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0

    if ($IsLegacyReparsePoint) {
        if ($LegacyItem.PSIsContainer) {
            [System.IO.Directory]::Delete($LegacyPath)
        } else {
            Remove-Item -LiteralPath $LegacyPath -Force
        }
        Write-Host "Removed legacy skill link: $LegacyName"
    } elseif ($Force) {
        $Stamp = Get-Date -Format "yyyyMMdd-HHmmss"
        $Backup = "$LegacyPath.backup-$Stamp"
        Move-Item -LiteralPath $LegacyPath -Destination $Backup
        Write-Host "Backed up legacy skill directory to: $Backup"
    } else {
        Write-Warning "Legacy skill exists as a real directory: $LegacyPath. Re-run with -Force to back it up."
    }
}

foreach ($Skill in Get-ChildItem -LiteralPath $SkillsRoot -Directory) {
    $Source = $Skill.FullName
    $Destination = Join-Path $CodexSkillsDir $Skill.Name
    $ResolvedSource = (Resolve-Path -LiteralPath $Source).Path

    if (Test-Path -LiteralPath $Destination) {
        $Existing = Get-Item -LiteralPath $Destination -Force
        $IsReparsePoint = ($Existing.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0

        if ($IsReparsePoint) {
            $CurrentTarget = $Existing.Target
            if ($CurrentTarget -is [array]) {
                $CurrentTarget = $CurrentTarget[0]
            }

            $ResolvedCurrent = $null
            if ($CurrentTarget) {
                $ResolvedCurrent = (Resolve-Path -LiteralPath $CurrentTarget -ErrorAction SilentlyContinue).Path
            }

            if ($ResolvedCurrent -eq $ResolvedSource) {
                Write-Host "Already linked: $($Skill.Name)"
                continue
            }

            if (-not $Force) {
                Write-Warning "Exists and points elsewhere: $Destination. Re-run with -Force to replace the link."
                continue
            }

            if ($Existing.PSIsContainer) {
                [System.IO.Directory]::Delete($Destination)
            } else {
                Remove-Item -LiteralPath $Destination -Force
            }
        } else {
            if (-not $Force) {
                Write-Warning "Exists as a real directory: $Destination. Re-run with -Force to back it up and replace it."
                continue
            }

            $Stamp = Get-Date -Format "yyyyMMdd-HHmmss"
            $Backup = "$Destination.backup-$Stamp"
            Move-Item -LiteralPath $Destination -Destination $Backup
            Write-Host "Backed up existing directory to: $Backup"
        }
    }

    New-Item -ItemType Junction -Path $Destination -Target $ResolvedSource | Out-Null
    Write-Host "Linked: $($Skill.Name)"
}

Write-Host "Done. Restart Codex to pick up new skills."
