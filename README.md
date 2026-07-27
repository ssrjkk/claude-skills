д<p align="center">
  <img src="https://img.shields.io/github/stars/ssrjkk/claude-skills?style=for-the-badge&color=gold" alt="Stars">
  <img src="https://img.shields.io/badge/skills-10,000+-blue?style=for-the-badge" alt="Skills">
  <img src="https://img.shields.io/badge/languages-EN%20%7C%20RU-green?style=for-the-badge" alt="Languages">
  <img src="https://img.shields.io/badge/domains-39-orange?style=for-the-badge" alt="Domains">
  <img src="https://img.shields.io/badge/license-MIT-purple?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/coverage-93%25-brightgreen?style=for-the-badge" alt="Coverage">
</p>

<h1 align="center">Claude Skills Library</h1>
<p align="center"><strong>10,000+ skills for Claude Code · 39 domains · English + Russian</strong></p>
<p align="center">Bilingual AI skills library</p>

<!--
Keywords: claude skills, claude code, ai skills, prompt engineering, claude templates, developer tools
-->

---

## Quick Start

```bash
# One-liner install
curl -fsSL https://raw.githubusercontent.com/ssrjkk/claude-skills/main/install.sh | bash

# Or via pip
pip install -e .

# Install a skill (from local repo or GitHub)
claude-skills install k8s-debugger

# Search the catalog
claude-skills search kubernetes

# Generate a new skill from a prompt
claude-skills generate "Debug PostgreSQL slow queries"

# Validate & explore
claude-skills stats          # Library statistics
claude-skills validate       # Validate all skills
claude-skills quality        # Quality analysis
```

## Why Claude Skills?

| Without skills | With skills |
|---|---|
| "Write a React component with tests" → generic output | "Write a React component with tests" → domain-optimized, production-ready code |
| You manually context-switch between 39 domains | Skills auto-load the right context for each task |
| No quality guarantees | 93% tested coverage, multi-dimensional quality scoring |
| English only | Full English + Russian parallel translations |

## Stats

| Metric | Value |
|--------|-------|
| Total skills | **10,000+** |
| Russian translations | **10,000** |
| Domains | **39** |
| Bilingual coverage | **100%** |
| Test coverage | **93%** |
| Quality grades | A–F scoring |
| Validation speed | **7.8s** for all 10K files |
| License | MIT |

## Structure

```
.claude/skills/
  {domain}/
    {skill-name}/
      ├── SKILL.md        ← English (primary)
      └── SKILL.ru.md     ← Russian (parallel)
```

## SDK

### Python

```python
from claude_skills.catalog import CatalogBuilder
from claude_skills.validator import ValidationPipeline
from claude_skills.quality import QualityAnalyzer

# Build & explore catalog
catalog = CatalogBuilder().build_catalog()
print(f"{catalog.metadata.total_skills} skills, {catalog.metadata.total_ru} RU")

# Validate all 10K skills in ~8s
pipeline = ValidationPipeline(Path(".claude/skills"))
report = pipeline.report(pipeline.run_all())
print(f"Errors: {report['errors']}, Warnings: {report['warnings']}")
```

### CLI

```bash
claude-skills install <name>           # Install a skill from catalog/GitHub
claude-skills search <query>           # Search skills by name, description, tags
claude-skills generate <prompt>        # Generate a skill via template (or --api for LLM)
claude-skills share <path>             # Share a skill (--github for issue, --text for summary)
claude-skills validate                 # Full validation pipeline
claude-skills quality --json report.json
claude-skills catalog                  # Rebuild catalog JSON
claude-skills stats                    # Library statistics
```

### TypeScript

```typescript
import { Catalog, search, byCategory } from 'claude-skills';
const catalog: Catalog = await loadCatalog();
const qaSkills = byCategory(catalog.skills)['qa'];
const results = search(catalog.skills, 'kubernetes');
```

## Quality Pipeline

Every skill is scored on 5 dimensions:

| Dimension | Weight | What it measures |
|-----------|--------|-----------------|
| Completeness | 25% | Section coverage (Quick Start, Validation, etc.) |
| Depth | 25% | Content length & substance |
| Code Quality | 20% | Working code examples |
| Freshness | 15% | Recency of last update |
| Bilingual | 15% | Russian translation quality |

**Current library score: 59.4% (Grade D)** — actively improving every week.

## Domains (39)

`ai` · `ar-vr` · `backend` · `block` · `blockchain` · `ci-cd-setup` · `cloud` · `communications` · `data` · `database` · `database-migration` · `design` · `desktop` · `devops` · `ecommerce` · `education` · `embedded` · `energy` · `engineering` · `finance` · `frontend` · `gamedev` · `geospatial` · `healthcare` · `hr` · `iot` · `media` · `mobile` · `networking` · `os-admin` · `payments` · `product` · `qa` · `scientific` · `security` · `supply-chain` · `sustainability` · `test-reporting`

## Author

**ssrjkk**

- Telegram: [@ssrjkk](https://t.me/ssrjkk)
- Email: [ray013lefe@gmail.com](mailto:ray013lefe@gmail.com)
- Twitter/X: [ssrjkk](https://twitter.com/ssrjkk)

## For Contributors

See [CONTRIBUTING.md](CONTRIBUTING.md). Quick checklist:
- [ ] `SKILL.md` has frontmatter with name, description, category, tags, models, version
- [ ] `SKILL.ru.md` is a **real translation** (not auto-generated)
- [ ] Code examples compile and run
- [ ] `make test` passes
- [ ] `ruff check src/` passes

## Product Components

| Component | Description |
|-----------|-------------|
| **Python CLI** | `claude-skills` — install, search, generate, validate, quality, catalog, stats |
| **TypeScript SDK** | `npm install claude-skills` — types + utilities for Node.js |
| **GitHub Action** | `ssrjkk/claude-skills` — validate skills in CI/CD |
| **VS Code Extension** | Browse 10K skills, one-click install from sidebar |
| **Next.js Site** | [ssrjkk.github.io/claude-skills/](https://ssrjkk.github.io/claude-skills/) — 10K+ static pages |
| **Featured Skills** | 50 curated starter skills across 15 core domains |

## Links

- [Documentation Site](https://ssrjkk.github.io/claude-skills/) — searchable catalog
- [Launch Checklist](docs/launch-checklist.md) — launch readiness
- [Launch Summary](docs/launch/launch-summary.md) — launch plan overview
- [Growth Metrics](docs/metrics.md) — tracking progress
- [Quality Report](docs/api/quality-report.json)
- [Architecture Guide](docs/ARCHITECTURE.md)
- [API Reference](docs/api/README.md)
- [Issue Tracker](https://github.com/ssrjkk/claude-skills/issues)

## Star History

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ssrjkk/claude-skills&type=Date&theme=dark" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ssrjkk/claude-skills&type=Date" />
  <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=ssrjkk/claude-skills&type=Date" />
</picture>

## License

MIT. Free for personal and commercial use.

---

<p align="center"><strong>Bilingual AI skills library.</strong>
</p>
