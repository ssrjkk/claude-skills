---
name: design-tokens
description: Manages design tokens with Style Dictionary or Theo. Use for maintaining design system consistency.
category: design
tags: [design-tokens, design-system, style-dictionary, theming]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# Design Tokens

> Manage design tokens for consistent UI systems.

## Quick Start
```json
{
  "color": {
    "primary": { "value": "#007AFF" },
    "secondary": { "value": "#5856D6" }
  },
  "spacing": {
    "small": { "value": "8px" },
    "medium": { "value": "16px" }
  }
}
```

## When to Use
- ✅ Design systems across multiple platforms
- ✅ Need consistency in colors, spacing, fonts
- ❌ Not for one-off projects

## Step-by-Step Instructions
1. Define tokens in JSON/YAML file
2. Configure Style Dictionary
3. Generate platform-specific files
4. Integrate into project

## Dependencies
```bash
npm install style-dictionary
```

## Examples
Input: Token `color.primary` → Output: CSS variable `--color-primary: #007AFF;`

## Resources
- [Style Dictionary](https://amzn.github.io/style-dictionary/)
- [Examples](./examples/)

## Validation
1. Tokens generated for all platforms
2. Values applied correctly
3. Themes (light/dark) switch properly
