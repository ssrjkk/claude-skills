# Contributing to Claude Skills Library

## How to Contribute

### Adding a New Skill

1. Choose the appropriate domain from the 39 available categories
2. Create a directory: `.claude/skills/{domain}/{skill-name}/`
3. Create `SKILL.md` with proper frontmatter:

```markdown
---
name: your-skill-name
description: Clear, one-line description of what this skill does
category: domain-name
tags: [your-skill, domain, relevant-tags]
models: [sonnet, opus]
version: 1.0.0
language: en
created: 2026-06-19
---

# Your Skill Name

> One-paragraph description

## Quick Start
Getting started instructions...

## When to Use
- Use case 1
- Use case 2

## Step-by-Step
1. Step one
2. Step two

## Dependencies
- Required tools/libraries

## Examples
```python
# Working code example
```

## Resources
- Links to docs

## Validation
- How to verify the skill works
```

4. Create `SKILL.ru.md` with a real Russian translation (not auto-generated)
5. Run `make validate` to verify
6. Run `make test` to ensure tests pass

### Quality Standards

- **Body length**: At least 500 characters of real content
- **Code examples**: Working, tested code in appropriate language
- **Sections**: All required sections present (Quick Start, When to Use, Step-by-Step, Validation)
- **Translations**: Real, human-quality Russian translations
- **No placeholders**: No `TODO`, `FIXME`, or stub content

### Validation

```bash
# Full validation
make validate

# Run tests
make test

# Quality report
make quality

# Lint check
ruff check src/
```

### Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Add/improve skills
4. Run validation pipeline
5. Submit PR with description of changes

### Code of Conduct

Be respectful, inclusive, and constructive. All contributions are welcome.
