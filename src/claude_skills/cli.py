"""CLI entry point for claude-skills.

Thin re-export — all command logic lives in claude_skills.commands.*
"""

from __future__ import annotations

import argparse
import sys

from claude_skills.commands.catalog import cmd_catalog, cmd_stats
from claude_skills.commands.generate import (
    _detect_domain,
    _generate_ru_content,
    _generate_skill_content,
    cmd_generate,
)
from claude_skills.commands.install import _fix_encoding, cmd_install
from claude_skills.commands.quality import cmd_quality
from claude_skills.commands.search import cmd_search
from claude_skills.commands.share import cmd_share
from claude_skills.commands.validate import cmd_validate

__all__ = [
    "cmd_catalog",
    "cmd_generate",
    "cmd_install",
    "cmd_quality",
    "cmd_search",
    "cmd_share",
    "cmd_stats",
    "cmd_validate",
    "main",
    "_detect_domain",
    "_generate_ru_content",
    "_generate_skill_content",
]


def main() -> int:
    _fix_encoding()
    parser = argparse.ArgumentParser(
        description="Claude Skills SDK — install, search, generate, and share Claude Code skills",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  claude-skills install k8s-debugger\n"
            "  claude-skills search kubernetes\n"
            "  claude-skills generate \"Debug PostgreSQL slow queries\" --domain database\n"
            "  claude-skills validate --dir .claude/skills\n"
            "  claude-skills share my-skill --github\n"
        ),
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_install = sub.add_parser("install", help="Install a skill from the catalog")
    p_install.add_argument("skill", help="Skill name to install (e.g., k8s-debugger)")
    p_install.add_argument("--dir", default=".claude/skills", help="Target skills directory (default: .claude/skills)")
    p_install.add_argument("--catalog", help="Path to catalog JSON (auto-detected if omitted)")
    p_install.set_defaults(func=cmd_install)

    p_search = sub.add_parser("search", help="Search skills in the catalog")
    p_search.add_argument("query", help="Search query")
    p_search.add_argument("--category", help="Filter by category")
    p_search.add_argument("--tag", help="Filter by tag")
    p_search.add_argument("--limit", type=int, default=20, help="Max results (default: 20)")
    p_search.add_argument("--json", action="store_true", help="Output as JSON")
    p_search.set_defaults(func=cmd_search)

    p_generate = sub.add_parser("generate", help="Generate a new skill via template or LLM")
    p_generate.add_argument("prompt", help="Description of the skill to generate")
    p_generate.add_argument("--domain", help="Domain/category (auto-detected from prompt if omitted)")
    p_generate.add_argument("--name", help="Skill name in kebab-case (auto-generated from prompt if omitted)")
    p_generate.add_argument("--dir", default=".claude/skills", help="Output directory (default: .claude/skills)")
    p_generate.add_argument("--api", action="store_true", help="Use Claude API for generation (requires ANTHROPIC_API_KEY)")
    p_generate.set_defaults(func=cmd_generate)

    p_share = sub.add_parser("share", help="Share a skill (format for GitHub issue or text output)")
    p_share.add_argument("skill", help="Path to skill directory or SKILL.md file")
    p_share.add_argument("--github", action="store_true", help="Generate GitHub issue link")
    p_share.add_argument("--text", action="store_true", help="Output formatted text summary")
    p_share.set_defaults(func=cmd_share)

    p_validate = sub.add_parser("validate", help="Validate all skills")
    p_validate.add_argument("--dir", default=".claude/skills", help="Skills directory")
    p_validate.add_argument("--strict", action="store_true", help="Fail CI on warnings, not just critical errors")
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
