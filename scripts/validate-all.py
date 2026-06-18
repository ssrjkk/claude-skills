#!/usr/bin/env python3
"""Thin wrapper: validate all skills using the SDK."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from claude_skills.cli import cmd_validate
from claude_skills.models import Severity


def main() -> int:
    class Args:
        dir = ".claude/skills"

    return cmd_validate(Args())


if __name__ == "__main__":
    sys.exit(main())
