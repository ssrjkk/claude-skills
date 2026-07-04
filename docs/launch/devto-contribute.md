# How to Contribute to the World's Largest AI Skills Library

## Why Contribute?
The Claude Skills Library is 10,000+ skills strong — but we need the community to make it truly great. Whether you're fixing a typo, adding a new domain, or writing a comprehensive skill, your contribution helps everyone build better software with AI.

## Quick Start

```bash
# Clone the repo
git clone https://github.com/ssrjkk/claude-skills.git
cd claude-skills

# Install the SDK
pip install -e ".[dev]"

# Validate existing skills
make validate

# Run tests
make test
```

## Adding a New Skill

### 1. Choose a domain
Pick from 39 existing domains or propose a new one.

### 2. Create the skill directory
```
.claude/skills/{domain}/{skill-name}/
├── SKILL.md
└── SKILL.ru.md (if bilingual)
```

### 3. Write the frontmatter
```yaml
---
name: my-awesome-skill
description: What this skill does
category: backend
tags: [python, fastapi, api]
models: [claude-3-5-sonnet, claude-4]
version: 1.0.0
created: 2026-07-04
updated: 2026-07-04
---
```

### 4. Include required sections
- **Quick Start** — minimal example
- **When to Use** — context and prerequisites
- **Step-by-Step** — detailed instructions
- **Validation** — how to verify the output

### 5. Run validation
```bash
make validate
make test
make quality
```

## Skill Quality Standards
- Minimum 500 characters of real content
- Working code examples (not placeholders)
- All required sections present
- No TODO/FIXME patterns
- Real Russian translations (not machine-translated)

## Adding a New Domain
1. Open an issue proposing the domain
2. Wait for community feedback
3. Add at least 10 skills to demonstrate coverage
4. Update `VALID_CATEGORIES` in the Python SDK

## PR Process
1. Fork the repo
2. Create a feature branch
3. Add/improve skills
4. Run validation pipeline
5. Submit PR with clear description

## Recognition
All contributors are listed in the community hall of fame. Top contributors earn badges (Top Contributor, Active Contributor, Verified Skill, Translator, Bug Hunter).

## Links
- GitHub: https://github.com/ssrjkk/claude-skills
- Contributing guide: https://github.com/ssrjkk/claude-skills/blob/main/.github/CONTRIBUTING.md
- Community: https://github.com/ssrjkk/claude-skills/community
