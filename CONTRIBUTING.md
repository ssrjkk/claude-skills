# Contributing

Thanks for contributing to Claude Skills Library!

## Bilingual Structure

Every skill has two files:
- `.claude/skills/{category}/{name}/SKILL.md` — English (primary)
- `.claude/skills/{category}/{name}/SKILL.ru.md` — Russian (parallel translation)

Both files share the same directory and name prefix. The RU file includes `original:` in frontmatter linking back to the EN version.

## Skill Template (EN)

```yaml
---
name: my-skill-name
description: Clear one-line description of what this skill does
category: ai|backend|frontend|devops|database|security|qa|...
tags: [tag1, tag2, tag3]
models: [sonnet, opus]
version: "1.0"
---
```

Required sections: Quick Start, When to Use, Step-by-Step, Dependencies, Examples, Resources, Validation.

## Skill Template (RU)

```yaml
---
name: my-skill-name
description: Однострочное описание навыка
category: ai|backend|frontend|devops|database|security|qa|...
tags: [tag1, tag2, tag3]
models: [sonnet, opus]
version: "1.0"
original: my-skill-name
language: ru
---
```

The `original` field must match the `name` of the corresponding EN skill. The `language: ru` field identifies this as the Russian variant.

## Checklist

- [ ] Name matches directory name (lowercase, hyphen-separated)
- [ ] Frontmatter has all required fields: name, description, category, tags, models, version
- [ ] Has Quick Start with runnable code
- [ ] Has Step-by-Step with actionable instructions
- [ ] Dependencies are specified with versions
- [ ] Examples compile/run correctly
- [ ] Validation section has concrete verification steps
- [ ] No placeholder content (TODO, FIXME, "See docs")
- [ ] Body is meaningful (>200 chars)
- [ ] RU file has `language: ru` and `original:` pointing to EN name

## Validation

```bash
# Structural check (both languages)
python scripts/validate-all.py

# Deep validation
python scripts/deep-validate.py

# Regenerate catalog (auto-detects RU files)
python scripts/generate-catalog.py
```

## PR Process

1. Fork and create a branch: `skill/{category}/{name}`
2. Add your SKILL.md (EN)
3. Add your SKILL.ru.md (RU) — optional but encouraged
4. Run validation
5. Open a PR with description of what the skill does
6. A maintainer will review within 48h

## Style Guide

- **Names**: lowercase, hyphen-separated: `async-queue-processing`
- **Descriptions**: start with verb, under 120 chars (EN); Russian equivalents in RU file
- **Code**: must be runnable or clearly annotated
- **Steps**: 3-7 actionable steps, each a concrete action
- **Dependencies**: pin minimum versions
- **Translations**: keep RU content faithful to EN, localized for Russian-speaking audience

**Remember**: Quality over quantity. One thorough skill is worth 100 templates.