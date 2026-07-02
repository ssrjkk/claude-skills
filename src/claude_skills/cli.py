from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from claude_skills.catalog import CatalogBuilder
from claude_skills.models import QualityScore, SkillFile
from claude_skills.quality import QualityAnalyzer, QualityReport
from claude_skills.validator import ValidationPipeline


def cmd_validate(args: argparse.Namespace) -> int:
    skills_dir = Path(args.dir)
    pipeline = ValidationPipeline(skills_dir)

    start = time.time()
    results = pipeline.run_all()
    elapsed = time.time() - start

    report = pipeline.report(results)

    print(f"Validation complete: {report['total']} files in {elapsed:.2f}s")
    print(f"  Errors:   {report['errors']}")
    print(f"  Warnings: {report['warnings']}")
    print(f"  Info:     {report['info']}")

    if report["error_details"]:
        print("\nErrors:")
        for e in report["error_details"][:10]:
            print(f"  {e}")
    if report["warning_details"]:
        print("\nWarnings (first 10):")
        for w in report["warning_details"][:10]:
            print(f"  {w}")

    return 1 if report["errors"] > 0 else 0


def cmd_quality(args: argparse.Namespace) -> int:
    skills_dir = Path(args.dir)
    analyzer = QualityAnalyzer()
    scores: dict[str, QualityScore] = {}

    for sk_path in sorted(skills_dir.rglob("SKILL.md")):
        skill_file = SkillFile(en_path=sk_path)
        content = sk_path.read_text(encoding="utf-8")
        skill_file.en_content = content

        end = content.find("---", 3)
        if end > 0:
            import yaml  # type: ignore[import-untyped]
            try:
                skill_file.en_frontmatter = yaml.safe_load(content[3:end].strip()) or {}
            except yaml.YAMLError:
                skill_file.en_frontmatter = {}
            skill_file.en_body = content[end + 3 :].strip()

        ru_path = sk_path.parent / "SKILL.ru.md"
        if ru_path.exists():
            skill_file.ru_path = ru_path
            ru_content = ru_path.read_text(encoding="utf-8")
            skill_file.ru_content = ru_content
            end_ru = ru_content.find("---", 3)
            if end_ru > 0:
                skill_file.ru_body = ru_content[end_ru + 3 :].strip()

        scores[sk_path.parent.name] = analyzer.analyze(skill_file)

    report = QualityReport(scores)
    print(report.summary())

    if args.json:
        out_path = Path(args.json)
        out_path.write_text(
            json.dumps(
                {
                    "summary": {
                        "total": len(scores),
                        "average": {
                            "completeness": report.average.completeness,
                            "depth": report.average.depth,
                            "code_quality": report.average.code_quality,
                            "freshness": report.average.freshness,
                            "bilingual": report.average.bilingual,
                            "overall": report.average.overall,
                        },
                        "grades": report.grade_distribution,
                    },
                    "skills": {name: {"overall": s.overall, "grade": s.grade} for name, s in scores.items()},
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        print(f"\nReport saved to {out_path}")

    return 0


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
        import json
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


def main() -> int:
    parser = argparse.ArgumentParser(description="Claude Skills SDK")
    sub = parser.add_subparsers(dest="command", required=True)

    p_validate = sub.add_parser("validate", help="Validate all skills")
    p_validate.add_argument("--dir", default=".claude/skills", help="Skills directory")
    p_validate.set_defaults(func=cmd_validate)

    p_quality = sub.add_parser("quality", help="Analyze skill quality")
    p_quality.add_argument("--dir", default=".claude/skills", help="Skills directory")
    p_quality.add_argument("--json", help="Output JSON report to path")
    p_quality.set_defaults(func=cmd_quality)

    p_catalog = sub.add_parser("catalog", help="Build catalog from skills")
    p_catalog.add_argument("--root", help="Project root directory")
    p_catalog.add_argument("-o", "--output", help="Output path for catalog JSON")
    p_catalog.set_defaults(func=cmd_catalog)

    p_stats = sub.add_parser("stats", help="Show statistics")
    p_stats.add_argument("--root", help="Project root directory")
    p_stats.add_argument("--output", help="Save stats to JSON")
    p_stats.set_defaults(func=cmd_stats)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
