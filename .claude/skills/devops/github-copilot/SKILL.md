---
name: github-copilot
description: GitHub Copilot setup and optimization
category: devops
tags: [github-copilot, ai, code-generation, productivity]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# GitHub Copilot

> Configure and optimize GitHub Copilot for maximum developer productivity.

## Quick Start
```markdown
# Copilot Setup & Configuration

## Installation
1. VS Code: Extensions → search "GitHub Copilot" → Install
2. JetBrains: Settings → Plugins → Marketplace → GitHub Copilot
3. Neovim: `:Copilot setup`
4. Authenticate with GitHub account

## Configuration (.vscode/settings.json)
```json
{
  "github.copilot.enable": {
    "*": true,
    "plaintext": false,
    "markdown": true
  },
  "github.copilot.inlineSuggest.enable": true,
  "github.copilot.advanced": {
    "length": 100,
    "inlineSuggestCount": 3
  },
  "editor.inlineSuggest.enabled": true,
  "github.copilot.editor.enableAutoCompletions": true
}
```

## Optimizing Suggestions
- Write clear function names and JSDoc comments
- Provide examples in comments: `// Example: sum([1, 2, 3]) → 6`
- Open relevant files for context
- Use descriptive variable names
- Keep function scope focused

## Shortcuts
- `Tab`: Accept suggestion
- `Ctrl+→`: Accept word
- `Ctrl+Enter`: Open Copilot suggestions panel
- `Alt+]`: Next suggestion
- `Alt+[`: Previous suggestion
```

## Key Concepts
Copilot learns from your open files, comments, and function signatures. Better context = better suggestions. Use comments as specifications. Works best with well-structured, typed code.

## When to Use
- Writing boilerplate code (getters, setters, CRUD operations)
- Implementing well-defined functions from comments
- Generating unit tests and test data
- Writing repetitive patterns (API endpoints, database queries)

## Validation
1. Copilot activates (icon in status bar shows active)
2. Suggestions appear while typing
3. `Ctrl+Enter` shows multiple alternatives
4. Suggestions improve with better context/comments
