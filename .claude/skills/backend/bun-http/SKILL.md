---
name: bun-http
description: Bun HTTP server and routing
category: backend
tags: [bun, http, server, routing, web]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Bun HTTP

> Build fast HTTP servers and APIs using Bun's built-in server and routing capabilities.

## Quick Start
```typescript
import { Hono } from "hono"; // or use Bun.serve directly
import { cors } from "hono/cors";

// Option 1: Bun.serve (minimal)
Bun.serve({
  port: 3000,
  async fetch(request: Request) {
    const url = new URL(request.url);
    
    if (url.pathname === "/api/users" && request.method === "GET") {
      const users = await Bun.sql`SELECT * FROM users`;
      return Response.json(users);
    }
    
    if (url.pathname.startsWith("/api/users/") && request.method === "GET") {
      const id = url.pathname.split("/").pop();
      const user = await Bun.sql`SELECT * FROM users WHERE id = ${id}`;
      return user ? Response.json(user[0]) : new Response("Not found", { status: 404 });
    }

    // Static files
    return new Response(Bun.file(`./public${url.pathname}`));
  },
});

// Option 2: Hono on Bun (full-featured)
const app = new Hono();

app.use("/api/*", cors());
app.get("/api/users", async (c) => {
  const users = await Bun.sql`SELECT * FROM users`;
  return c.json(users);
});

app.post("/api/users", async (c) => {
  const body = await c.req.json();
  const result = await Bun.sql`
    INSERT INTO users (name, email) 
    VALUES (${body.name}, ${body.email}) 
    RETURNING *
  `;
  return c.json(result[0], 201);
});

app.get("/api/users/:id", async (c) => {
  const user = await Bun.sql`SELECT * FROM users WHERE id = ${c.req.param("id")}`;
  return user[0] ? c.json(user[0]) : c.text("Not found", 404);
});

export default app;
```

## Key Concepts
Bun.serve provides a fast HTTP server with WebSocket support. Bun.sql offers built-in SQLite querying. Hono on Bun gives you routing, middleware, and validation. Bun handles 10x more requests/second than Node.js equivalents.

## When to Use
- High-performance API servers
- Real-time applications with WebSocket
- Full-stack applications with built-in SQLite
- Microservices needing fast startup times

## Validation
1. Server starts and responds to HTTP requests
2. Routes handle GET, POST, PUT, DELETE correctly
3. Bun.sql queries return correct results
4. Static file serving works for assets
