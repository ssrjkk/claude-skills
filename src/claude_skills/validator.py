from __future__ import annotations

import re
from pathlib import Path
from typing import Optional

import yaml  # type: ignore[import-untyped]

from claude_skills.models import Severity, ValidationResult


class SkillValidator:
    REQUIRED_FIELDS = {"name", "description", "category", "tags", "models", "version"}
    VALID_CATEGORIES = {
        "ai", "ar-vr", "backend", "block", "blockchain", "ci-cd-setup", "cloud",
        "communications", "data", "database", "database-migration", "design", "desktop",
        "devops", "ecommerce", "education", "embedded", "energy", "engineering",
        "finance", "frontend", "gamedev", "geospatial", "healthcare", "hr", "iot",
        "media", "mobile", "networking", "os-admin", "payments", "product", "qa",
        "scientific", "security", "supply-chain", "sustainability", "test-reporting",
        "api-testing",
    }
    PLACEHOLDER_NAMES = re.compile(r"^(skill-\d+|.*-skill-\d+)$")
    BAD_PATTERNS = re.compile(r"\b(TODO|FIXME|HACK|XXX|UNDONE)\b")

    def validate_skill_file(self, filepath: Path) -> list[ValidationResult]:
        results: list[ValidationResult] = []
        name = filepath.parent.name
        try:
            content = filepath.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as e:
            results.append(ValidationResult(str(filepath), Severity.ERROR, "E001", f"Cannot read file: {e}"))
            return results

        if not content.startswith("---"):
            results.append(ValidationResult(str(filepath), Severity.ERROR, "E010", "Missing opening frontmatter ---"))
            return results

        frontmatter, body, parse_ok = self._parse_frontmatter(content)
        if not parse_ok:
            results.append(ValidationResult(str(filepath), Severity.ERROR, "E011", "Malformed frontmatter"))
            return results

        if not frontmatter:
            results.append(ValidationResult(str(filepath), Severity.ERROR, "E012", "Empty frontmatter"))
            return results

        results.extend(self._validate_frontmatter(filepath, frontmatter, name))
        results.extend(self._validate_body(filepath, body))

        return results

    def _validate_frontmatter(self, filepath: Path, fm: dict, expected_name: str) -> list[ValidationResult]:
        results: list[ValidationResult] = []
        missing = self.REQUIRED_FIELDS - set(fm.keys())
        if missing:
            results.append(ValidationResult(str(filepath), Severity.ERROR, "E020", f"Missing required fields: {sorted(missing)}"))

        name = fm.get("name", "")
        if name != expected_name:
            results.append(ValidationResult(str(filepath), Severity.WARNING, "W010", f'Directory name "{expected_name}" != frontmatter name "{name}"'))

        if self.PLACEHOLDER_NAMES.match(name):
            results.append(ValidationResult(str(filepath), Severity.WARNING, "W011", f"Placeholder-style name: {name}"))

        category = fm.get("category", "")
        if category and category not in self.VALID_CATEGORIES:
            results.append(ValidationResult(str(filepath), Severity.WARNING, "W012", f'Unknown category "{category}"'))

        tags = fm.get("tags", [])
        if isinstance(tags, list):
            dupes = self._find_duplicates(tags)
            if dupes:
                results.append(ValidationResult(str(filepath), Severity.WARNING, "W013", f"Duplicate tags: {dupes}"))

        version = str(fm.get("version", ""))
        if version and not re.match(r"^\d+\.\d+(\.\d+)?$", version):
            results.append(ValidationResult(str(filepath), Severity.WARNING, "W014", f"Non-standard version format: {version}"))

        models = fm.get("models", [])
        if isinstance(models, list) and len(models) == 2 and "gpt-4" in models and "claude-3" in models:
            results.append(ValidationResult(str(filepath), Severity.INFO, "I010", "Default model set [gpt-4, claude-3] - may need updating"))

        return results

    def _validate_body(self, filepath: Path, body: str) -> list[ValidationResult]:
        results: list[ValidationResult] = []
        body_stripped = body.strip()

        if len(body_stripped) < 80:
            results.append(ValidationResult(str(filepath), Severity.WARNING, "W020", f"Body too short ({len(body_stripped)} chars)"))

        if len(body_stripped) < 50:
            results.append(ValidationResult(str(filepath), Severity.WARNING, "W030", f"Body critically short ({len(body_stripped)} chars)"))

        if self.BAD_PATTERNS.search(body):
            results.append(ValidationResult(str(filepath), Severity.WARNING, "W021", "Contains TODO/FIXME placeholder"))

        required_sections = ["Quick Start", "Validation"]
        for section in required_sections:
            if section not in body:
                results.append(ValidationResult(str(filepath), Severity.INFO, "I020", f'Missing section "{section}"'))

        fence_count = body.count("```")
        if fence_count > 0 and fence_count % 2 != 0:
            results.append(ValidationResult(str(filepath), Severity.ERROR, "E040", f"Unbalanced code fences ({fence_count} fences)"))

        return results

    def _parse_frontmatter(self, content: str) -> tuple[Optional[dict], str, bool]:
        try:
            end = content.find("---", 3)
            if end < 0:
                return None, "", False
            front = content[3:end].strip()
            body = content[end + 3 :].strip()
            parsed = yaml.safe_load(front)
            return (parsed, body, True) if isinstance(parsed, dict) else (None, body, False)
        except yaml.YAMLError:
            return None, "", False

    def _find_duplicates(self, items: list) -> list:
        seen = {}
        dupes = []
        for item in items:
            key = str(item).strip().lower()
            if key in seen:
                dupes.append(str(item))
            else:
                seen[key] = True
        return list(set(dupes))


class ValidationPipeline:
    def __init__(self, skills_dir: Path):
        self.skills_dir = skills_dir
        self.validator = SkillValidator()

    def run_all(self) -> dict[str, list[ValidationResult]]:
        results: dict[str, list[ValidationResult]] = {}
        for sk_path in sorted(self.skills_dir.rglob("SKILL.md")):
            name = sk_path.parent.name
            results[name] = self.validator.validate_skill_file(sk_path)
        return results

    def run_ru_all(self) -> dict[str, list[ValidationResult]]:
        results: dict[str, list[ValidationResult]] = {}
        for sk_path in sorted(self.skills_dir.rglob("SKILL.ru.md")):
            name = sk_path.parent.name
            results[name] = self.validator.validate_skill_file(sk_path)
        return results

    def report(self, results: dict[str, list[ValidationResult]]) -> dict:
        stats = {"total": len(results), "errors": 0, "warnings": 0, "info": 0}
        all_errors: list[str] = []
        all_warnings: list[str] = []
        for skill_name, skill_results in results.items():
            for r in skill_results:
                if r.severity == Severity.ERROR:
                    stats["errors"] += 1
                    all_errors.append(str(r))
                elif r.severity == Severity.WARNING:
                    stats["warnings"] += 1
                    all_warnings.append(str(r))
                elif r.severity == Severity.INFO:
                    stats["info"] += 1
        return {**stats, "error_details": all_errors[:50], "warning_details": all_warnings[:50]}
