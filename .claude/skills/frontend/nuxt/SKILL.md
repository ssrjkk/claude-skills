---
name: nuxt
description: Creates universal Vue applications with Nuxt 3, file-based routing, SSR, and auto-imports. Use for SEO-friendly Vue apps.
category: frontend
tags: [nuxt, vue, ssr, ssg, vue3]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Nuxt

> Vue.js framework with SSR, SSG, and file-based routing.

## Quick Start
```bash
npx nuxi init my-app
cd my-app
npm run dev
```

## When to Use
- SEO-critical Vue apps
- Full-stack Vue applications
- Static generated sites
- Enterprise dashboards

## Step-by-Step
1. Init project: `npx nuxi init`
2. Create pages in `pages/` directory
3. Use auto-imported components
4. Deploy with `npm run build`

## Dependencies
```bash
npm install nuxt
```

## Examples
```vue
<template>
  <div>
    <h1>{{ title }}</h1>
    <NuxtLink to="/about">About</NuxtLink>
  </div>
</template>
<script setup>
const { data: title } = await useFetch('/api/title')
</script>
```

## Resources
- [Nuxt Docs](https://nuxt.com/docs)

## Validation
1. Dev server runs on port 3000
2. SSR renders HTML correctly
3. Navigation works without full reload
