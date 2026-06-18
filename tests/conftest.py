"""Test configuration and fixtures."""

from __future__ import annotations

from pathlib import Path

import pytest


@pytest.fixture
def sample_skill_content() -> str:
    return (
        "---\n"
        "name: test-skill\n"
        "description: A sample skill for testing\n"
        "category: qa\n"
        "tags: [testing, automation]\n"
        "models: [sonnet, opus]\n"
        "version: 1.0.0\n"
        "created: 2026-06-01\n"
        "language: en\n"
        "---\n"
        "# Test Skill\n\n"
        "## 🚀 Quick Start\n"
        "This is a test skill for unit testing.\n\n"
        "## 📋 When to Use\n"
        "- Testing validation logic\n"
        "- Verifying quality scoring\n\n"
        "## 🔧 Step-by-Step\n"
        "1. Create the test file\n"
        "2. Run the validator\n"
        "3. Check the results\n\n"
        "## 🧪 Examples\n"
        "```python\n"
        "def test_example():\n"
        '    assert "hello" == "hello"\n'
        "```\n\n"
        "## ✅ Validation\n"
        "- Test passes\n"
        "- Coverage is good\n"
    )


@pytest.fixture
def sample_ru_content() -> str:
    return (
        "---\n"
        "name: test-skill\n"
        "description: Тестовый навык\n"
        "category: qa\n"
        "tags: [testing, russian]\n"
        "models: [sonnet, opus]\n"
        "version: 1.0.0\n"
        "language: ru\n"
        "original: test-skill\n"
        "---\n"
        "# Тестовый навык\n\n"
        "## Быстрый старт\n"
        "Тестовый навык для unit-тестов.\n\n"
        "## Валидация\n"
        "Все тесты пройдены.\n"
    )


@pytest.fixture
def tmp_skill_dir(tmp_path: Path, sample_skill_content: str, sample_ru_content: str) -> Path:
    skill_dir = tmp_path / ".claude" / "skills" / "qa" / "test-skill"
    skill_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(sample_skill_content, encoding="utf-8")
    (skill_dir / "SKILL.ru.md").write_text(sample_ru_content, encoding="utf-8")
    return tmp_path


@pytest.fixture
def minimal_catalog_json(tmp_path: Path) -> Path:
    data = {
        "metadata": {
            "schema_version": "3.0",
            "generated_at": "2026-06-19T00:00:00Z",
            "total_skills": 2,
            "total_ru": 1,
            "domains": ["ai", "qa"],
            "bilingual": True,
        },
        "skills": [
            {
                "name": "skill-one",
                "description": "First skill",
                "category": "qa",
                "tags": ["testing"],
                "models": ["sonnet"],
                "version": "1.0.0",
                "path": ".claude/skills/qa/skill-one/SKILL.md",
                "languages": ["en"],
                "has_ru": False,
                "created": "2026-01-01",
                "updated": "",
            },
            {
                "name": "skill-two",
                "description": "Second skill",
                "category": "ai",
                "tags": ["ml"],
                "models": ["opus"],
                "version": "2.0.0",
                "path": ".claude/skills/ai/skill-two/SKILL.md",
                "languages": ["en", "ru"],
                "has_ru": True,
                "created": "2026-05-01",
                "updated": "",
            },
        ],
    }
    path = tmp_path / "catalog.json"
    import json
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return path
