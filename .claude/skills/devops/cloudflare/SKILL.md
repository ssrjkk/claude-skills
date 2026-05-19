---
name: cloudflare
description: Configures Cloudflare for CDN, DNS, Workers, D1, R2, and Durable Objects. Use for edge computing and site acceleration.
category: devops
tags: [cloudflare, cdn, workers, dns, edge]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Cloudflare

> Edge network platform for CDN, DNS, Workers, and storage.

## Quick Start (Worker)
```typescript
export default { async fetch(request): Promise<Response> {
  const url = new URL(request.url)
  if (url.pathname === '/api/hello') {
    return new Response(JSON.stringify({ message: 'Hello from edge!' }), { headers: { 'Content-Type': 'application/json' } })
  }
  return fetch(request)
}}
```

## D1 Database
```typescript
export default { async fetch(request, env) {
  const { results } = await env.DB.prepare('SELECT * FROM users WHERE id = ?').bind(1).all()
  return Response.json(results)
}}
```

## R2 Storage
```typescript
await env.MY_BUCKET.put('file.txt', 'Hello World')
const object = await env.MY_BUCKET.get('file.txt')
```

## When to Use
- Global CDN and caching
- Edge compute applications
- DNS management
- DDoS protection

## Validation
1. DNS resolves through Cloudflare
2. Workers deploy and respond
3. Cache headers respected correctly
