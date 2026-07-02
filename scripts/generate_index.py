#!/usr/bin/env python3
"""Generate index markdown from skills library."""

import json
from collections import defaultdict
from pathlib import Path


def generate_index(filepath: Path) -> str:
    """Generate index of all skills organized by category."""
    with open(filepath, 'r') as f:
        data = json.load(f)

    skills = data.get('skills', []) + data.get('extended_skills', [])
    by_category = defaultdict(list)

    for skill in skills:
        cat = skill.get('category', 'Other')
        by_category[cat].append(skill)

    md = []
    md.append("# Skills Library Index")
    md.append("")
    md.append(f"Total: **{len(skills)}** skills across **{len(by_category)}** categories")
    md.append("")

    for category in sorted(by_category.keys()):
        skills_in_cat = by_category[category]
        md.append(f"## {category}")
        md.append("")
        for skill in sorted(skills_in_cat, key=lambda s: str(s.get('id', ''))):
            skill_id = skill.get('id', 'N/A')
            title = skill.get('title', 'N/A')
            difficulty = skill.get('difficulty', 'N/A')
            md.append(f"- **{skill_id}** - {title} _(_{difficulty}_)_")
        md.append("")

    md.append("*Auto-generated index - last updated on each push*")

    return "\n".join(md)


def main() -> int:
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Generate skills index")
    parser.add_argument('filepath', help="Path to skills_library.json")
    args = parser.parse_args()

    filepath = Path(args.filepath)
    index = generate_index(filepath)
    print(index)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
