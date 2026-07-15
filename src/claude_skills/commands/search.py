from __future__ import annotations

import difflib
import json
import sys
from pathlib import Path
from typing import Optional
import argparse

from claude_skills.catalog import CatalogBuilder


def _find_catalog() -> Optional[Path]:
    for path in [Path("skills_catalog.json"), Path("../skills_catalog.json")]:
        if path.exists():
            return path
    return None


def _get_skills_base() -> Path:
    for path in [Path(".claude/skills"), Path("../.claude/skills")]:
        if path.exists():
            return path.resolve()
    return Path(".claude/skills")


def cmd_search(args: argparse.Namespace) -> int:
    query = args.query.lower()
    limit = args.limit

    catalog_path = _find_catalog()
    if catalog_path:
        catalog = CatalogBuilder.from_json(catalog_path)
        skills_list = catalog.skills
    else:
        skills_base = _get_skills_base()
        if skills_base.exists():
            builder = CatalogBuilder()
            catalog = builder.build_catalog()
            skills_list = catalog.skills
        else:
            print("Error: no catalog found. Generate one with 'claude-skills catalog'", file=sys.stderr)
            return 1

    results = []
    for s in skills_list:
        name = s.name.lower()
        desc = s.description.lower()
        tags = [t.lower() for t in s.tags]
        name_ratio = difflib.SequenceMatcher(None, query, name).ratio()
        tag_match = any(query in t or difflib.SequenceMatcher(None, query, t).ratio() > 0.6 for t in tags)
        query_in_name = query in name
        query_in_desc = query in desc

        if query_in_name or query_in_desc or tag_match or name_ratio > 0.4:
            score = 0
            if query_in_name:
                score += 100
            if query_in_desc:
                score += 50
            if tag_match:
                score += 75
            score += int(name_ratio * 50)
            results.append((score, s))

    if args.category:
        results = [(s, skill) for s, skill in results if skill.category == args.category]
    if args.tag:
        results = [(s, skill) for s, skill in results if args.tag.lower() in [t.lower() for t in skill.tags]]

    results.sort(key=lambda x: -x[0])
    results = results[:limit]

    if args.json:
        data = [
            {
                "name": s.name,
                "description": s.description,
                "category": s.category,
                "tags": s.tags,
                "version": s.version,
                "has_ru": s.has_ru,
            }
            for _, s in results
        ]
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        if not results:
            print(f"No skills found for '{query}'")
            return 0
        print(f"Found {len(results)} skill(s) for '{query}':\n")
        for idx, (_, s) in enumerate(results, 1):
            ru_tag = " [RU]" if s.has_ru else ""
            print(f"  {idx}. {s.name}{ru_tag}")
            print(f"       {s.description}")
            print(f"       Category: {s.category} | Tags: {', '.join(s.tags[:5])}")
            print()

    return 0
