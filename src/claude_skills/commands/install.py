from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Optional
import argparse

from claude_skills.catalog import CatalogBuilder

REPO = "ssrjkk/claude-skills"
BRANCH = "main"
GITHUB_RAW = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}"
GITHUB_API = f"https://api.github.com/repos/{REPO}"


def _fix_encoding():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, LookupError):
        pass


def _get_skills_base() -> Path:
    for path in [Path(".claude/skills"), Path("../.claude/skills")]:
        if path.exists():
            return path.resolve()
    return Path(".claude/skills")


def _github_get(path: str) -> Optional[str]:
    url = f"{GITHUB_RAW}/{path.lstrip('/')}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "claude-skills-cli"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read().decode("utf-8")
    except (urllib.error.HTTPError, urllib.error.URLError, OSError):
        return None


def _fetch_skill_from_github(name: str) -> Optional[dict]:
    url = f"{GITHUB_API}/contents/.claude/skills"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "claude-skills-cli", "Accept": "application/vnd.github.v3+json"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            categories = json.loads(resp.read().decode("utf-8"))
    except (urllib.error.HTTPError, urllib.error.URLError, OSError, json.JSONDecodeError):
        return None

    for cat in categories:
        if cat["type"] != "dir":
            continue
        cat_name = cat["name"]
        skill_url = f"{GITHUB_API}/contents/.claude/skills/{cat_name}/{name}"
        try:
            req = urllib.request.Request(skill_url, headers={"User-Agent": "claude-skills-cli", "Accept": "application/vnd.github.v3+json"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                files = json.loads(resp.read().decode("utf-8"))
                has_sk = any(f["name"] == "SKILL.md" for f in files if f["type"] == "file")
                if has_sk:
                    en = None
                    ru = None
                    for f in files:
                        if f["name"] == "SKILL.md":
                            en = _github_get(f"claude/skills/{cat_name}/{name}/SKILL.md")
                        elif f["name"] == "SKILL.ru.md":
                            ru = _github_get(f"claude/skills/{cat_name}/{name}/SKILL.ru.md")
                    return {"category": cat_name, "name": name, "en": en, "ru": ru}
        except urllib.error.HTTPError:
            continue
    return None


def cmd_install(args: argparse.Namespace) -> int:
    skill_name = args.skill
    target_dir = Path(args.dir)
    target_dir.mkdir(parents=True, exist_ok=True)

    skills_base = _get_skills_base()

    found: Optional[dict] = None

    if skills_base.exists():
        for domain_dir in sorted(skills_base.iterdir()):
            if not domain_dir.is_dir():
                continue
            skill_dir = domain_dir / skill_name
            if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                found = {"category": domain_dir.name, "name": skill_name, "en": (skill_dir / "SKILL.md").read_text(encoding="utf-8")}
                ru_path = skill_dir / "SKILL.ru.md"
                if ru_path.exists():
                    found["ru"] = ru_path.read_text(encoding="utf-8")
                break

    if not found and args.catalog:
        cat_path = Path(args.catalog)
        if cat_path.exists():
            catalog = CatalogBuilder.from_json(cat_path)
            skill_meta = catalog.get(skill_name)
            if skill_meta:
                src = Path(skill_meta.path)
                if src.exists():
                    found = {"category": skill_meta.category, "name": skill_name, "en": src.read_text(encoding="utf-8")}
                    ru_path = src.parent / "SKILL.ru.md"
                    if ru_path.exists():
                        found["ru"] = ru_path.read_text(encoding="utf-8")

    if not found:
        print(f"Searching GitHub for '{skill_name}'...", file=sys.stderr)
        found = _fetch_skill_from_github(skill_name)

    if not found:
        print(f"Error: skill '{skill_name}' not found", file=sys.stderr)
        return 1

    category = found["category"]
    target = target_dir / category / skill_name
    target.mkdir(parents=True, exist_ok=True)

    (target / "SKILL.md").write_text(found["en"], encoding="utf-8")
    if found.get("ru"):
        (target / "SKILL.ru.md").write_text(found["ru"], encoding="utf-8")

    print(f"Installed '{skill_name}' ({category}) to {target}")
    return 0
