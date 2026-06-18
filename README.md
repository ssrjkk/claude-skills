# Claude Skills Library

> **10,000+ bilingual skills • 39 domains • English + Russian**

A community-driven collection of structured, executable skill definitions for AI coding assistants. Build smarter, faster, and more consistently with battle-tested skills.

## 🚀 Quick Start

```bash
# Install the SDK
pip install -e .

# Validate all skills
make validate

# Run quality analysis
make quality

# Regenerate catalog
make catalog
```

## 📊 Stats

| Metric | Value |
|--------|-------|
| Total English skills | **10,000** |
| Total Russian skills | **10,000** |
| Domains | **39** |
| Bilingual coverage | **100%** |
| Languages | EN (primary), RU (parallel) |
| License | MIT |

## 🏗 Structure

```
.claude/skills/{domain}/{skill-name}/
  ├── SKILL.md        # English skill definition
  └── SKILL.ru.md     # Russian translation
```

## 📚 SDK

### Python

```python
from claude_skills.catalog import CatalogBuilder
from claude_skills.validator import ValidationPipeline
from claude_skills.quality import QualityAnalyzer

# Build catalog from disk
catalog = CatalogBuilder().build_catalog()
print(f"{catalog.metadata.total_skills} skills found")

# Validate all skills
pipeline = ValidationPipeline(Path(".claude/skills"))
results = pipeline.run_all()
report = pipeline.report(results)
print(f"Errors: {report['errors']}, Warnings: {report['warnings']}")

# Quality analysis
analyzer = QualityAnalyzer()
for sk_path in Path(".claude/skills").rglob("SKILL.md"):
    score = analyzer.analyze(SkillFile(en_path=sk_path, en_body=sk_path.read_text()))
    print(f"{sk_path.parent.name}: {score.overall:.1f}% ({score.grade})")
```

### CLI

```bash
# Validate all skills
claude-skills validate

# Quality analysis
claude-skills quality --json report.json

# Build catalog
claude-skills catalog

# Statistics
claude-skills stats
```

### TypeScript

```typescript
import { Catalog, search, byCategory } from 'claude-skills';

const catalog: Catalog = await loadCatalog();
const qaSkills = byCategory(catalog.skills)['qa'];
const results = search(catalog.skills, 'kubernetes');
```

## 🧪 Validation Pipeline

```bash
# Full validation suite
make validate

# Run tests with coverage
make test

# Build catalog
make catalog

# Quality report
make quality
```

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Quick checklist:
- [ ] `SKILL.md` follows the template with frontmatter
- [ ] `SKILL.ru.md` is a real translation (not auto-generated stub)
- [ ] Code examples are valid and tested
- [ ] `/python -m pytest tests/` passes
- [ ] `ruff check src/` passes

## 📦 Domains

`ai` `ar-vr` `backend` `block` `blockchain` `ci-cd-setup` `cloud` `communications` `data` `database` `database-migration` `design` `desktop` `devops` `ecommerce` `education` `embedded` `energy` `engineering` `finance` `frontend` `gamedev` `geospatial` `healthcare` `hr` `iot` `media` `mobile` `networking` `os-admin` `payments` `product` `qa` `scientific` `security` `supply-chain` `sustainability` `test-reporting`

## 🔗 Links

- [GitHub](https://github.com/ssrjkk/claude-skills)
- [Documentation](https://ssrjkk.github.io/claude-skills/)
- [Quality Report](docs/api/quality-report.json)

## 📄 License

MIT
