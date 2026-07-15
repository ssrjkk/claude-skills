---
name: remix
description: "Builds full-stack web applications with Remix, nested routes, and server-side rendering. Use for modern React apps with SSR."
category: frontend
tags: [remix, react, ssr, fullstack, web]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Remix

> Full-stack React framework with nested routing and SSR.

## Quick Start
```typescript
// app/routes/_index.tsx
import { json } from "@remix-run/node";
import { useLoaderData } from "@remix-run/react";

export const loader = async () => {
  return json({ message: "Hello from Remix!" });
};

export default function Index() {
  const { message } = useLoaderData<typeof loader>();
  return <h1>{message}</h1>;
}
```

## When to Use
- ✅ Full-stack React apps
- ✅ SEO-optimized content sites
- ❌ Not for static blogs (better Astro)

## Step-by-Step Instructions
1. Create project: `npx create-remix@latest`
2. Choose deployment target (Vercel, Cloudflare, Node)
3. Create routes in `app/routes/`
4. Run: `npm run dev`

## Dependencies
```bash
npx create-remix@latest
```

## Examples
Input: `npx create-remix@latest my-app` → Output: Remix project with routes scaffolded

## Resources
- [Remix Docs](https://remix.run/docs)
- [Examples](./examples/)

## Validation
1. Dev server starts without errors
2. Routes render correctly
3. Forms/submissions work
