---
name: hono
description: "Creates lightweight, fast web APIs with Hono, supporting Cloudflare Workers, Deno, Bun, and Node.js. Use for edge-compatible APIs."
category: backend
tags: [hono, edge, cloudflare, workers, typescript]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Hono

> Ultralight web framework for edge runtimes (Cloudflare Workers, Deno, Bun).

## Quick Start
```typescript
import { Hono } from 'hono'
const app = new Hono()
app.get('/', (c) => c.text('Hello Hono!'))
app.get('/api/users/:id', (c) => c.json({ id: c.req.param('id'), name: 'Alice' }))
export default app
```

## Middleware
```typescript
import { cors } from 'hono/cors'
import { jwt } from 'hono/jwt'
app.use('/api/*', cors())
app.use('/api/admin/*', jwt({ secret: 'my-secret-key' }))
app.onError((err, c) => c.json({ error: err.message }, 500))
```

## When to Use
- Cloudflare Workers APIs
- Edge computing applications
- Multi-runtime deployments
- Minimal bundle size requirements

## Validation
1. Server responds on all target runtimes
2. Middleware chain executes correctly
3. Edge deployment succeeds
