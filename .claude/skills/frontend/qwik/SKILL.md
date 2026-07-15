---
name: qwik
description: "Creates instant-loading web applications with Qwik, resumability, and fine-grained lazy loading. Use for maximum performance SPAs."
category: frontend
tags: [qwik, resumable, performance, framework, typescript]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Qwik

> Resumable framework for instant-loading web applications.

## Quick Start
```bash
npm create qwik@latest
cd my-app && npm start
```

## Components
```tsx
export default component$(() => {
  const count = useSignal(0)
  return <button onClick$={() => count.value++}>{count.value}</button>
})
```

## Route Loaders
```tsx
export const useData = routeLoader$(async () => {
  const data = await fetch('https://api.example.com/data')
  return data.json()
})
```

## When to Use
- SEO-critical applications
- Slow network environments
- Large enterprise SPAs
- E-commerce and content sites

## Validation
1. App loads instantly on first visit
2. Code splits and lazy loads correctly
3. Resumability preserves state after pause
