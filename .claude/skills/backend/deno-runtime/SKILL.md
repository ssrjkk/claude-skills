---
name: deno-runtime
description: Deno runtime and standard library
category: backend
tags: [deno, runtime, typescript, javascript, secure]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Deno Runtime

> Build secure TypeScript-first applications with Deno runtime and its extensive standard library.

## Quick Start
```typescript
// deno serve — modern HTTP server
import { Hono } from "jsr:@hono/hono";
import { cors } from "jsr:@hono/hono/cors";
import { Database } from "jsr:@db/sqlite";

const db = new Database("app.db");
db.run(`CREATE TABLE IF NOT EXISTS todos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  completed BOOLEAN DEFAULT FALSE
)`);

const app = new Hono();

app.use("/api/*", cors());

app.get("/api/todos", (c) => {
  const todos = db.query("SELECT * FROM todos").map(([id, title, completed]) => ({
    id, title, completed: !!completed
  }));
  return c.json(todos);
});

app.post("/api/todos", async (c) => {
  const { title } = await c.req.json();
  db.run("INSERT INTO todos (title) VALUES (?)", [title]);
  return c.json({ success: true }, 201);
});

app.patch("/api/todos/:id", async (c) => {
  const id = c.req.param("id");
  const { completed } = await c.req.json();
  db.run("UPDATE todos SET completed = ? WHERE id = ?", [completed ? 1 : 0, id]);
  return c.json({ success: true });
});

app.delete("/api/todos/:id", (c) => {
  db.run("DELETE FROM todos WHERE id = ?", [c.req.param("id")]);
  return c.json({ success: true });
});

// Deno.serve is built-in (no external server needed)
Deno.serve({ port: 3000 }, app.fetch);
```

```bash
# Run (permissions required explicitly)
deno run --allow-net --allow-read --allow-write --allow-env server.ts

# Or just use --allow-all for development
deno run -A server.ts

# Format code
deno fmt

# Lint
deno lint

# Compile to standalone binary
deno compile -A -o app-server server.ts
```

## Key Concepts
Deno is secure by default — no file/network/env access without explicit flags. Uses web standard APIs (fetch, Request, Response). Built-in formatter, linter, test runner, and compiler. Import from URLs or JSR.

## When to Use
- Building secure applications with Principle of Least Privilege
- TypeScript-first projects without configuration
- CLI tools (deno compile creates standalone binaries)
- Applications wanting web standard APIs

## Validation
1. `deno run` works with explicit permission flags
2. Deno standard library functions work correctly
3. `deno compile` produces a working standalone binary
4. HTTP server responds correctly with proper permissions
