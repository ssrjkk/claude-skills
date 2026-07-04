# Product Hunt Launch Draft

## Title
**Claude Skills Library — 10,000+ bilingual skills for Claude Code**

## Tagline
The largest open library of battle-tested skills for Claude Code. 39 domains, English + Russian, quality-scored, 93% test coverage.

## Description

**What is it?**
Claude Skills Library is an open collection of 10,000+ structured, executable skill definitions for Claude Code and other AI coding assistants. Each skill is a markdown file with YAML frontmatter that teaches the AI how to handle specific tasks — from API testing to Kubernetes deployment.

**Why 10,000?**
We didn't just dump a million prompts. Skills are organized into 39 domains, each with working code examples, validation steps, and bilingual (EN + RU) translations. The library includes a Python SDK for validation, quality scoring (A–F), and catalog management.

**What makes it different?**
- **Dual language**: Only library with full Russian + English support
- **Quality scoring**: Every skill graded on completeness, depth, code quality, freshness, and bilingual accuracy
- **SDK included**: Python + TypeScript packages for validation and management
- **Validation in 7.8 seconds**: Full pipeline checks all 10,000+ files
- **93% test coverage**: 82 test cases with property-based testing
- **4 product components**: Python CLI, VS Code extension, GitHub Action, TypeScript SDK
- **GitHub Action**: Validate skills in CI/CD with `ssrjkk/claude-skills`
- **VS Code Extension**: Browse + install 10K skills from sidebar
- **Next.js site**: Static-generated catalog with search, dark mode, 10K pages
- **Featured skills**: 50 curated starter skills across 15 core domains

**Who is it for?**
- Developers using Claude Code for daily coding
- Teams standardizing their AI workflow
- Russian-speaking developers who need native-language AI instructions
- Anyone who wants to level up their AI coding assistant

## Maker Comment

I built this because I was tired of getting the same generic output from Claude every time. "Write tests" → basic tests. "Deploy to Kubernetes" → generic config.

So I started collecting patterns. Then organizing them. Then structuring them with YAML frontmatter, quality scores, and bilingual translations.

3 months later: 10,000+ skills across 39 domains. A Python SDK. TypeScript package. GitHub Action. VS Code extension. Next.js site. 93% test coverage. Full CI/CD pipeline.

The kicker? It's the first bilingual AI skills library — every skill has a parallel Russian translation.

**Quick start:**
```bash
curl -fsSL https://raw.githubusercontent.com/ssrjkk/claude-skills/main/install.sh | bash
claude-skills search kubernetes
claude-skills install kubernetes-deployment
```

Check it out: https://github.com/ssrjkk/claude-skills

## Images
[Screenshot of docs site with search filtering]
[Screenshot of VS Code extension sidebar]
[Screenshot of GitHub Action running]
[GIF of CLI install command]

## Tags
developer-tools, ai, open-source, productivity, claude
