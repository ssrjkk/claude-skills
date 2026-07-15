---
name: mongodb
description: "Models data and builds queries with MongoDB aggregation pipelines and indexes. Use for flexible document-based storage."
category: database
tags: [mongodb, nosql, database, document, aggregation]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# MongoDB

> Document database design, aggregation pipelines, and indexing.

## Quick Start
```javascript
// Connect and query
const { MongoClient } = require('mongodb');
const client = new MongoClient('mongodb://localhost:27017');
await client.connect();

const db = client.db('shop');
const users = db.collection('users');

// Insert
await users.insertOne({ name: 'Alice', email: 'alice@example.com' });

// Aggregation pipeline
const result = await users.aggregate([
  { $match: { active: true } },
  { $group: { _id: '$role', count: { $sum: 1 } } }
]).toArray();
```

## When to Use
- ✅ Flexible/unstructured data
- ✅ Rapid prototyping with changing schema
- ❌ Not for complex transactions (better PostgreSQL)

## Step-by-Step Instructions
1. Install: `npm install mongodb` or use Compass GUI
2. Connect to local or Atlas cluster
3. Design documents and indexes
4. Write aggregation pipelines

## Dependencies
```bash
npm install mongodb mongoose
# MongoDB Atlas: https://www.mongodb.com/atlas
```

## Examples
Input: `users.aggregate([{ $group: { _id: "$city" } }])` → Output: List of unique cities

## Resources
- [MongoDB Docs](https://www.mongodb.com/docs/)
- [Examples](./examples/)

## Validation
1. Connection established
2. CRUD operations work
3. Indexes improve query performance
