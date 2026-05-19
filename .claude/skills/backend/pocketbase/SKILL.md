---
name: pocketbase
description: Deploys backend-as-a-service with PocketBase, including embedded SQLite, auth, file storage, and real-time subscriptions. Use for rapid prototyping.
category: backend
tags: [pocketbase, bas, sqlite, auth, realtime]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# PocketBase

> Lightweight backend with embedded database, auth, file storage, and admin UI.

## Quick Start
```bash
# Download from pocketbase.io
./pocketbase serve
# Admin UI at http://localhost:8090/_/
```

## Collections & API
```javascript
const pb = new PocketBase('http://localhost:8090')
await pb.admins.authWithPassword('admin@example.com', 'password')
const collection = await pb.collections.create({
  name: 'posts',
  schema: [{ name: 'title', type: 'text', required: true }, { name: 'body', type: 'editor' }, { name: 'published', type: 'bool' }]
})
const record = await pb.collection('posts').create({ title: 'Hello World', body: 'First post', published: true })
```

## Auth Rules
Configure API rules in Admin UI per collection (create, read, update, delete, list).
Use `@request.auth.id != ""` for authenticated users, empty for public.

## When to Use
- Prototypes and MVPs
- Side projects and hackathons
- Small to medium apps
- Embedded database needs

## Validation
1. Admin UI accessible at port 8090
2. Collections created and API responds
3. Auth (email, OAuth2) works correctly
