---
name: vercel
description: "Deploys frontend applications with Vercel, including serverless functions, preview deployments, and edge functions."
category: devops
tags: [vercel, deployment, serverless, frontend, edge]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Vercel

> Frontend deployment platform with serverless functions and edge compute.

## Quick Start
```bash
npm install -g vercel
vercel deploy
```

## Serverless Functions
```typescript
// api/users.ts
import type { VercelRequest, VercelResponse } from '@vercel/node'
export default function handler(req: VercelRequest, res: VercelResponse) {
  res.json({ users: [{ id: 1, name: 'Alice' }] })
}
```

## Edge Middleware
```typescript
// middleware.ts
export default function middleware(request: Request) {
  const country = request.headers.get('x-vercel-ip-country')
  return new Response(`Hello from ${country}`, { headers: { 'x-edge': 'true' } })
}
export const config = { matcher: '/api/edge' }
```

## When to Use
- Frontend deployments
- Next.js applications
- Preview deployments per branch
- Edge computing needs

## Validation
1. Deploy succeeds with zero errors
2. Preview URL works correctly
3. Serverless functions respond
