---
name: fastify
description: Builds fast and low-overhead Node.js web APIs with Fastify, schema validation, and plugins. Use for high-performance Node.js backends.
category: backend
tags: [fastify, nodejs, api, performance, validation]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Fastify

> Fast and low-overhead Node.js web framework with schema validation.

## Quick Start
```javascript
import Fastify from 'fastify'
const app = Fastify({ logger: true })
app.get('/health', async () => ({ status: 'ok' }))
await app.listen({ port: 3000 })
```

## Schema Validation
```javascript
app.post('/users', {
  schema: {
    body: { type: 'object', properties: { name: { type: 'string' }, email: { type: 'string' } }, required: ['name', 'email'] }
  }
}, async (req, reply) => ({ id: 1, ...req.body }))
```

## Plugins
```javascript
import cors from '@fastify/cors'
import jwt from '@fastify/jwt'
await app.register(cors, { origin: '*' })
await app.register(jwt, { secret: process.env.JWT_SECRET })
app.decorate('authenticate', async (req, reply) => { await req.jwtVerify() })
```

## When to Use
- High-throughput APIs
- JSON schema validated endpoints
- Plugin-based architecture
- Drop-in Express replacement

## Validation
1. Server starts with logging
2. Schema validation rejects invalid input
3. Plugins register without errors
