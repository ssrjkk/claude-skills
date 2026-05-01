# Integration Guide

## How to use Claude Skills

### Option 1: Local Folder (Recommended)

1. Clone this repository:
```bash
git clone https://github.com/ssrjkk/claude-skills.git
cd claude-skills
```

2. Open Claude.ai → Settings → **Skills**
3. Click **Add local folder**
4. Select the path: `/path/to/claude-skills/.claude/skills/`
5. Claude will automatically load all skills

### Option 2: Individual Skill

1. Copy any skill folder to your project:
```bash
cp -r .claude/skills/python-fastapi ~/.claude/skills/
```

2. Restart Claude if needed

## Using Skills in Chat

Once connected, simply mention the skill in your chat:

```
Use the python-fastapi skill to create a REST API for user management
```

Or just describe your task naturally:
```
I need to create a FastAPI project with user authentication
```

Claude will automatically detect and use the relevant skill.

## Skill Compatibility Matrix

| Skill | Haiku | Sonnet | Opus |
|-------|-------|--------|------|
| python-fastapi | ❌ | ✅ | ✅ |
| nodejs-express | ✅ | ✅ | ✅ |
| api-testing | ✅ | ✅ | ❌ |
| ... | ... | ... | ... |

For full matrix, see `.claude/MODELS.md`

## Troubleshooting

**Skill not detected?**
- Ensure the path points to `.claude/skills/` folder
- Check that `SKILL.md` exists in each skill folder
- Restart Claude.ai after adding new skills

**Skill not working as expected?**
- Check the skill's `models` field - some skills work better with specific models
- Review `SKILL.md` for the correct usage pattern
- Open an issue if the skill needs improvement
