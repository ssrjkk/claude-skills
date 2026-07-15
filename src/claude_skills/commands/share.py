from __future__ import annotations

import sys
import urllib.parse
from pathlib import Path
import argparse

from claude_skills.commands.install import REPO


def cmd_share(args: argparse.Namespace) -> int:
    import yaml

    target = Path(args.skill)

    if target.is_dir():
        skill_path = target / "SKILL.md"
    else:
        skill_path = target

    if not skill_path.exists():
        print(f"Error: '{skill_path}' not found", file=sys.stderr)
        return 1

    content = skill_path.read_text(encoding="utf-8")
    end = content.find("---", 3)
    if end < 0:
        print("Error: invalid skill file (no frontmatter)", file=sys.stderr)
        return 1

    front = content[3:end].strip()
    try:
        fm = yaml.safe_load(front) or {}
    except yaml.YAMLError:
        print("Error: invalid YAML frontmatter", file=sys.stderr)
        return 1

    name = fm.get("name", skill_path.parent.name)
    desc = fm.get("description", "")
    category = fm.get("category", "unknown")

    if args.github:
        body = (
            f"## Skill Submission\n\n"
            f"**Name:** {name}\n"
            f"**Category:** {category}\n"
            f"**Description:** {desc}\n\n"
            f"**Content:**\n```markdown\n{content}\n```\n"
        )
        params = urllib.parse.urlencode({
            "title": f"Share skill: {name}",
            "body": body,
            "labels": "skill-submission",
        })
        url = f"https://github.com/{REPO}/issues/new?{params}"
        print(f"Open this URL to submit your skill:\n{url}")
    elif args.text:
        print(f"[Skill] {name}")
        print(f"[Category] {category}")
        print(f"[Description] {desc}")
        print()
        print(f"Install: claude-skills install {name}")
        print()
        body = (content[end + 3:]).strip()
        preview = body[:500] + "..." if len(body) > 500 else body
        print(f"Content preview:\n{preview}")
    else:
        print(f"Name:        {name}")
        print(f"Category:    {category}")
        print(f"Description: {desc}")
        print(f"Path:        {skill_path}")
        print(f"Install:     claude-skills install {name}")
        print()
        print("Use --github to create a GitHub issue or --text for a text summary.")

    return 0
