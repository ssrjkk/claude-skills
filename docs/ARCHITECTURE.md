# Claude Skills Library — Architecture Guide

## Project Structure

```
claude-skills/
├── .claude/skills/          # 10,000+ skill definitions
│   ├── {domain}/
│   │   └── {skill-name}/
│   │       ├── SKILL.md     # English version
│   │       └── SKILL.ru.md  # Russian translation
├── src/
│   └── claude_skills/       # Python SDK
│       ├── __init__.py      # Public API exports
│       ├── models.py        # Data models (Skill, Catalog, etc.)
│       ├── catalog.py       # Catalog builder & loader
│       ├── validator.py     # Validation pipeline
│       ├── quality.py       # Quality scoring
│       └── cli.py           # CLI entry points
├── ts-sdk/                  # TypeScript SDK
│   └── src/
│       ├── index.ts         # Type definitions & utilities
│       └── index.test.ts    # TS tests
├── scripts/                 # CLI scripts (thin wrappers)
│   ├── validate-all.py      → claude_skills.validator
│   ├── deep-validate.py     → claude_skills.quality
│   ├── generate-catalog.py  → claude_skills.catalog
│   ├── detect_anti_patterns.py
│   ├── generate_skill.py    # Skill generator
│   ├── build_docs.py        # Doc site builder
│   └── list-skills.py
├── tests/                   # Test suite
│   ├── test_models.py       # Model unit tests
│   ├── test_catalog.py      # Catalog builder tests
│   ├── test_validator.py    # Validator tests
│   ├── test_quality.py      # Quality analyzer tests
│   ├── test_property.py     # Hypothesis property tests
│   └── conftest.py
├── docs/                    # Documentation site
├── skills_catalog.json      # Generated catalog
├── setup.py                 # Package configuration
├── Makefile                 # Cross-platform build
└── .github/workflows/       # CI/CD
```

## Data Flow

```
SKILL.md files on disk
        │
        ▼
  CatalogBuilder.scan()
        │
        ▼
  Catalog (in-memory)
        │
        ├──╴CatalogBuilder.to_json() → skills_catalog.json
        │
        ├──╴ValidationPipeline.run_all() → ValidationResult[]
        │
        └──╴QualityAnalyzer.analyze() → QualityScore[]
                │
                ▼
          QualityReport → Summary + Grades
```

## Quality Scoring

The quality score is a weighted composite of 5 dimensions:

| Dimension | Weight | Description |
|-----------|--------|-------------|
| Completeness | 25% | Section coverage (Quick Start, When to Use, etc.) |
| Depth | 25% | Content length and substance |
| Code Quality | 20% | Code examples, fences, inline code |
| Freshness | 15% | Recency of last update |
| Bilingual | 15% | Russian translation quality |
