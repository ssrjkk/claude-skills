---
name: ai-coding-workflow
description: "Modern AI-assisted development workflow"
category: ai
tags: [workflow, ai-assisted, development, best-practices]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# AI Coding Workflow

> A systematic approach to modern AI-assisted software development from spec to deployment.

## Quick Start
```bash
# 1. Specification
cat > spec.md << 'EOF'
## Feature: User Authentication
- Email/password login with JWT
- OAuth (Google, GitHub)
- Session management with refresh tokens
- Rate limiting on login attempts
EOF

# 2. Architecture review with AI
claude -p "Review this spec for completeness. Identify missing edge cases and security considerations." < spec.md

# 3. Implementation with AI pair programming
claude -p "Implement the authentication system per spec.md. Use FastAPI, SQLAlchemy, and python-jose. Include comprehensive error handling."

# 4. Test generation
claude -p "Write pytest tests for the auth module. Cover: happy path, invalid credentials, token expiry, rate limiting, OAuth flow."

# 5. Code review
claude -p "Review the auth module for security vulnerabilities, specifically: SQL injection, JWT secret handling, timing attacks on comparison."
```

## Key Concepts
The modern AI workflow: Spec → Architecture Review → Implementation → Test Generation → Code Review → Deployment. Each phase uses AI differently—from creative generation to critical analysis.

## When to Use
- Starting new projects with AI from the ground up
- Adding complex features to existing codebases
- Implementing security-critical code that needs thorough review

## Validation
1. Each phase produces artifacts (spec, tests, code) that build on previous phases
2. AI-generated code passes existing test suite
3. Security review identifies no critical vulnerabilities
