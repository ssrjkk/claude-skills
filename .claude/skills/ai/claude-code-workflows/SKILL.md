---
name: claude-code-workflows
description: "Advanced Claude Code workflows and automation"
category: ai
tags: [claude, workflows, automation, ci, devops]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Claude Code Workflows

> Build automated development pipelines with Claude Code for CI/CD, code review, and maintenance.

## Quick Start
```bash
# Automated PR review workflow
claude -p "Review all changed files in this PR. Check for:\n1. Security vulnerabilities\n2. Type safety issues\n3. Performance regressions\n4. Missing error handling\nOutput a structured review report."

# Batch refactoring across many files
claude -p "Rename all usages of `oldFunction` to `newFunction` across the src/ directory. Update type definitions accordingly."

# Automated changelog generation
git log --oneline $(git describe --tags --abbrev=0)..HEAD | claude -p "Generate a changelog from these commits, grouped by type (feat, fix, chore, docs)."

# CI integration script
cat << 'SCRIPT' > .ci/claude-review.sh
#!/bin/bash
git diff main...HEAD --name-only | claude -p "Review these changed files for bugs and style issues. Format output as GitHub Actions annotations."
SCRIPT
```

## Key Concepts
Chain Claude Code calls together for multi-stage workflows. Use with git hooks, CI pipelines, and cron jobs. Pipe data between stages for context. Store CLAUDE.md with project conventions for consistent output.

## When to Use
- Automated PR code review in CI pipelines
- Scheduled dependency updates and code migrations
- Release automation (changelogs, version bumps, release notes)

## Validation
1. Workflow script runs end-to-end without manual intervention
2. Claude respects project conventions defined in CLAUDE.md
3. Output is structured and usable by downstream tools
