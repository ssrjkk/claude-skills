"""Tests for the validator."""

from __future__ import annotations

from pathlib import Path

import pytest

from claude_skills.models import Severity
from claude_skills.validator import SkillValidator, ValidationPipeline


class TestSkillValidator:
    @pytest.fixture
    def validator(self):
        return SkillValidator()

    def test_valid_skill(self, validator: SkillValidator, tmp_path: Path):
        path = tmp_path / "test-skill" / "SKILL.md"
        path.parent.mkdir(parents=True)
        path.write_text(
            "---\n"
            "name: test-skill\n"
            "description: A skill\n"
            "category: qa\n"
            "tags: [testing]\n"
            "models: [sonnet, opus]\n"
            "version: 1.0.0\n"
            "created: 2026-01-01\n"
            "---\n"
            "# Test Skill\n\n"
            "## Quick Start\n\nContent\n\n"
            "## Validation\n\nContent\n"
        )
        results = validator.validate_skill_file(path)
        errors = [r for r in results if r.severity == Severity.ERROR]
        assert len(errors) == 0

    def test_missing_frontmatter(self, validator: SkillValidator, tmp_path: Path):
        path = tmp_path / "test" / "SKILL.md"
        path.parent.mkdir(parents=True)
        path.write_text("Just content without frontmatter\n")
        results = validator.validate_skill_file(path)
        errors = [r for r in results if r.severity == Severity.ERROR]
        assert any("E010" in r.code for r in errors)

    def test_missing_required_fields(self, validator: SkillValidator, tmp_path: Path):
        path = tmp_path / "test" / "SKILL.md"
        path.parent.mkdir(parents=True)
        path.write_text("---\nname: test\n---\nContent\n")
        results = validator.validate_skill_file(path)
        errors = [r for r in results if r.severity == Severity.ERROR]
        assert any("E020" in r.code for r in errors)

    def test_short_body_warning(self, validator: SkillValidator, tmp_path: Path):
        path = tmp_path / "test" / "SKILL.md"
        path.parent.mkdir(parents=True)
        path.write_text(
            "---\n"
            "name: test\ndescription: desc\ncategory: qa\ntags: []\nmodels: []\nversion: 1.0.0\n"
            "---\n"
            "Short\n"
        )
        results = validator.validate_skill_file(path)
        warnings = [r for r in results if r.severity == Severity.WARNING]
        assert any("W020" in r.code for r in warnings)

    def test_unbalanced_code_fences(self, validator: SkillValidator, tmp_path: Path):
        path = tmp_path / "test" / "SKILL.md"
        path.parent.mkdir(parents=True)
        path.write_text(
            "---\n"
            "name: test\ndescription: desc\ncategory: qa\ntags: []\nmodels: []\nversion: 1.0.0\n"
            "---\n"
            "# Test\n\n"
            "```python\nprint('hello')\n```\n"
            "```bash\necho hi\n"
        )
        results = validator.validate_skill_file(path)
        errors = [r for r in results if r.severity == Severity.ERROR]
        assert any("E040" in r.code for r in errors)

    def test_placeholder_name(self, validator: SkillValidator, tmp_path: Path):
        path = tmp_path / "skill-0001" / "SKILL.md"
        path.parent.mkdir(parents=True)
        path.write_text(
            "---\n"
            "name: skill-0001\ndescription: desc\ncategory: qa\ntags: []\nmodels: []\nversion: 1.0.0\n"
            "---\n"
            "## Quick Start\n\nContent\n\n## Validation\n\nContent\n"
        )
        results = validator.validate_skill_file(path)
        warnings = [r for r in results if r.severity == Severity.WARNING]
        assert any("W011" in r.code for r in warnings)

    def test_duplicate_tags(self, validator: SkillValidator, tmp_path: Path):
        path = tmp_path / "test" / "SKILL.md"
        path.parent.mkdir(parents=True)
        path.write_text(
            "---\n"
            "name: test\ndescription: desc\ncategory: qa\n"
            "tags: [qa, basics, qa]\nmodels: [sonnet]\nversion: 1.0.0\n"
            "---\n"
            "## Quick Start\n\nContent\n\n## Validation\n\nContent\n"
        )
        results = validator.validate_skill_file(path)
        warnings = [r for r in results if r.severity == Severity.WARNING]
        assert any("W013" in r.code for r in warnings)

    def test_default_model_detection(self, validator: SkillValidator, tmp_path: Path):
        path = tmp_path / "test" / "SKILL.md"
        path.parent.mkdir(parents=True)
        path.write_text(
            "---\n"
            "name: test\ndescription: desc\ncategory: qa\n"
            "tags: [qa]\nmodels: [gpt-4, claude-3]\nversion: 1.0.0\n"
            "---\n"
            "## Quick Start\n\nContent\n\n## Validation\n\nContent\n"
        )
        results = validator.validate_skill_file(path)
        infos = [r for r in results if r.severity == Severity.INFO]
        assert any("I010" in r.code for r in infos)

    def test_unknown_category(self, validator: SkillValidator, tmp_path: Path):
        path = tmp_path / "test" / "SKILL.md"
        path.parent.mkdir(parents=True)
        path.write_text(
            "---\n"
            "name: test\ndescription: desc\ncategory: nonexistent\n"
            "tags: []\nmodels: []\nversion: 1.0.0\n"
            "---\n"
            "## Quick Start\n\nContent\n\n## Validation\n\nContent\n"
        )
        results = validator.validate_skill_file(path)
        warnings = [r for r in results if r.severity == Severity.WARNING]
        assert any("W012" in r.code for r in warnings)


class TestValidationPipeline:
    @pytest.fixture
    def pipeline(self, tmp_path: Path):
        skills_dir = tmp_path / ".claude" / "skills"
        for cat, name in [("qa", "skill-a"), ("ai", "skill-b"), ("backend", "skill-c")]:
            path = skills_dir / cat / name / "SKILL.md"
            path.parent.mkdir(parents=True)
            path.write_text(
                "---\n"
                f"name: {name}\ndescription: desc\ncategory: {cat}\n"
                "tags: [test]\nmodels: [sonnet]\nversion: 1.0.0\n"
                "---\n"
                "# Test\n\n## Quick Start\n\nContent\n\n## Validation\n\nContent\n"
            )
        return ValidationPipeline(skills_dir)

    def test_run_all(self, pipeline: ValidationPipeline):
        results = pipeline.run_all()
        assert len(results) == 3
        assert "skill-a" in results
        assert "skill-b" in results
        assert "skill-c" in results

    def test_run_all_no_errors(self, pipeline: ValidationPipeline):
        results = pipeline.run_all()
        for name, res in results.items():
            errors = [r for r in res if r.severity == Severity.ERROR]
            assert len(errors) == 0, f"{name} has errors: {errors}"

    def test_report(self, pipeline: ValidationPipeline):
        results = pipeline.run_all()
        report = pipeline.report(results)
        assert report["total"] == 3
        assert report["errors"] == 0

    def test_run_ru_all(self, pipeline: ValidationPipeline, tmp_path: Path):
        ru_path = tmp_path / ".claude" / "skills" / "qa" / "skill-a" / "SKILL.ru.md"
        ru_path.write_text(
            "---\nname: skill-a\ndescription: desc-ru\ncategory: qa\ntags: [test]\nmodels: [sonnet]\nversion: 1.0.0\nlanguage: ru\n---\nContent"
        )
        results = pipeline.run_ru_all()
        assert "skill-a" in results
