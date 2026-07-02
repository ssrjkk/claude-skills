# Contributing to Claude Skills Library

First off, thanks for taking the time to contribute! 

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
 - [Report a Bug](#report-a-bug)
 - [Request a Skill](#request-a-skill)
 - [Submit a Skill](#submit-a-skill)
 - [Improve Documentation](#improve-documentation)
- [Skill Development Guide](#skill-development-guide)
 - [Skill Structure](#skill-structure)
 - [Skill Template](#skill-template)
 - [Naming Conventions](#naming-conventions)
 - [Validation](#validation)
- [Adding a New Domain](#adding-a-new-domain)
- [Pull Request Process](#pull-request-process)
- [Style Guides](#style-guides)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Report a Bug

If you find a skill that doesn't work correctly, open a [Bug Report](https://github.com/ssrjkk/claude-skills/issues/new?template=bug_report.md) with:
- The skill name and domain
- What you expected vs what happened
- The prompt you used

### Request a Skill

Missing a skill? Open a [Skill Request](https://github.com/ssrjkk/claude-skills/issues/new?template=skill_request.md) with:
- Skill name and domain
- Description of what it should do
- Example use case

### Submit a Skill

1. Fork the repo
2. Create your skill following the [template](#skill-template)
3. Run validation
4. Open a PR

### Improve Documentation

Found a typo? Unclear instructions? PRs for README, docs, and comments are always welcome.

## Skill Development Guide

### Skill Structure

Each skill lives in its own directory:

```
.claude/skills/{domain}/{skill-name}/
├── SKILL.md # Main skill file (required)
├── examples.md # Usage examples (optional)
├── reference.md # Reference docs (optional)
└── scripts/ # Helper scripts (optional)
```

### Skill Template

Every `SKILL.md` must start with YAML frontmatter:

```yaml
---
name: skill-name
description: Brief description of what this skill does
category: domain-name
tags: [tag1, tag2, tag3]
models: [claude-sonnet-4-20250514]
version: "1.0"
---
```

Followed by the skill content in markdown. Keep it:
- **Concise** — Claude has a context window, use it wisely
- **Actionable** — Step-by-step instructions
- **Complete** — Include examples and edge cases

### Naming Conventions

- Skill names: `kebab-case` (e.g., `python-fastapi`)
- Max 64 characters
- Domain names: `kebab-case` (e.g., `supply-chain`, `os-admin`)

### Validation

Always validate before submitting:

```bash
# Validate ALL skills
python scripts/validate-all.py

# Deep validation (checks frontmatter, structure, references)
python scripts/deep-validate.py

# List all skills
python scripts/list-skills.py
```

## Adding a New Domain

1. Create folder `.claude/skills/{domain}/`
2. Add at least one skill in `.claude/skills/{domain}/{skill-name}/SKILL.md`
3. Update `skills_catalog.json`
4. Update the domain table in `README.md`
5. Update `MODELS.md`

## Pull Request Process

1. Ensure your skill passes validation
2. Update the `skills_catalog.json` if adding a new skill
3. Update documentation if changing behavior
4. Your PR will be reviewed within 48 hours
5. Once approved, a maintainer will merge it

### PR Checklist

- [ ] Skill name is in `kebab-case`, ≤64 characters
- [ ] Description is in 3rd person, ≤1024 characters
- [ ] `SKILL.md` has valid YAML frontmatter
- [ ] Tags and category are correct
- [ ] Tested in Claude (minimum Sonnet)
- [ ] `skills_catalog.json` is updated (if new skill)
- [ ] `python scripts/validate-all.py` passes

## Style Guides

### Markdown
- Use `#` for headers (start at H2 within skill content)
- Use code blocks with language tags
- Use `>` for notes and warnings
- Keep line length under 100 characters

### Frontmatter
- `name`: lowercase, kebab-case
- `description`: 3rd person, present tense
- `category`: must match an existing domain folder
- `tags`: array of relevant keywords
- `models`: array of compatible Claude models
- `version`: semver string

## Questions?

- Telegram: [@ssrjkk](https://t.me/ssrjkk)
- Email: [ray013lefe@gmail.com](mailto:ray013lefe@gmail.com)
- GitHub Issues: [Create an issue](https://github.com/ssrjkk/claude-skills/issues/new)

---

**Thank you for contributing!** Every skill helps the entire community build faster. 
