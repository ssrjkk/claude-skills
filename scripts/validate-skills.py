#!/usr/bin/env python3
"""
validate-skills.py - Validate structure and content of Claude Skills
"""
import os
import re
import json
import sys
from pathlib import Path

SKILLS_DIR = Path(__file__).parent.parent / ".claude" / "skills"
MAX_NAME_LEN = 64
MAX_DESC_LEN = 1024

def validate_skill(skill_path):
    errors = []
    skill_name = skill_path.name
    
    # Check name
    if not re.match(r'^[a-z0-9-]+$', skill_name):
        errors.append(f"Invalid name: {skill_name}")
    if len(skill_name) > MAX_NAME_LEN:
        errors.append(f"Name too long: {skill_name}")
    
    # Check SKILL.md exists
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return errors  # Skip directories without SKILL.md
    
    # Parse YAML frontmatter
    content = skill_md.read_text(encoding='utf-8')
    if not content.startswith('---\n'):
        errors.append(f"No YAML frontmatter in {skill_name}")
    else:
        # Extract description
        desc_match = re.search(r'description:\s*(.+)', content)
        if desc_match:
            desc = desc_match.group(1).strip()
            if len(desc) > MAX_DESC_LEN:
                errors.append(f"Description too long in {skill_name}")
        else:
            errors.append(f"Missing description in {skill_name}")
    
    return errors

def main():
    all_errors = []
    
    def traverse(directory):
        for item in directory.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                # Check if this is a skill directory (has SKILL.md)
                if (item / "SKILL.md").exists():
                    errors = validate_skill(item)
                    all_errors.extend(errors)
                else:
                    # Traverse subdirectories
                    traverse(item)
    
    traverse(SKILLS_DIR)
    
    if all_errors:
        print("Validation FAILED:")
        for err in all_errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("Validation PASSED")
        sys.exit(0)

if __name__ == "__main__":
    main()
