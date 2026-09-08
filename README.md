<p align="center">
  <img src="https://img.shields.io/badge/skills-21-blue?style=for-the-badge" alt="Skills">
  <img src="https://img.shields.io/badge/languages-EN%20%7C%20RU-green?style=for-the-badge" alt="Languages">
  <img src="https://img.shields.io/badge/domains-11-orange?style=for-the-badge" alt="Domains">
  <img src="https://img.shields.io/badge/quality-A%20(100%25)-brightgreen?style=for-the-badge" alt="Quality">
  <img src="https://img.shields.io/badge/coverage-100%25-brightgreen?style=for-the-badge" alt="Coverage">
  <img src="https://img.shields.io/badge/agents-universal-purple?style=for-the-badge" alt="Agent-agnostic">
</p>

<h1 align="center">Skills Library</h1>
<p align="center"><strong>Curated bilingual (EN + RU) skills in the universal Agent Skills format</strong></p>
<p align="center">Works with Claude Code, OpenCode, Cursor, Windsurf and every Agent Skills-compatible tool</p>

---

## What is this?

21 production-grade, bilingual (English + Russian) skills following the
**universal Agent Skills format** — the `SKILL.md` convention shared by Claude
Code, OpenCode, Cursor, Windsurf and other agents. Each skill is a folder with
a `SKILL.md` (primary, English) and an optional `SKILL.ru.md` (parallel
Russian translation). Any agent that implements the Agent Skills spec can
consume them directly.

The library ships with a Python SDK + CLI for validation, quality scoring,
cataloging and search, all enforced in CI.

## Quick Start

```bash
# Install (editable)
pip install -e .

# Explore the library
claude-skills stats          # Library statistics
claude-skills search <query> # Search skills
claude-skills validate       # Validate all skills (EN + RU)
claude-skills quality        # Quality analysis
claude-skills catalog        # Rebuild skills_catalog.json
```

## Using the skills with your agent

Every skill is a standard Agent Skills directory:

```
.claude/skills/
  {domain}/
    {skill-name}/
      SKILL.md        <- English (primary)
      SKILL.ru.md     <- Russian (parallel)
```

To install a skill into another agent, point it at the same folder — the file
format is identical, only the root directory changes:

| Agent      | Default skills root     | Notes |
|------------|-------------------------|-------|
| Claude Code | `.claude/skills/`       | Native |
| OpenCode   | `.opencode/skills/`     | Same `SKILL.md` format |
| Cursor     | `.cursor/skills/`       | Same `SKILL.md` format |
| Windsurf   | `.windsurf/skills/`     | Same `SKILL.md` format |

Frontmatter is strictly validated for cross-agent portability in CI
(`scripts/check_agent_interop.py`): portable `name`, single-line
`description`, no duplicate names.

## Stats

| Metric | Value |
|--------|-------|
| Total skills | **21** |
| Russian translations | **21 (100%)** |
| Domains | **11** |
| Quality score | **100% (Grade A)** |
| Test coverage | **100%** |
| License | MIT |

Only skills meeting the quality bar (Grade A, no validation errors) are kept
in `main`. Everything else is archived under the `v1.0-legacy` tag.

## Skills by domain

| Domain | Skill | Description |
|--------|-------|-------------|
| `ai` | `few-shot-learning` | Few-shot prompt design with example selection |
| `ai` | `llm-finetuning` | Fine-tuning LLMs end-to-end |
| `backend` | `deno-runtime` | Deno realtime apps & Workers |
| `backend` | `nestjs` | NestJS modular backends |
| `backend` | `rust-tokio` | Async Rust with Tokio |
| `blockchain` | `zk-proofs` | Zero-knowledge proofs |
| `database` | `prisma-orm` | Prisma ORM data layer |
| `desktop` | `electron` | Electron cross-platform apps |
| `devops` | `aws-lambda` | Serverless on AWS Lambda |
| `devops` | `cloud-native-ai` | Cloud-native AI platforms |
| `devops` | `gitlab-ci` | GitLab CI/CD pipelines |
| `devops` | `observability-llm` | LLM observability |
| `devops` | `platform-engineering` | Internal developer platforms |
| `devops` | `serverless-ai` | Serverless AI workloads |
| `devops` | `sre-slos` | SLOs & reliability |
| `embedded` | `rust-embedded` | Embedded Rust |
| `engineering` | `ai-testing` | AI/LLM testing |
| `frontend` | `bun-runtime` | Bun runtime & tooling |
| `frontend` | `tailwind-v4` | Tailwind CSS v4 |
| `mobile` | `expo-rn` | Expo & React Native |
| `security` | `oauth2-jwt` | OAuth 2.0 & JWT |

## SDK

### Python

```python
from claude_skills.catalog import CatalogBuilder
from claude_skills.validator import ValidationPipeline
from claude_skills.quality import QualityAnalyzer

catalog = CatalogBuilder().build_catalog()
print(f"{catalog.metadata.total_skills} skills, {catalog.metadata.total_ru} RU")

pipeline = ValidationPipeline(Path(".claude/skills"))
report = pipeline.report(pipeline.run_all())
print(f"Errors: {report['errors']}, Warnings: {report['warnings']}")
```

### CLI

Commands: `stats`, `search`, `validate`, `quality`, `catalog`.

```bash
claude-skills search <query>      # Search by name, description, tags
claude-skills validate --json out.json
claude-skills quality --json out.json
claude-skills catalog             # Rebuild catalog JSON
claude-skills stats               # Library statistics
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

## Domains (11)

`ai` · `backend` · `blockchain` · `database` · `desktop` · `devops` ·
`embedded` · `engineering` · `frontend` · `mobile` · `security`

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
- [ ] `SKILL.md` passes `scripts/check_agent_interop.py` (portable to all agents)
- [ ] `make test` passes
- [ ] `make lint` passes

## Links

- [Architecture Guide](docs/ARCHITECTURE.md)
- [Release Notes](docs/RELEASE_NOTES_v3.1.md)
- [Issue Tracker](https://github.com/ssrjkk/claude-skills/issues)

## Legacy Version

Version 2.0 is a complete rewrite focused on quality — 21 carefully curated,
bilingual, Grade A skills with a validated SDK instead of thousands of
auto-generated ones.

The original v1.0 library (10,000+ auto-generated skills) is archived under
the `v1.0-legacy` tag:

```bash
git checkout v1.0-legacy
```

## License

MIT.