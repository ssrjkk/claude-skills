"""Tests for the quality analyzer."""

from __future__ import annotations

from pathlib import Path

import pytest

from claude_skills.models import QualityScore, SkillFile
from claude_skills.quality import QualityAnalyzer, QualityReport


class TestQualityAnalyzer:
    @pytest.fixture
    def analyzer(self):
        return QualityAnalyzer()

    def _make_skill_file(self, body: str, ru_body: str = "", created: str = "", models: str = "") -> SkillFile:
        sf = SkillFile(en_path=Path("test/SKILL.md"), en_body=body, en_content=f"---\n---\n{body}")
        if created:
            sf.en_frontmatter = {"created": created, "models": models}
        if ru_body:
            sf.ru_path = Path("test/SKILL.ru.md")
            sf.ru_body = ru_body
            sf.ru_content = f"---\n---\n{ru_body}"
        return sf

    def test_complete_skill_score(self, analyzer: QualityAnalyzer):
        body = "\n\n".join([
            "## 🚀 Quick Start\nContent",
            "## 📋 When to Use\nContent",
            "## 🔧 Step-by-Step\nContent",
            "## 🧪 Examples\nContent",
            "## ✅ Validation\nContent",
        ])
        sf = self._make_skill_file(body=body, created="2026-06-01", ru_body="\n\n".join(["## Быстрый старт\n", "## Когда использовать\n"]))
        score = analyzer.analyze(sf)
        assert score.completeness > 80
        assert score.depth > 0
        assert score.bilingual > 0

    def test_empty_skill_score(self, analyzer: QualityAnalyzer):
        sf = self._make_skill_file(body="")
        score = analyzer.analyze(sf)
        assert score.completeness == 0.0
        assert score.depth == 0.0
        assert score.overall > 0  # bilingual might be > 0 from freshness

    def test_depth_calculation(self, analyzer: QualityAnalyzer):
        short = self._make_skill_file(body="Line1\nLine2\n")
        assert analyzer._score_depth(short) < 50
        long_body = "\n".join([f"Line {i}" for i in range(80)])
        long = self._make_skill_file(body=long_body)
        assert analyzer._score_depth(long) >= 80

    def test_code_quality_no_code(self, analyzer: QualityAnalyzer):
        sf = self._make_skill_file(body="Just text\nNo code blocks\n")
        assert analyzer._score_code_quality(sf) < 30

    def test_code_quality_with_fences(self, analyzer: QualityAnalyzer):
        sf = self._make_skill_file(body="Text\n```python\nx=1\n```\nMore\n```bash\nls\n```\nEnd\n")
        assert analyzer._score_code_quality(sf) >= 70

    def test_freshness_recent(self, analyzer: QualityAnalyzer):
        sf = self._make_skill_file(body="Content", created="2026-06-01")
        assert analyzer._score_freshness(sf) > 80

    def test_freshness_old(self, analyzer: QualityAnalyzer):
        sf = self._make_skill_file(body="Content", created="2025-01-01")
        assert analyzer._score_freshness(sf) < 80

    def test_freshness_no_date(self, analyzer: QualityAnalyzer):
        sf = self._make_skill_file(body="Content")
        assert analyzer._score_freshness(sf) == 30.0

    def test_bilingual_no_ru(self, analyzer: QualityAnalyzer):
        sf = self._make_skill_file(body="Content")
        assert analyzer._score_bilingual(sf) == 0.0

    def test_bilingual_with_ru(self, analyzer: QualityAnalyzer):
        sf = self._make_skill_file(body="EN content\n## Quick Start\nMore", ru_body="RU content\n## Быстрый старт\nMore")
        assert analyzer._score_bilingual(sf) > 0

    def test_completeness_sections(self, analyzer: QualityAnalyzer):
        sf = self._make_skill_file(body="## Quick Start\nContent\n## Validation\nContent")
        score = analyzer._score_completeness(sf)
        assert score > 30  # 2/5 sections + partial frontmatter
        assert score < 100

    def test_overall_zero_edge_case(self, analyzer: QualityAnalyzer):
        sf = self._make_skill_file(body="")
        score = analyzer.analyze(sf)
        assert score.overall >= 0


class TestQualityReport:
    @pytest.fixture
    def scores(self):
        return {
            "skill-a": QualityScore(90, 90, 90, 90, 90),
            "skill-b": QualityScore(70, 70, 70, 70, 70),
            "skill-c": QualityScore(30, 30, 30, 30, 30),
        }

    def test_average(self, scores: dict):
        report = QualityReport(scores)
        avg = report.average
        assert avg.completeness == pytest.approx(63.33, 0.1)
        assert avg.overall == pytest.approx(63.33, 0.1)

    def test_grade_distribution(self, scores: dict):
        report = QualityReport(scores)
        dist = report.grade_distribution
        assert dist["A"] == 1
        assert dist["B"] == 0
        assert dist["C"] == 1
        assert dist["F"] == 1

    def test_top_skills(self, scores: dict):
        report = QualityReport(scores)
        top = report.top_skills(2)
        assert len(top) == 2
        assert top[0][0] == "skill-a"

    def test_bottom_skills(self, scores: dict):
        report = QualityReport(scores)
        bottom = report.bottom_skills(2)
        assert len(bottom) == 2
        assert bottom[0][0] == "skill-c"

    def test_summary_contains_key_metrics(self, scores: dict):
        report = QualityReport(scores)
        summary = report.summary()
        assert "QUALITY REPORT" in summary
        assert "63" in summary
        assert "A" in summary

    def test_empty_report(self):
        report = QualityReport({})
        avg = report.average
        assert avg.overall == 0.0
        assert avg.grade == "F"
        assert report.grade_distribution["F"] == 0
