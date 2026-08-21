#!/usr/bin/env sh
set -eu

usage() {
  printf '%s\n' "Usage: $0 [--force]"
}

force=0
case "${1:-}" in
  "") ;;
  --force) force=1 ;;
  -h|--help)
    usage
    exit 0
    ;;
  *)
    usage >&2
    exit 2
    ;;
esac

script_dir=$(CDPATH= cd "$(dirname "$0")" && pwd)
repo_dir=$(dirname "$script_dir")
source_dir="$repo_dir/skills/sae"
skills_dir="${CODEX_HOME:-$HOME/.codex}/skills"
target_dir="$skills_dir/sae"

if [ ! -f "$source_dir/SKILL.md" ]; then
  printf '%s\n' "Error: installable skill not found at $source_dir" >&2
  exit 1
fi

if [ -e "$target_dir" ]; then
  if [ "$force" -ne 1 ]; then
    printf '%s\n' "Error: $target_dir already exists." >&2
    printf '%s\n' "Run $0 --force to replace it." >&2
    exit 1
  fi
  rm -rf "$target_dir"
fi

mkdir -p "$skills_dir"
cp -R "$source_dir" "$target_dir"
printf '%s\n' "Installed SAE to $target_dir"
