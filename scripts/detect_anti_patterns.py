#!/usr/bin/env python3
"""Detect anti-patterns in skill definitions."""

import json
import sys
from pathlib import Path

from colorama import Fore, Style, init

init(autoreset=True)

ANTI_PATTERNS = {
    'steps': ['think about', 'consider', 'learn', 'understand', 'might', 'could'],
    'title': ['learn', 'understand', 'know', 'about']
}


def detect_patterns(filepath: Path) -> int:
    """Detect anti-patterns in skills."""
    with open(filepath, 'r') as f:
        data = json.load(f)

    issues = 0
    for skill in data.get('skills', []):
        skill_id = skill.get('id', 'Unknown')

        # Check title
        title = str(skill.get('title', '')).lower()
        for pattern in ANTI_PATTERNS['title']:
            if pattern in title:
                print(f"{Fore.YELLOW}Skill {skill_id}: Title contains '{pattern}': {skill.get('title')}{Style.RESET_ALL}")
                issues += 1

        # Check steps
        for i, step in enumerate(skill.get('steps', []), 1):
            step_lower = str(step).lower()
            for pattern in ANTI_PATTERNS['steps']:
                if pattern in step_lower:
                    print(f"{Fore.YELLOW}Skill {skill_id} Step {i}: Contains '{pattern}': {step}{Style.RESET_ALL}")
                    issues += 1
                    break

    if issues == 0:
        print(f"{Fore.GREEN}✅ No anti-patterns detected{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}⚠️  {issues} potential issue(s) found{Style.RESET_ALL}")

    return 0  # Don't fail on warnings


def main() -> int:
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Detect anti-patterns in skills")
    parser.add_argument('filepath', help="Path to skills_library.json")
    args = parser.parse_args()

    filepath = Path(args.filepath)
    return detect_patterns(filepath)


if __name__ == '__main__':
    sys.exit(main())
