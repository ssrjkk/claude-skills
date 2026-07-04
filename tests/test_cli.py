"""Tests for CLI commands."""

from __future__ import annotations

from pathlib import Path

import pytest
from claude_skills.cli import (
    _detect_domain,
    _generate_skill_content,
    _generate_ru_content,
    cmd_install,
    cmd_search,
    cmd_share,
)


class TestDomainDetection:
    def test_detect_ai(self):
        assert _detect_domain("train a neural network with PyTorch") == "ai"

    def test_detect_frontend(self):
        assert _detect_domain("build a React component with TypeScript") == "frontend"

    def test_detect_devops(self):
        assert _detect_domain("deploy to Kubernetes with CI/CD") == "devops"

    def test_detect_database(self):
        assert _detect_domain("optimize PostgreSQL query performance") == "database"

    def test_detect_security(self):
        assert _detect_domain("implement OAuth and JWT authentication") == "security"

    def test_detect_backend(self):
        assert _detect_domain("create a FastAPI REST API") == "backend"

    def test_detect_qa(self):
        assert _detect_domain("write pytest unit tests") == "qa"

    def test_detect_general(self):
        assert _detect_domain("do something random") == "general"


class TestGenerateContent:
    def test_generate_basic(self):
        content = _generate_skill_content("database", "pg-slow-query", "Debug slow PostgreSQL queries")
        assert "name: pg-slow-query" in content
        assert "category: database" in content
        assert "Debug slow PostgreSQL queries" in content
        assert "Quick Start" in content
        assert "Validation" in content

    def test_generate_ru(self):
        ru = _generate_ru_content("pg-slow-query", "Debug slow PostgreSQL queries", "database")
        assert "name: pg-slow-query" in ru
        assert "language: ru" in ru
        assert "Быстрый старт" in ru

    def test_generate_unknown_domain(self):
        content = _generate_skill_content("unknown-domain", "my-skill", "A custom skill")
        assert "name: my-skill" in content
        assert "category: unknown-domain" in content


class TestCmdInstall:
    def test_install_local_skill(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
        import os
        orig_dir = Path.cwd()
        os.chdir(tmp_path)
        try:
            src_dir = tmp_path / ".claude" / "skills" / "qa" / "test-skill"
            src_dir.mkdir(parents=True)
            (src_dir / "SKILL.md").write_text(
                "---\nname: test-skill\ndescription: Test\ncategory: qa\ntags: []\nmodels: []\nversion: 1.0.0\n---\nContent"
            )
            (src_dir / "SKILL.ru.md").write_text("---\nname: test-skill\ndescription: Test\ncategory: qa\ntags: []\nmodels: []\nversion: 1.0.0\n---\nRU Content")

            import argparse
            target = tmp_path / "target"
            args = argparse.Namespace(skill="test-skill", dir=str(target), catalog=None)
            result = cmd_install(args)
            assert result == 0
            assert (target / "qa" / "test-skill" / "SKILL.md").exists()
            assert (target / "qa" / "test-skill" / "SKILL.ru.md").exists()
            assert (target / "qa" / "test-skill" / "SKILL.md").read_text() == "---\nname: test-skill\ndescription: Test\ncategory: qa\ntags: []\nmodels: []\nversion: 1.0.0\n---\nContent"
        finally:
            os.chdir(orig_dir)

    def test_install_not_found(self, tmp_path: Path):
        import argparse
        target = tmp_path / "target"
        target.mkdir()
        args = argparse.Namespace(skill="nonexistent-skill", dir=str(target), catalog=None)
        result = cmd_install(args)
        assert result == 1


class TestCmdSearch:
    def test_search_basic(self, tmp_path: Path):
        import os
        orig_dir = Path.cwd()
        os.chdir(tmp_path)
        try:
            catalog_dir = tmp_path / ".claude" / "skills"
            skill_dir = catalog_dir / "qa" / "my-tester"
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(
                "---\nname: my-tester\ndescription: A testing skill\ncategory: qa\ntags: [testing, automation]\nmodels: [sonnet]\nversion: 1.0.0\n---\nContent"
            )
            import argparse
            args = argparse.Namespace(query="tester", category=None, tag=None, limit=10, json=False)
            result = cmd_search(args)
            assert result == 0
        finally:
            os.chdir(orig_dir)

    def test_search_no_catalog(self, tmp_path: Path):
        import os
        import argparse
        orig_dir = Path.cwd()
        os.chdir(tmp_path)
        try:
            args = argparse.Namespace(query="zzzznotfound", category=None, tag=None, limit=10, json=False)
            result = cmd_search(args)
            assert result == 1
        finally:
            os.chdir(orig_dir)


class TestCmdShare:
    def test_share_text(self, tmp_path: Path):
        skill_dir = tmp_path / "test-skill"
        skill_dir.mkdir()
        (skill_dir / "SKILL.md").write_text(
            "---\nname: test-skill\ndescription: A test\ncategory: qa\ntags: []\nmodels: []\nversion: 1.0.0\n---\n# Test Skill\n\nContent here"
        )
        import argparse
        args = argparse.Namespace(skill=str(skill_dir), github=False, text=True)
        result = cmd_share(args)
        assert result == 0

    def test_share_github(self, tmp_path: Path):
        skill_dir = tmp_path / "test-skill"
        skill_dir.mkdir()
        (skill_dir / "SKILL.md").write_text(
            "---\nname: test-skill\ndescription: A test\ncategory: qa\ntags: []\nmodels: []\nversion: 1.0.0\n---\nContent"
        )
        import argparse
        args = argparse.Namespace(skill=str(skill_dir), github=True, text=False)
        result = cmd_share(args)
        assert result == 0

    def test_share_not_found(self, tmp_path: Path):
        import argparse
        args = argparse.Namespace(skill=str(tmp_path / "nonexistent"), github=False, text=False)
        result = cmd_share(args)
        assert result == 1


class TestImport:
    def test_cli_import(self):
        from claude_skills.cli import main
        assert main is not None

    def test_cli_help(self):
        import subprocess
        import sys
        result = subprocess.run(
            [sys.executable, "-m", "claude_skills.cli", "--help"],
            capture_output=True, text=True
        )
        assert result.returncode == 0
        assert "install" in result.stdout
        assert "search" in result.stdout
        assert "generate" in result.stdout
        assert "share" in result.stdout
        assert "validate" in result.stdout
