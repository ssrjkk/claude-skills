---
name: bun-runtime
description: "Bun runtime for JavaScript/TypeScript"
category: frontend
tags: [bun, javascript, typescript, runtime, bundler]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Bun Runtime

> Build and run JavaScript/TypeScript applications with Bun — the all-in-one toolkit.

## Quick Start
```bash
# Install Bun
powershell -c "irm bun.sh/install.ps1 | iex"

# Create a new project
bun init

# Run TypeScript directly (no ts-node needed)
bun run server.ts

# Package scripts (3-5x faster than npm)
bun install
bun add express
bun add -d typescript

# Run package.json scripts
bun run dev
bun run build

# Test runner (Jest-compatible)
bun test

# Bun's built-in bundler
bun build ./src/index.ts --outdir=./dist
```

```typescript
// bun自带 features

// Fetch API (built-in, no polyfill needed)
const response = await fetch("https://api.example.com/data");
const data = await response.json();

// SQLite (built-in)
import { Database } from "bun:sqlite";
const db = new Database(":memory:");
db.run("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)");
db.run("INSERT INTO users (name) VALUES ($name)", { name: "Alice" });
const users = db.query("SELECT * FROM users").all();

// File I/O (Bun native)
const file = Bun.file("data.json");
const contents = await file.json();

// Environment variables (built-in)
const apiKey = Bun.env.API_KEY;

// WebSocket server
Bun.serve({
  port: 3000,
  fetch(req, server) {
    if (server.upgrade(req)) return; // upgrade to WebSocket
    return new Response("Hello");
  },
  websocket: {
    message(ws, message) {
      ws.send(`Echo: ${message}`);
    }
  }
});
```

## Key Concepts
Bun is a JavaScript runtime, bundler, test runner, and package manager in one. Uses JavaScriptCore (not V8), starts faster than Node.js, and is fully compatible with Node.js APIs.

## When to Use
- New TypeScript/JavaScript projects
- CI/CD pipelines needing faster installs and builds
- Development servers requiring hot reload
- Projects wanting built-in SQLite, fetch, and WebSocket support

## Validation
1. `bun --version` shows installed version
2. `bun run` executes TypeScript without compilation step
3. `bun install` is faster than npm/pnpm on the same project
4. `bun test` runs existing Jest/Vitest test suites
