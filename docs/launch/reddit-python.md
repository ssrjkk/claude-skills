# r/Python Post

## Title
Claude Skills SDK — validate and score 10K+ AI prompts with Python

## Body

I built a Python SDK (`claude-skills`) for managing 10,000+ structured AI skills. It includes validation, quality scoring, catalog generation, and anti-pattern detection.

**Quick install:**
```bash
pip install claude-skills
# Or with dev tools:
pip install "claude-skills[dev]"
```

**What you can do:**

```python
# Load and explore the catalog
from claude_skills import CatalogBuilder
catalog = CatalogBuilder.from_json("skills_catalog.json")
print(f"{catalog.metadata.total_skills} skills in {len(catalog.metadata.domains)} domains")

# Query skills
backend = catalog.by_category("backend")
docker_skills = catalog.by_tag("docker")

# Validate your own skills
from claude_skills import ValidationPipeline
pipeline = ValidationPipeline()
results = pipeline.validate_all()  # 10K files in 7.8s
```

**From CLI:**
```bash
# Search
claude-skills search docker

# Install a skill
claude-skills install kubernetes-deployment

# Validate all skills
claude-skills validate --dir .claude/skills

# Quality report
claude-skills quality --dir .claude/skills

# Generate a new skill
claude-skills generate "Debug PostgreSQL slow queries"

# Catalog stats
claude-skills stats
```

**Quality scoring:** 5 dimensions (completeness, depth, code quality, freshness, bilingual) → overall A–F grade.

**Tech stack:** Python, PyYAML, colorama, pytest, hypothesis, mypy, ruff  
**Coverage:** 93% (82 tests)  
**License:** MIT

**Repo:** https://github.com/ssrjkk/claude-skills  
**Docs:** https://ssrjkk.github.io/claude-skills/
