from __future__ import annotations

import json
from pathlib import Path
import argparse

from claude_skills.catalog import CatalogBuilder


def cmd_catalog(args: argparse.Namespace) -> int:
    builder = CatalogBuilder(root=Path(args.root) if args.root else None)
    catalog = builder.build_catalog()

    out_path = Path(args.output) if args.output else Path("skills_catalog.json")
    builder.to_json(catalog, path=out_path)

    print(f"Catalog: {catalog.metadata.total_skills} skills, {len(catalog.metadata.domains)} domains")
    print(f"  RU: {catalog.metadata.total_ru} skills")
    print(f"  Saved to {out_path}")
    return 0


def cmd_stats(args: argparse.Namespace) -> int:
    builder = CatalogBuilder(root=Path(args.root) if args.root else None)
    catalog = builder.build_catalog()

    by_cat = catalog.by_category
    print(f"{'='*60}")
    print("  CLAUDE SKILLS LIBRARY — STATISTICS")
    print(f"{'='*60}")
    print(f"  Total skills:    {catalog.metadata.total_skills}")
    print(f"  Total RU:        {catalog.metadata.total_ru}")
    print(f"  Bilingual rate:  {catalog.metadata.total_ru/max(catalog.metadata.total_skills,1)*100:.1f}%")
    print(f"  Domains:         {len(catalog.metadata.domains)}")
    print(f"  Schema version:  {catalog.metadata.schema_version}")
    print(f"  Generated:       {catalog.metadata.generated_at}")
    print()
    print("  By domain:")
    for domain in sorted(by_cat):
        skills = by_cat[domain]
        ru_in_cat = sum(1 for s in skills if s.has_ru)
        print(f"    {domain:25s}: {len(skills):5d} skills, {ru_in_cat:5d} RU")

    if args.output:
        text = json.dumps(
            {
                "total_skills": catalog.metadata.total_skills,
                "total_ru": catalog.metadata.total_ru,
                "bilingual_rate": round(catalog.metadata.total_ru / max(catalog.metadata.total_skills, 1) * 100, 1),
                "domains": sorted(catalog.metadata.domains),
                "domain_skills": {d: len(by_cat[d]) for d in sorted(by_cat)},
            },
            indent=2,
            ensure_ascii=False,
        )
        Path(args.output).write_text(text, encoding="utf-8")
        print(f"\n  Stats saved to {args.output}")

    return 0
