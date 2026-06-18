#!/usr/bin/env python3
"""Thin wrapper: regenerate catalog using the SDK."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from claude_skills.catalog import CatalogBuilder


def main() -> int:
    builder = CatalogBuilder()
    catalog = builder.build_catalog()
    builder.to_json(catalog, path=Path("skills_catalog.json"))
    print(f"Catalog: {catalog.metadata.total_skills} skills, {len(catalog.metadata.domains)} domains")
    print(f"  RU: {catalog.metadata.total_ru}")
    print(f"  Saved to skills_catalog.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
