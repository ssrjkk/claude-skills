---
name: astro-ssg
description: Creates static sites with Astro, supporting any UI framework. Use for fast content-oriented sites.
category: frontend
tags: [astro, ssg, static-site, markdown, mdx]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# Astro SSG

> Fast static sites with Astro and any UI framework.

## 🚀 Quick Start
```astro
---
// src/pages/index.astro
const title = "Hello Astro";
---
<html>
  <head><title>{title}</title></head>
  <body>
    <h1>{title}</h1>
  </body>
</html>
```

## 📋 When to Use
- ✅ Content sites (blogs, documentation)
- ✅ Need maximum performance
- ❌ Not for complex SPAs with heavy state

## 🔧 Step-by-Step Instructions
1. Create project: `npm create astro@latest`
2. Add integrations (React, Vue, Svelte)
3. Create pages in `src/pages/`
4. Run: `npm run dev`

## 📦 Dependencies
```bash
npm create astro@latest
```

## 🧪 Examples
Input: Create MDX page → Output: Static HTML page

## 🔗 Resources
- [Astro Docs](https://docs.astro.build/)
- [Examples](./examples/)

## ✅ Validation
1. Site builds to static HTML files
2. Markdown/MDX processed correctly
3. UI framework integrations work
