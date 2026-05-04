---
name: svelte-kit
description: Creates SvelteKit applications with file-based routing and server-side rendering. Use for lightweight, fast web applications.
category: frontend
tags: [svelte, sveltekit, frontend, ssr]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# SvelteKit

> Fast framework for creating Svelte applications with server-side rendering.

## 🚀 Quick Start
```svelte
<!-- src/routes/+page.svelte -->
<script>
    let count = 0;
    function increment() {
        count += 1;
    }
</script>

<button on:click={increment}>
    Clicked {count} times
</button>
```

## 📋 When to Use
- ✅ Lightweight, high-performance applications
- ✅ Need SSR with minimal JS bundle
- ❌ Not if team only knows React/Vue

## 🔧 Step-by-Step Instructions
1. Create project: `npm create svelte@latest my-app`
2. Create routes in `src/routes/`
3. Add server logic in `+page.server.js`
4. Run: `npm run dev`

## 📦 Dependencies
```bash
npm create svelte@latest my-app
```

## 🧪 Examples
Input: Button click → counter increments reactively

## 🔗 Resources
- [SvelteKit Docs](https://kit.svelte.dev/)
- [Examples](./examples/)

## ✅ Validation
1. App builds without errors
2. Routing works via file structure
3. Svelte reactivity functions
