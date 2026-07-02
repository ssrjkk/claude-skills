# Examples: Using Claude Skills in Real Projects

This directory contains real-world examples of using skills from the library.

## 🚀 Quick Start Example

```bash
# 1. Clone the library
git clone https://github.com/ssrjkk/claude-skills.git
cd claude-skills

# 2. Install SDK
pip install -e .

# 3. Find a skill
claude-skills stats | grep qa

# 4. Read a skill
cat .claude/skills/qa/pytest-basics/SKILL.md
```

## 🎯 Before vs After

### Without skill
```
User: "Write tests for my FastAPI app"
Claude: [generic test suggestions, misses project-specific patterns]
```

### With `api-testing` skill
```
User: "Write tests for my FastAPI app"
Claude: [activates qa/api-testing skill]
- pytest configuration with asyncio support
- TestClient patterns with auth headers
- Database fixture with rollback
- Response validation with Pydantic
- Coverage configuration
```

## 📊 Domain-Specific Examples

### Backend: FastAPI + PostgreSQL
```
Skill: backend/fastapi-api
Produces: project structure, models, CRUD endpoints, DB migrations, tests
Time saved: ~30 min per API endpoint
```

### Frontend: React + TypeScript
```
Skill: frontend/react-component
Produces: typed component, Storybook stories, unit tests, accessibility
Time saved: ~20 min per component
```

### DevOps: Docker + K8s
```
Skill: devops/docker-compose
Produces: multi-service compose file, health checks, volumes, networks
Time saved: ~40 min per service
```

## 🔧 Workflow Integration

### VS Code
```json
{
  "claude.skills.path": "$HOME/.claude/skills"
}
```

### GitHub Actions
```yaml
- name: Validate skills
  run: |
    pip install -e ./claude-skills
    claude-skills validate
```

### Pre-commit Hook
```yaml
repos:
  - repo: local
    hooks:
      - id: validate-skills
        name: Validate skills
        entry: claude-skills validate
        language: system
        pass_filenames: false
```
