---
name: claude-code-customization
description: "Customizing Claude Code with CLAUDE.md"
category: ai
tags: [claude, configuration, customization, project-setup]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Claude Code Customization

> Tailor Claude Code's behavior per-project using CLAUDE.md configuration files.

## Quick Start
```markdown
# CLAUDE.md — Project Configuration for Claude Code

## Project Overview
E-commerce platform built with Next.js, Prisma, and PostgreSQL.
Uses tRPC for API routes and Zod for validation.

## Code Conventions
- React components: functional with hooks, no class components
- API routes: tRPC routers in src/server/routers/
- Database: Prisma with migrations in prisma/
- Testing: Vitest with React Testing Library
- Types: strict TypeScript, no `any`

## Commands
- Build: `npm run build`
- Test: `npm run test`
- Lint: `npm run lint`
- Dev: `npm run dev`
- Type-check: `npm run typecheck`

## Architecture
- /src/app — Next.js App Router pages
- /src/components — Shared React components
- /src/server — tRPC server routers and middleware
- /prisma — Database schema and migrations
- /public — Static assets

## Preferences
- Use path aliases (@/ for src/)
- Prefer async/await over raw promises
- Use `zod` for all input validation
```

## Key Concepts
CLAUDE.md files act as system prompts for Claude Code. Place them at the project root or in subdirectories for scoped configuration. Include project overview, conventions, commands, architecture, and any critical constraints.

## When to Use
- Setting up a new project for AI-assisted development
- Onboarding Claude Code to large existing codebases
- Enforcing project-specific patterns and conventions

## Validation
1. Claude Code sessions respect the defined conventions
2. Claude uses correct commands from the config
3. Claude follows the specified architecture patterns in new code
