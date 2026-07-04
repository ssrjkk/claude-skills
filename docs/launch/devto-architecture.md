# Building a Bilingual AI Skills Library — Architecture & Design

## Introduction
Over the last 3 months, I built the largest open library of structured skills for Claude Code. This is the first article in a series covering the architecture, quality system, and community-building behind 10,000+ bilingual AI skills.

## The Problem
AI coding assistants are incredibly powerful, but they lack context. When you ask Claude to "write tests" or "deploy to Kubernetes," you get generic output that requires significant editing. The solution? Structured skills — markdown files with YAML frontmatter that teach AI assistants how to handle specific tasks.

## Architecture Overview

```
.claude/skills/
├── backend/
│   ├── fastapi-crud/
│   │   ├── SKILL.md
│   │   └── SKILL.ru.md
│   └── django-rest/
├── devops/
│   ├── kubernetes-deployment/
│   └── docker-compose/
├── frontend/
│   ├── react-component-library/
│   └── nextjs-fullstack/
└── ... (39 domains)
```

Each skill is a markdown file with YAML frontmatter containing:
- `name` — unique identifier
- `description` — what this skill does
- `category` — one of 39 domains
- `tags` — for search and discovery
- `models` — compatible Claude models
- `version` — semantic versioning
- `created` / `updated` — timestamps

## Python SDK
The core of the library is the Python SDK with four main components:

1. **CatalogBuilder** — scans skill directories, parses frontmatter, builds in-memory catalog, serializes to JSON
2. **ValidationPipeline** — validates frontmatter, body content, structure, and detects anti-patterns
3. **QualityAnalyzer** — scores skills on 5 dimensions with weighted overall score
4. **CLI** — install, search, generate, validate, quality, catalog, stats commands

## Bilingual Design
Every skill has a parallel Russian translation (`SKILL.ru.md`). This required:
- Consistent frontmatter across translations
- Synchronized version numbers
- Validation that translations are real (not machine-translated)
- UI indicators (RU badge) in the catalog

## TypeScript SDK
A parallel TypeScript SDK is available for Node.js projects with the same types and utility functions.

## Next.js Documentation Site
A fully searchable documentation site built with Next.js 16 (static export), featuring:
- Live search with category/tag filtering
- Static generation of all 10,000+ skill pages
- Dark mode
- Copy-install buttons

## Links
- GitHub: https://github.com/ssrjkk/claude-skills
- Documentation: https://ssrjkk.github.io/claude-skills/
- TypeScript SDK: `npm install claude-skills`
