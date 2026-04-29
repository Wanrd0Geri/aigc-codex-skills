#!/usr/bin/env bash
set -euo pipefail

FORCE=0
CODEX_SKILLS_DIR=""

for arg in "$@"; do
  case "$arg" in
    --force|-f)
      FORCE=1
      ;;
    --codex-skills-dir=*)
      CODEX_SKILLS_DIR="${arg#*=}"
      ;;
    *)
      echo "Unknown argument: $arg" >&2
      exit 2
      ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILLS_ROOT="$REPO_ROOT/skills"

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

mkdir -p "$CODEX_SKILLS_DIR"

echo "Linking skills from $SKILLS_ROOT"
echo "Target Codex skills directory: $CODEX_SKILLS_DIR"

for source in "$SKILLS_ROOT"/*; do
  [[ -d "$source" ]] || continue
  name="$(basename "$source")"
  destination="$CODEX_SKILLS_DIR/$name"

  if [[ -L "$destination" ]]; then
    current_target="$(readlink "$destination")"
    if [[ "$current_target" == "$source" ]]; then
      echo "Already linked: $name"
      continue
    fi

    if [[ "$FORCE" -ne 1 ]]; then
      echo "Exists and points elsewhere: $destination. Re-run with --force to replace the link." >&2
      continue
    fi

    rm "$destination"
  elif [[ -e "$destination" ]]; then
    if [[ "$FORCE" -ne 1 ]]; then
      echo "Exists as a real directory: $destination. Re-run with --force to back it up and replace it." >&2
      continue
    fi

    backup="${destination}.backup-$(date +%Y%m%d-%H%M%S)"
    mv "$destination" "$backup"
    echo "Backed up existing directory to: $backup"
  fi

  ln -s "$source" "$destination"
  echo "Linked: $name"
done

echo "Done. Restart Codex to pick up new skills."
