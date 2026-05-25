---
name: claude-code
description: Using Claude Code CLI for autonomous development
category: ai
tags: [claude, cli, development, automation, terminal]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Claude Code

> Leverage Claude Code CLI for AI-powered software development directly in your terminal.

## Quick Start
```bash
# Install Claude Code
npm install -g @anthropic-ai/claude-code

# Start a session in your project
claude

# Run with a specific task
claude "Add input validation to the login form"

# Use file references
claude "Refactor src/auth.ts to use async/await"

# Run in non-interactive mode
claude -p "Add unit tests for the payment module"

# Use with pipe
cat bug-report.md | claude -p "Fix all issues described in this report"
```

## Key Concepts
Claude Code operates as an autonomous coding agent in your terminal. It reads files, writes code, runs commands, and iterates on solutions. Use `-p` for headless mode, `-f` for follow-up questions, and `CLAUD.md` for project-level customization.

## When to Use
- Automated code generation and refactoring
- Bug fixing from error logs or descriptions
- Test generation and documentation writing
- Code review and analysis

## Validation
1. `claude --version` returns the installed version
2. A session starts and Claude can read project files
3. Claude successfully writes and modifies code files
