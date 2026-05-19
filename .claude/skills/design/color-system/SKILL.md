---
name: color-system
description: Designs color systems and design tokens for consistent UI theming across light and dark modes.
category: design
tags: [color, design-tokens, theming, accessibility, ui]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Color System
> Designing scalable color systems for UI theming.
## Quick Start
```css
:root { --gray-50: #f9fafb; --gray-500: #6b7280; --gray-900: #111827; --primary-500: #3b82f6; --color-success: #10b981; --color-warning: #f59e0b; --color-error: #ef4444; }
[data-theme="dark"] { --gray-50: #1e293b; --gray-500: #64748b; --gray-900: #f8fafc; }
```
## WCAG Requirements
- AA Normal text: 4.5:1; AA Large text: 3:1; AAA Normal text: 7:1
## When to Use
- Design system foundations; Dark mode theming; Accessibility compliance
## Validation
1. Token pairs meet WCAG AA; 2. Dark mode switches smoothly; 3. Semantic tokens consistently used
