#!/usr/bin/env bash
set -euo pipefail

FORCE=0
CODEX_SKILLS_DIR=""

for arg in "$@"; do
  case "$arg" in
    --force|-f) FORCE=1 ;;
    --codex-skills-dir=*) CODEX_SKILLS_DIR="${arg#*=}" ;;
    *)
      echo "Unknown argument: $arg" >&2
      exit 2
      ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILLS_ROOT="$REPO_ROOT/skills"

ACTIVE_SKILLS=(
  "aigc-image"
  "aigc-video"
  "aigc-vfx-combat"
  "aigc-project-context"
)

RETIRED_SKILLS=(
  "aigc-prompt-rewrite"
  "aigc-image-edit-prompt"
  "aigc-image-reverse-prompt"
  "aigc-visual-diagnose"
  "aigc-vibe-creating-prompt"
  "aigc-seedance-prompt"
  "aigc-script-context"
  "aigc-natural-language-prompt"
  "aigc-creative-director"
  "aigc-project-planner"
  "aigc-shot-diagnosis-pipeline"
  "aigc-workflow-router"
  "aigc-shot-diagnose"
  "cinematic-storyboard-enhancer"
  "seedance-prompt-master"
)

if [[ -z "$CODEX_SKILLS_DIR" ]]; then
  if [[ -n "${CODEX_HOME:-}" ]]; then
    CODEX_SKILLS_DIR="$CODEX_HOME/skills"
  else
    CODEX_SKILLS_DIR="$HOME/.codex/skills"
  fi
fi

if [[ ! -d "$SKILLS_ROOT" ]]; then
  echo "Skills directory not found: $SKILLS_ROOT" >&2
  exit 1
fi

# Validate the complete replacement before touching the installed set.
for name in "${ACTIVE_SKILLS[@]}"; do
  source="$SKILLS_ROOT/$name"
  if [[ ! -f "$source/SKILL.md" || ! -f "$source/agents/openai.yaml" ]]; then
    echo "Incomplete skill: $source" >&2
    exit 1
  fi
  if ! grep -Eq "^name:[[:space:]]*$name[[:space:]]*$" "$source/SKILL.md"; then
    echo "SKILL.md name does not match directory: $name" >&2
    exit 1
  fi
  if ! grep -Eq '^interface:[[:space:]]*$' "$source/agents/openai.yaml"; then
    echo "Invalid agents/openai.yaml interface: $name" >&2
    exit 1
  fi
done

mkdir -p "$CODEX_SKILLS_DIR"

BACKUP_PARENT="$HOME"
if [[ -d "$HOME/Desktop" ]]; then
  BACKUP_PARENT="$HOME/Desktop"
fi
BACKUP_ROOT="$BACKUP_PARENT/aigc-skill-backups"
MIGRATION_ID="$(date +%Y%m%d-%H%M%S)-$$"

resolved_directory() {
  local path="$1"
  (cd "$path" 2>/dev/null && pwd -P) || true
}

repo_owned_retired_link() {
  local path="$1"
  local name="$2"
  local raw_target
  raw_target="$(readlink "$path")"
  if [[ "$raw_target" == "$SKILLS_ROOT/$name" ]]; then
    return 0
  fi
  local resolved
  resolved="$(resolved_directory "$path")"
  [[ -n "$resolved" && "$resolved" == "$SKILLS_ROOT/"* ]]
}

new_backup_path() {
  local name="$1"
  local candidate="$BACKUP_ROOT/${name}.backup-$MIGRATION_ID"
  local suffix=0
  while [[ -e "$candidate" || -L "$candidate" ]]; do
    suffix=$((suffix + 1))
    candidate="$BACKUP_ROOT/${name}.backup-$MIGRATION_ID-$suffix"
  done
  printf '%s\n' "$candidate"
}

# Preflight every conflict before any removal or backup.
blocked=0
needs_backup=0
for name in "${RETIRED_SKILLS[@]}"; do
  path="$CODEX_SKILLS_DIR/$name"
  if [[ -L "$path" ]]; then
    if [[ "$FORCE" -ne 1 ]] && ! repo_owned_retired_link "$path" "$name"; then
      echo "Retired-name link points outside this repository: $path. Re-run with --force to remove it." >&2
      blocked=1
    fi
  elif [[ -e "$path" && "$FORCE" -ne 1 ]]; then
    echo "Retired skill exists as a real directory: $path. Re-run with --force to back it up." >&2
    blocked=1
  elif [[ -e "$path" ]]; then
    needs_backup=1
  fi
done

for name in "${ACTIVE_SKILLS[@]}"; do
  source="$SKILLS_ROOT/$name"
  destination="$CODEX_SKILLS_DIR/$name"
  if [[ -L "$destination" ]]; then
    if [[ "$(resolved_directory "$destination")" != "$(resolved_directory "$source")" && "$FORCE" -ne 1 ]]; then
      echo "Exists and points elsewhere: $destination. Re-run with --force to replace it." >&2
      blocked=1
    fi
  elif [[ -e "$destination" && "$FORCE" -ne 1 ]]; then
    echo "Exists as a real directory: $destination. Re-run with --force to back it up and replace it." >&2
    blocked=1
  elif [[ -e "$destination" ]]; then
    needs_backup=1
  fi
done

if [[ "$blocked" -ne 0 ]]; then
  echo "No changes were made." >&2
  exit 1
fi

if [[ "$needs_backup" -eq 1 ]]; then
  mkdir -p "$BACKUP_ROOT"
  if [[ ! -d "$BACKUP_ROOT" || ! -w "$BACKUP_ROOT" ]]; then
    echo "Backup directory is not writable: $BACKUP_ROOT" >&2
    exit 1
  fi
fi

# Prove that all four links can be created in the target directory before retiring anything.
TEMP_LINKS=()
cleanup_temp_links() {
  local temp
  for temp in "${TEMP_LINKS[@]}"; do
    if [[ -L "$temp" ]]; then
      rm "$temp"
    fi
  done
}
trap cleanup_temp_links EXIT

for name in "${ACTIVE_SKILLS[@]}"; do
  source="$SKILLS_ROOT/$name"
  temp="$CODEX_SKILLS_DIR/.aigc-migration-$MIGRATION_ID-$name"
  if [[ -e "$temp" || -L "$temp" ]]; then
    echo "Temporary migration path already exists: $temp" >&2
    exit 1
  fi
  ln -s "$source" "$temp"
  TEMP_LINKS+=("$temp")
  if [[ "$(resolved_directory "$temp")" != "$(resolved_directory "$source")" ]]; then
    echo "Temporary link verification failed: $name" >&2
    exit 1
  fi
done

echo "Validated replacement suite: ${ACTIVE_SKILLS[*]}"
echo "Target Codex skills directory: $CODEX_SKILLS_DIR"

# Install and verify the complete active set before retiring old names.
for index in "${!ACTIVE_SKILLS[@]}"; do
  name="${ACTIVE_SKILLS[$index]}"
  source="$SKILLS_ROOT/$name"
  destination="$CODEX_SKILLS_DIR/$name"
  temp="${TEMP_LINKS[$index]}"

  if [[ -L "$destination" && "$(resolved_directory "$destination")" == "$(resolved_directory "$source")" ]]; then
    rm "$temp"
    echo "Already linked: $name"
    continue
  fi

  if [[ -L "$destination" ]]; then
    hold="$CODEX_SKILLS_DIR/.aigc-previous-$MIGRATION_ID-$name"
    mv "$destination" "$hold"
    if mv "$temp" "$destination" && [[ "$(resolved_directory "$destination")" == "$(resolved_directory "$source")" ]]; then
      rm "$hold"
    else
      [[ -L "$destination" ]] && rm "$destination"
      mv "$hold" "$destination"
      echo "Failed to replace active link; restored previous entry: $name" >&2
      exit 1
    fi
  elif [[ -e "$destination" ]]; then
    backup="$(new_backup_path "$name")"
    mv "$destination" "$backup"
    if mv "$temp" "$destination" && [[ "$(resolved_directory "$destination")" == "$(resolved_directory "$source")" ]]; then
      echo "Backed up existing directory to: $backup"
    else
      [[ -L "$destination" ]] && rm "$destination"
      mv "$backup" "$destination"
      echo "Failed to replace active directory; restored previous entry: $name" >&2
      exit 1
    fi
  else
    mv "$temp" "$destination"
  fi

  if [[ ! -L "$destination" || "$(resolved_directory "$destination")" != "$(resolved_directory "$source")" ]]; then
    echo "Active link verification failed: $name" >&2
    exit 1
  fi
  echo "Linked: $name"
done

# Only now retire old entry names. Links are removed; real directories are backed up.
for name in "${RETIRED_SKILLS[@]}"; do
  path="$CODEX_SKILLS_DIR/$name"
  if [[ -L "$path" ]]; then
    rm "$path"
    echo "Removed retired skill link: $name"
  elif [[ -e "$path" ]]; then
    backup="$(new_backup_path "$name")"
    mv "$path" "$backup"
    echo "Backed up retired skill directory to: $backup"
  fi
done

# Postflight: four correct active links and no known retired entries.
for name in "${ACTIVE_SKILLS[@]}"; do
  source="$SKILLS_ROOT/$name"
  destination="$CODEX_SKILLS_DIR/$name"
  if [[ ! -L "$destination" || "$(resolved_directory "$destination")" != "$(resolved_directory "$source")" ]]; then
    echo "Postflight failed for active skill: $name" >&2
    exit 1
  fi
done

for name in "${RETIRED_SKILLS[@]}"; do
  path="$CODEX_SKILLS_DIR/$name"
  if [[ -e "$path" || -L "$path" ]]; then
    echo "Postflight found a retired entry: $path" >&2
    exit 1
  fi
done

trap - EXIT
echo "Done. Four replacement skills are linked and known retired entries are absent. Restart Codex to reload them."
