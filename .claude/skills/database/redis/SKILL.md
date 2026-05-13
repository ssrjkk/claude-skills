---
name: redis
description: Implements caching, session storage, and pub/sub messaging with Redis. Use for high-performance in-memory data.
category: database
tags: [redis, cache, pubsub, session, database]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Redis

> In-memory data store for caching, sessions, and real-time messaging.

## Quick Start
```javascript
import Redis from 'ioredis';

const redis = new Redis();

// Caching
await redis.set('user:1', JSON.stringify({ name: 'Alice' }), 'EX', 3600);
const user = JSON.parse(await redis.get('user:1'));

// Pub/Sub
const pub = new Redis();
const sub = new Redis();
sub.subscribe('notifications', (err, count) => {});
sub.on('message', (channel, message) => {
  console.log(`Received: ${message}`);
});
pub.publish('notifications', 'Hello subscribers!');
```

## When to Use
- ✅ Application caching layer
- ✅ Session storage for web apps
- ❌ Not for persistent primary storage

## Step-by-Step Instructions
1. Install Redis: `docker run -p 6379:6379 redis`
2. Install client: `npm install ioredis`
3. Connect and use data structures (strings, lists, sets, sorted sets)
4. Set TTL for cache keys

## Dependencies
```bash
docker run -d -p 6379:6379 redis
npm install ioredis
```

## Examples
Input: `redis.set('key', 'value', 'EX', 60)` → Output: Cached for 60 seconds

## Resources
- [Redis Docs](https://redis.io/docs/)
- [Examples](./examples/)

## Validation
1. Redis responds to ping: `redis.ping()`
2. Keys expire correctly
3. Pub/sub delivers messages
