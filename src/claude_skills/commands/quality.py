from __future__ import annotations

import json
from pathlib import Path
import argparse

from claude_skills.models import QualityScore, SkillFile
from claude_skills.quality import QualityAnalyzer, QualityReport


def cmd_quality(args: argparse.Namespace) -> int:
    import yaml
    skills_dir = Path(args.dir)
    analyzer = QualityAnalyzer()
    scores: dict[str, QualityScore] = {}

    for sk_path in sorted(skills_dir.rglob("SKILL.md")):
        skill_file = SkillFile(en_path=sk_path)
        content = sk_path.read_text(encoding="utf-8")
        skill_file.en_content = content

        end = content.find("---", 3)
        if end > 0:
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
