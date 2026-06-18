# Claude Skills Library — API Reference

## `claude_skills.models`

### `Skill`
Core skill data model.

| Field | Type | Description |
|-------|------|-------------|
| `name` | `str` | Unique skill identifier (kebab-case) |
| `description` | `str` | One-line description |
| `category` | `str` | Domain category |
| `tags` | `list[str]` | Searchable tags |
| `models` | `list[str]` | Compatible AI models |
| `version` | `str` | Semantic version |
| `path` | `Path` | Filesystem path to SKILL.md |
| `languages` | `list[str]` | Available languages |
| `has_ru` | `bool` | Russian translation exists |
| `created` | `Optional[str]` | ISO 8601 creation date |
| `updated` | `Optional[str]` | ISO 8601 last update |
| `quality` | `Optional[QualityScore]` | Computed quality score |
| `validation_results` | `list[ValidationResult]` | Validation issues |

### `Catalog`
Full catalog container.

| Property | Type | Description |
|----------|------|-------------|
| `metadata` | `CatalogMetadata` | Catalog-level metadata |
| `skills` | `list[Skill]` | All skills |
| `by_category` | `dict[str, list[Skill]]` | Grouped by category |
| `by_tag` | `dict[str, list[Skill]]` | Grouped by tag |
| `get(name)` | `Optional[Skill]` | Lookup by name |

### `QualityScore`
Multi-dimensional quality assessment.

| Field | Type | Description |
|-------|------|-------------|
| `completeness` | `float` | 0-100: Section coverage |
| `depth` | `float` | 0-100: Content length/depth |
| `code_quality` | `float` | 0-100: Code example quality |
| `freshness` | `float` | 0-100: Content recency |
| `bilingual` | `float` | 0-100: Translation quality |
| `overall` | `float` | Weighted composite (0-100) |
| `grade` | `str` | A-F letter grade |

### `ValidationResult`
Single validation finding.

| Field | Type | Description |
|-------|------|-------------|
| `skill_path` | `str` | Path to skill file |
| `severity` | `Severity` | error/warning/info |
| `code` | `str` | Error code (E001, W010, etc.) |
| `message` | `str` | Human-readable description |
| `line` | `Optional[int]` | Line number (if applicable) |

## `claude_skills.catalog`

### `CatalogBuilder`
Scan filesystem and build catalog.

```python
builder = CatalogBuilder(root=Path("."))
catalog = builder.build_catalog()
builder.to_json(catalog, path=Path("catalog.json"))

# Load from JSON
catalog = CatalogBuilder.from_json(Path("catalog.json"))
```

## `claude_skills.validator`

### `SkillValidator`
Validate individual skill files.

```python
validator = SkillValidator()
results = validator.validate_skill_file(Path("SKILL.md"))
```

### `ValidationPipeline`
Batch validation across all skills.

```python
pipeline = ValidationPipeline(Path(".claude/skills"))
results = pipeline.run_all()
report = pipeline.report(results)
```

## `claude_skills.quality`

### `QualityAnalyzer`
Compute quality scores for skills.

```python
analyzer = QualityAnalyzer()
score = analyzer.analyze(skill_file)
```

### `QualityReport`
Aggregate quality reporting.

```python
report = QualityReport(scores)
print(report.summary())
print(report.grade_distribution)
print(report.top_skills(10))
```

## CLI Usage

```bash
# Validate all skills
claude-skills validate --dir .claude/skills

# Quality analysis with JSON output
claude-skills quality --dir .claude/skills --json report.json

# Build catalog
claude-skills catalog --output skills_catalog.json

# Statistics
claude-skills stats --output stats.json
```
