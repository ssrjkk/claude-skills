// GitHub Copilot custom instructions for Skills Library
// This file configures Copilot behavior for this repository

// Every skill uses the universal Agent Skills format (SKILL.md), shared by
// Claude Code, OpenCode, Cursor, Windsurf and other agents. Keep skills
// portable so they work in ALL agents, not just Claude.

// When suggesting skills, always follow the standard template:
// 1. YAML frontmatter (name, description, category, tags, models, version)
// 2. Quick Start section with code
// 3. When to Use section
// 4. Step-by-Step section
// 5. Dependencies section
// 6. Examples section
// 7. Resources section
// 8. Validation section

// Portable frontmatter requirements (enforced by scripts/check_agent_interop.py):
// - name: lowercase, hyphen-separated, matches the skill directory name
// - description: single line, <=1024 characters
// name + description are mandatory; other fields are optional metadata

// Category naming convention: lowercase, single word (ai, backend, frontend, etc.)
// Skill naming convention: lowercase, hyphen-separated (my-skill-name)
// All skills go under .claude/skills/{category}/{skill-name}/SKILL.md
// Russian translations live next to the primary file as SKILL.ru.md