#!/usr/bin/env python3
"""Thin wrapper: deep validation and quality analysis using the SDK."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from claude_skills.quality import QualityAnalyzer, QualityReport
from claude_skills.models import SkillFile

import yaml


def main() -> int:
    skills_dir = Path(".claude/skills")
    analyzer = QualityAnalyzer()
    scores = {}

    for sk_path in sorted(skills_dir.rglob("SKILL.md")):
        name = sk_path.parent.name
        content = sk_path.read_text(encoding="utf-8")
        sf = SkillFile(en_path=sk_path, en_content=content)
        end = content.find("---", 3)
        if end > 0:
            try:
                sf.en_frontmatter = yaml.safe_load(content[3:end].strip()) or {}
            except yaml.YAMLError:
                sf.en_frontmatter = {}
            sf.en_body = content[end + 3 :].strip()

        ru_path = sk_path.parent / "SKILL.ru.md"
        if ru_path.exists():
            sf.ru_path = ru_path
            ru_content = ru_path.read_text(encoding="utf-8")
            sf.ru_content = ru_content
            end_ru = ru_content.find("---", 3)
            if end_ru > 0:
                sf.ru_body = ru_content[end_ru + 3 :].strip()

        scores[name] = analyzer.analyze(sf)

    report = QualityReport(scores)
    print(report.summary())
    print("\nTop 5 skills:")
    for name, score in report.top_skills(5):
        print(f"  {name}: {score.overall:.1f}% ({score.grade})")
    print("\nBottom 5 skills:")
    for name, score in report.bottom_skills(5):
        print(f"  {name}: {score.overall:.1f}% ({score.grade})")

    failing = sum(1 for s in scores.values() if s.grade == "F")
    if failing > 0:
        print(f"\n{failing} skills have grade F")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
