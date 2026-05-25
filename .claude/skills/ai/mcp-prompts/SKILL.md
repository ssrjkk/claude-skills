---
name: mcp-prompts
description: MCP prompt templates and management
category: ai
tags: [mcp, prompts, templates, management, llm]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# MCP Prompts

> Create and manage reusable prompt templates via the Model Context Protocol.

## Quick Start
```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";

const server = new Server(
  { name: "prompt-server", version: "1.0.0" },
  { capabilities: { prompts: {} } }
);

server.setRequestHandler("prompts/list", async () => ({
  prompts: [{
    name: "code-review",
    description: "Review code changes",
    arguments: [
      { name: "language", description: "Programming language", required: true },
      { name: "diff", description: "Code diff to review", required: true }
    ]
  }]
}));

server.setRequestHandler("prompts/get", async (request) => {
  const { name, arguments: args } = request.params;
  if (name === "code-review") {
    return {
      messages: [
        {
          role: "system",
          content: { type: "text", text: `You are a ${args.language} expert. Review the following diff for bugs, security issues, and style problems.` }
        },
        {
          role: "user",
          content: { type: "text", text: `Review this diff:\n\n\`\`\`diff\n${args.diff}\n\`\`\`` }
        }
      ]
    };
  }
});
```

## Key Concepts
Prompts are reusable message templates with typed arguments. They let Claude use structured, pre-defined prompts for consistent interactions.

## When to Use
- Standardizing code review, debugging, or analysis workflows
- Providing domain-specific prompt templates
- Building multi-step prompting sequences

## Validation
1. Prompt list returns correct names and argument schemas
2. Prompt get with valid args returns properly formatted messages
3. Prompt get with missing required args returns error
