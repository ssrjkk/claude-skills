# Contributing Guide

## Checklist before PR
- [ ] 'name' in kebab-case, ≤64 characters
- [ ] 'description' in 3rd person, ≤1024 characters
- [ ] 'SKILL.md' follows the pattern
- [ ] Tags and category added
- [ ] Tested in Claude (min. sonnet)

## Skill testing
1. Open Claude → connect your local folder
2. Call the skill: 'Use the {name} skill for {task}'
3. Check: accuracy, completeness, absence of hallucinations

## Adding a new domain
1. Create a folder '.claude/skills/{domain}/'
2. Add 'domain-index.md' with the domain description
3. Update 'skills_catalog.json' and 'README.md'

## Skill structure
'''
.claude/skills/{skill-name}/
├── SKILL.md # Main skill file
├── examples.md # Examples of use
├── reference.md # Help information
└── scripts/ # Auxiliary scripts
'''

Thank you for your contribution!
