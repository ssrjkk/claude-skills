# r/programming Post

## Title
Open source library of 10,000+ structured AI prompts across 39 domains

## Body

I created an open source library of 10,000+ structured skill definitions for AI coding assistants (Claude Code).

**The problem this solves:**
AI coding assistants give generic output because they lack context. Every time you ask them to "write tests" or "set up CI/CD" you get output that needs heavy editing. Structured skills fix this by providing domain-specific context, code examples, validation criteria, and best practices in a machine-readable format.

**Technical details:**
- Each skill is a markdown file with YAML frontmatter (name, description, category, tags, models, version)
- Skills are organized as: `.claude/skills/{domain}/{skill-name}/SKILL.md`
- Python SDK with: validation pipeline (7.8s for 10K files), quality scoring (A–F), anti-pattern detection
- TypeScript SDK also available
- Quality assurance: 93% test coverage, 82 tests, property-based testing with Hypothesis
- Bilingual: every skill has English + Russian versions

**Domains covered:** API testing, Backend, Frontend, DevOps, Security, AI/ML, Mobile, Database, Database migration, Testing/reporting, CI/CD, Architecture, Design, CLI, Performance, and 24 more.

**Stack:** Python, TypeScript, PyYAML, GitHub Actions (CI/CD), Next.js (docs site), pytest, hypothesis, ruff, mypy

**Links:**
GitHub: https://github.com/ssrjkk/claude-skills
Docs & live search: https://ssrjkk.github.io/claude-skills/

Would love contributions — especially new domains and skill improvements.
