# Contributing Guide

## Checklist Before PR
- [ ] `name` in kebab-case, ≤64 characters
- [ ] `description` in 3rd person, ≤1024 characters
- [ ] `SKILL.md` follows the template
- [ ] Tags and category added
- [ ] Tested in Claude (min. sonnet)

## Testing a Skill
1. Open Claude → connect local folder
2. Invoke skill: "Use skill {name} for {task}"
3. Verify: accuracy, completeness, no hallucinations

## Adding a New Domain
1. Create folder `.claude/skills/{domain}/`
2. Add `domain-index.md` with domain description
3. Update `skills_catalog.json` and `README.md`

## Skill Structure
```
.claude/skills/{skill-name}/
├── SKILL.md           # Main skill file
├── examples.md        # Usage examples
├── reference.md       # Reference information
└── scripts/          # Helper scripts
```

Thanks for your contribution!
