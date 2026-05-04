---
name: nextjs-ssr
description: Generates Next.js applications with SSR, SSG, and API routes. Use for SEO-optimized React applications.
category: frontend
tags: [nextjs, react, ssr, ssg, seo]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# Next.js SSR

> React framework for production with SSR, SSG and SEO optimization.

## 🚀 Quick Start
```typescript
// pages/api/users.ts
import { NextApiRequest, NextApiResponse } from 'next';

export default function handler(req: NextApiRequest, res: NextApiResponse) {
    res.status(200).json([{ id: 1, name: 'John' }]);
}

// pages/users.tsx
export async function getServerSideProps() {
    const res = await fetch('http://localhost:3000/api/users');
    const users = await res.json();
    return { props: { users } };
}
```

## 📋 When to Use
- ✅ SEO-critical React applications
- ✅ Need SSR or static generation
- ❌ Not for simple SPAs without SSR

## 🔧 Step-by-Step Instructions
1. Create project: `npx create-next-app@latest`
2. Create pages in `pages/` or `app/`
3. Add API routes in `pages/api/`
4. Run: `npm run dev`

## 📦 Dependencies
```bash
npx create-next-app@latest
```

## 🧪 Examples
Input: `GET /users` → SSR page with user list

## 🔗 Resources
- [Next.js Docs](https://nextjs.org/docs)
- [Examples](./examples/)

## ✅ Validation
1. Pages generate correctly on server
2. API routes respond properly
3. SEO metadata present
