---
name: mcp-client
description: MCP client integration for Claude
category: ai
tags: [mcp, client, integration, claude, protocol]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# MCP Client

> Connect Claude to any MCP-compatible server for extended capabilities.

## Quick Start
```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["my-server.js"]
});

const client = new Client({
  name: "my-client",
  version: "1.0.0"
});

await client.connect(transport);

// List available tools
const tools = await client.listTools();
console.log(tools);

// Call a tool
const result = await client.callTool({
  name: "calculator",
  arguments: { expr: "2 + 2" }
});
```

## Key Concepts
MCP clients connect to servers over stdio or SSE, discover available tools/resources, and invoke them. The SDK handles transport, JSON-RPC messaging, and capability negotiation.

## When to Use
- Embedding Claude in custom applications with extended tool access
- Building multi-server orchestration layers
- Creating proxy servers that aggregate multiple MCP servers

## Validation
1. Client successfully initializes connection
2. Tool listing returns expected tools
3. Tool calls return correct results with proper error handling
