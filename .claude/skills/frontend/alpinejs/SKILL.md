---
name: alpinejs
description: "Adds JavaScript behavior to HTML with Alpine.js, a minimal reactive framework. Use for sprinkling interactivity into server-rendered apps."
category: frontend
tags: [alpinejs, javascript, reactive, html, lightweight]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Alpine.js

> Minimal JavaScript framework for composing behavior directly in HTML.

## Quick Start
```html
<script src="https://unpkg.com/alpinejs" defer></script>
<div x-data="{ count: 0 }">
  <button @click="count++">Clicked <span x-text="count"></span> times</button>
</div>
```

## Directives
- `x-data` — Component data scope
- `x-bind` / `:` — Bind attributes
- `x-on` / `@` — Event listeners
- `x-show` — Toggle visibility (`display: none`)
- `x-model` — Two-way binding
- `x-for` — Loops over arrays
- `x-text` — Set innerText
- `x-html` — Set innerHTML

## When to Use
- Server-rendered HTML with interactivity
- Laravel/Rails/Django apps
- Replacing jQuery
- Simple interactive components

## Validation
1. Reactive state updates DOM
2. Event handlers fire correctly
3. x-show and x-if toggle visibility
