---
name: windsurf-ide
description: Using Windsurf/Cascade IDE
category: ai
tags: [windsurf, cascade, ide, ai, editor]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Windsurf IDE

> Harness Windsurf's Cascade AI for flow-state development with deep code understanding.

## Quick Start
```markdown
# Windsurf & Cascade Guide

## Cascade Modes
- **Ask Mode** (`Ctrl+L`): Questions, explanations, codebase exploration
- **Edit Mode** (`Ctrl+I`): Inline code generation and modification
- **Agent Mode**: Autonomous task execution across files

## Key Features
- **Deep Context**: Cascade understands your entire codebase, not just open files
- **Flow State**: Predicts your next action and pre-loads context
- **Multi-file Editing**: Edits across multiple files with one command
- **Terminal Integration**: Cascade can run and interpret terminal commands
- **Web Search**: Built-in web search through Cascade

## Workflow
1. Open project → Cascade auto-indexes
2. Describe task in natural language
3. Review AI-generated changes
4. Accept/reject with diff view

## Rules (.windsurfrules)
```
# .windsurfrules
Always use TypeScript strict mode
Prefer functional components with hooks
Use path alias @/ for src/
Write unit tests for all new functions
```
```

## Key Concepts
Windsurf focuses on "flow state" — proactive AI that anticipates needs. Cascade indexes your full codebase for context-aware assistance. Use `.windsurfrules` to encode project conventions.

## When to Use
- Large codebases requiring deep context understanding
- Complex refactoring across many interconnected files
- Teams wanting consistent AI-assisted development patterns

## Validation
1. Cascade answers questions correctly about codebase structure
2. Multi-file edits maintain consistency across all changed files
3. Agent mode completes tasks without hallucinating file contents
