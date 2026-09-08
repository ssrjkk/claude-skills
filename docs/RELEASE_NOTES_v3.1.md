# Release Notes - v3.1

## Highlights

- **21/21 skills at 100.0% quality (Grade A)** across all five dimensions:
  completeness, depth, code quality, freshness, bilingual.
- **Universal Agent Skills format** — every skill is portable to Claude Code,
  OpenCode, Cursor and Windsurf. New CI check (`scripts/check_agent_interop.py`)
  enforces cross-agent invariants: kebab-case `name` matching the directory,
  single-line `description` ≤1024 chars, no duplicate names.
- **100% test coverage** (133 tests) with zero missed statements.
- **Codebase refactor**:
  - Shared `parse_frontmatter` in `models.py` (LF/CRLF, malformed YAML,
    missing/empty frontmatter, non-dict payloads) reused by validator, catalog
    and CLI — duplicate logic removed.
  - CLI bug fixes: `stats` now respects `--dir` and writes `--json`; `search`
    gained `--dir`; `catalog` gained `--dir`/`--output`; `validate` checks RU
    in addition to EN.
  - Quality scorer: dead code removed, `SECTION_VARIANTS`, fixed `datetime.date`
    freshness handling (previously a date object fell back to a flat 30).
- All 21 skills gained honest, skill-specific `Troubleshooting` sections
  (EN + RU) to reach full depth scoring.

## Quality Report

```
21/21 skills at 100.0% (A)
Grade A:  21/21
Bilingual coverage: 21/21 (100%)
Average score: 100.0
```

## Validation

- 133 tests pass; `ruff` clean; `mypy` clean (src + tests).
- Catalog: 21 skills, 11 domains, 21 Russian translations, regenerated from
  source with anti-pattern detection passing.