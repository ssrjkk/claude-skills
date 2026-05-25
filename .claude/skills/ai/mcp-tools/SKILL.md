---
name: mcp-tools
description: Creating custom MCP tools for Claude
category: ai
tags: [mcp, tools, custom, integration, python, typescript]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# MCP Tools

> Design and implement powerful custom tools for Claude to interact with your systems.

## Quick Start
```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";

const server = new Server(
  { name: "github-tools", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

server.setRequestHandler("tools/list", async () => ({
  tools: [{
    name: "search_repos",
    description: "Search GitHub repositories",
    inputSchema: {
      type: "object",
      properties: {
        query: { type: "string", description: "Search query" },
        limit: { type: "number", default: 10 }
      },
      required: ["query"]
    }
  }]
}));

server.setRequestHandler("tools/call", async (request) => {
  const { name, arguments: args } = request.params;
  if (name === "search_repos") {
    const res = await fetch(`https://api.github.com/search/repositories?q=${args.query}&per_page=${args.limit}`);
    const data = await res.json();
    return { content: [{ type: "text", text: JSON.stringify(data.items) }] };
  }
  throw new Error(`Unknown tool: ${name}`);
});
```

## Key Concepts
Each tool needs a name, description, and JSON Schema input definition. Tool descriptions are critical — Claude uses them to decide which tool to invoke. Return content as typed content blocks.

## When to Use
- Exposing CRUD operations on your database or API
- Providing search, analysis, or computation capabilities
- Building domain-specific toolkits (finance,医疗, engineering)

## Validation
1. Tool schema is valid JSON Schema and tools appear in listing
2. Required parameters enforce correctly — missing params rejected
3. Error responses are informative and don't crash the server
