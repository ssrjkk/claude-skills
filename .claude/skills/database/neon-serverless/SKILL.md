---
name: neon-serverless
description: Neon serverless PostgreSQL
category: database
tags: [neon, postgresql, serverless, database, edge]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Neon Serverless

> Build with Neon — the serverless PostgreSQL with branching, autoscaling, and edge-ready architecture.

## Quick Start
```typescript
import { neon } from '@neondatabase/serverless';
import { drizzle } from 'drizzle-orm/neon-http';
import { pgTable, serial, text, timestamp } from 'drizzle-orm/pg-core';

// 1. Direct SQL with edge-ready driver
const sql = neon(process.env.DATABASE_URL!);

async function getUsers() {
  const { rows } = await sql`SELECT * FROM users WHERE active = true`;
  return rows;
}

// 2. ORM with Drizzle
const users = pgTable('users', {
  id: serial('id').primaryKey(),
  name: text('name').notNull(),
  email: text('email').notNull().unique(),
  createdAt: timestamp('created_at').defaultNow(),
});

const db = drizzle(sql);

async function createUser(name: string, email: string) {
  const [user] = await db.insert(users).values({ name, email }).returning();
  return user;
}

// 3. Neon branching for preview environments
/*
# Create a branch for each PR
neon branch create --name pr-$PR_NUMBER --parent main

# Deploy with branch-specific connection string
DATABASE_URL=postgres://user:pass@pr-$PR_NUMBER.cloud.neon.tech/db

# Auto-suspend after inactivity (pay only for active time)
*/

// 4. Connection pooling with PgBouncer
const poolSql = neon(process.env.DATABASE_URL!, {
  pool: true, // Transaction mode for prepared statements
  maxConnections: 10,
});

// 5. AI integration — pgvector
async function searchSimilar(embedding: number[], threshold = 0.8) {
  const result = await sql`
    SELECT id, content, 1 - (embedding <=> ${JSON.stringify(embedding)}::vector) as similarity
    FROM documents
    WHERE 1 - (embedding <=> ${JSON.stringify(embedding)}::vector) > ${threshold}
    ORDER BY similarity DESC
    LIMIT 10
  `;
  return result;
}
```

## Key Concepts
Neon separates storage from compute. Databases auto-suspend when idle and scale from 0 to full capacity. Branches enable instant DB cloning for development. Supports pgvector for AI embeddings.

## When to Use
- Serverless applications needing PostgreSQL
- Preview environments needing isolated databases per branch
- Applications with variable traffic patterns
- AI applications needing pgvector for similarity search

## Validation
1. `sql` tag function executes queries without errors
2. Connection pooling works in serverless environments
3. Database branch creates instantly and is accessible
4. pgvector extension is enabled and similarity search works
