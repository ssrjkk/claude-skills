# Claude Skills Library

> **Bilingual Claude Skills — 10,000 EN + 10,000 RU across 39 domains**

A community-driven collection of structured, executable skill definitions for Claude AI. Each skill has parallel English (`SKILL.md`) and Russian (`SKILL.ru.md`) translations with YAML frontmatter, ready-to-use code, and validation steps.

## Stats

| Metric | Value |
|--------|-------|
| **English skills** | 10,000 |
| **Russian skills** | 10,000 |
| **Domains** | 39 |
| **Languages** | EN (primary), RU (parallel) |
| **License** | MIT |

Browse skills: [GitHub Pages](https://ssrjkk.github.io/claude-skills/)

## Structure

```
.claude/skills/{category}/{skill-name}/SKILL.md
```

Example: `.claude/skills/ai/accelerate-checkpointing/SKILL.md`

## Quick Start

```bash
# Validate all skills
python scripts/validate-all.py

# Deep validation (sections, code fences, frontmatter)
python scripts/deep-validate.py

# Regenerate catalog from disk
python scripts/generate-catalog.py

# List all skills
python scripts/list-skills.py
```

## Validation Pipeline

| Check | Script | When |
|-------|--------|------|
| Frontmatter completeness | `validate-all.py` | Every PR |
| Deep structure (sections, fences) | `deep-validate.py` | Every PR |
| Path consistency | `generate-catalog.py` | On push |
| Anti-pattern detection | `detect_anti_patterns.py` | On push |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Quick checklist:
- [ ] SKILL.md follows the template
- [ ] Frontmatter has: name, description, category, tags, models, version
- [ ] Code examples are valid
- [ ] `python scripts/validate-all.py` passes
- [ ] `python scripts/deep-validate.py` passes

## Domains

`ai` `ar-vr` `backend` `block` `blockchain` `communications` `data` `database`
`design` `desktop` `devops` `ecommerce` `education` `embedded` `energy`
`engineering` `finance` `frontend` `gamedev` `geospatial` `healthcare` `hr`
`iot` `media` `mobile` `networking` `os-admin` `payments` `product` `qa`
`scientific` `security` `supply-chain` `sustainability`

## License

MIT
