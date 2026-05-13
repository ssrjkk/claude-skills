---
name: tailwind-css
description: Creates responsive UIs with Tailwind CSS utility classes and custom design tokens. Use for rapid, consistent styling.
category: frontend
tags: [tailwind, css, design, responsive, frontend]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Tailwind CSS

> Utility-first CSS for rapid UI development.

## Quick Start
```html
<div class="flex items-center justify-between p-4 bg-white shadow rounded-lg">
  <h1 class="text-2xl font-bold text-gray-900">Hello, Tailwind</h1>
  <button class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">
    Click me
  </button>
</div>
```

## When to Use
- ✅ Rapid UI prototyping
- ✅ Consistent design system
- ❌ Not for complex component libraries (better Material UI)

## Step-by-Step Instructions
1. Install: `npm install -D tailwindcss @tailwindcss/cli`
2. Init: `npx tailwindcss init`
3. Configure `content` paths
4. Add Tailwind directives to CSS

## Dependencies
```bash
npm install -D tailwindcss postcss autoprefixer
```

## Examples
Input: `npx tailwindcss -i input.css -o output.css --watch` → Output: Compiled CSS with all utilities

## Resources
- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [Examples](./examples/)

## Validation
1. CSS compiles without errors
2. Utility classes apply correctly
3. Responsive breakpoints work
