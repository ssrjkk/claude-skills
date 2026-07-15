---
name: htmx
description: "Builds dynamic web UIs with htmx, HTML-over-the-Wire, and hypermedia-driven interactions. Use for server-rendered apps with modern UX."
category: frontend
tags: [htmx, html, hypermedia, ajax, server-rendered]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# htmx

> Access modern browser features directly from HTML, without JavaScript.

## Quick Start
```html
<script src="https://unpkg.com/htmx.org"></script>
<button hx-get="/api/clicked" hx-swap="outerHTML">Click Me</button>
<div hx-get="/api/updates" hx-trigger="every 10s" hx-target="#status">Loading...</div>
```

## Core Attributes
- `hx-get`, `hx-post`, `hx-put`, `hx-delete` — HTTP methods
- `hx-target` — Where to swap response content
- `hx-swap` — How to swap (innerHTML, outerHTML, beforebegin, afterend, delete, none)
- `hx-trigger` — Event that triggers request (click, change, keyup, every 5s, revealed, etc.)
- `hx-indicator` — Loading indicator element

## When to Use
- Server-rendered applications
- Progressive enhancement
- Django/Rails/Express apps
- Replacing jQuery interactions

## Validation
1. AJAX requests replace content correctly
2. All triggers fire as expected
3. Form submissions work without page reload
