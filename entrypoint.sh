#!/bin/sh
set -e

COMMAND="${1:-validate}"
shift 2>/dev/null || true

case "$COMMAND" in
  validate)
    python -m claude_skills.cli validate "$@"
    ;;
  quality)
    python -m claude_skills.cli quality "$@"
    ;;
  catalog)
    python -m claude_skills.cli catalog "$@"
    ;;
  stats)
    python -m claude_skills.cli stats "$@"
    ;;
  *)
    echo "Usage: validate|quality|catalog|stats [options]"
    exit 1
    ;;
esac
