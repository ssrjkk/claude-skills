---
name: graphql-api
description: "Designs and implements GraphQL APIs with Apollo Server (Node.js). Use for flexible, type-safe API layers."
category: backend
tags: [graphql, apollo, nodejs, typescript, api]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# GraphQL API

> Build flexible, type-safe GraphQL APIs with Apollo Server.

## Quick Start
```typescript
import { ApolloServer } from '@apollo/server';
import { startStandaloneServer } from '@apollo/server/standalone';

const typeDefs = `#graphql
  type Query {
    hello: String
  }`;

const resolvers = { Query: { hello: () => 'Hello world' } };

const server = new ApolloServer({ typeDefs, resolvers });
const { url } = await startStandaloneServer(server, { listen: { port: 4000 } });
console.log(`Server ready at ${url}`);
```

## When to Use
- ✅ Flexible APIs with custom queries
- ✅ Multiple data sources (REST, DB, gRPC)
- ❌ Not for simple CRUD (better REST)

## Step-by-Step Instructions
1. Install: `npm install @apollo/server graphql`
2. Define schema with typeDefs
3. Write resolvers
4. Run: `npx ts-node index.ts`

## Dependencies
```bash
npm install @apollo/server graphql
```

## Examples
Input: `{ users { id name } }` → Output: JSON with user data

## Resources
- [Apollo Server Docs](https://www.apollographql.com/docs/apollo-server/)
- [Examples](./examples/)

## Validation
1. Server starts on port 4000
2. GraphQL Playground accessible
3. Queries return expected data
