---
name: typography-system
description: Creates scalable typography systems with type scale, line height, and responsive text tokens.
category: design
tags: [typography, fonts, design-tokens, responsive, type-scale]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Typography System
> Building consistent type scales and typography tokens.
## Quick Start
```css
:root { --text-xs: 0.75rem; --text-sm: 0.875rem; --text-base: 1rem; --text-lg: 1.125rem; --text-xl: 1.25rem; --text-2xl: 1.5rem; --text-3xl: 1.875rem; --text-4xl: 2.25rem; --leading-tight: 1.25; --leading-normal: 1.5; --font-normal: 400; --font-bold: 700; }
```
## Text Styles
```css
.heading-1 { font-size: var(--text-4xl); font-weight: var(--font-bold); line-height: var(--leading-tight); }
.body { font-size: var(--text-base); font-weight: var(--font-normal); line-height: var(--leading-normal); }
```
## When to Use
- Design system foundations; Responsive typography; Brand consistency
## Validation
1. Type scale maintains consistent ratio; 2. Text meets WCAG size requirements; 3. Responsive sizes adapt
