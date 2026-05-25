---
name: mcp-server
description: Model Context Protocol server implementation in Python/TypeScript
category: ai
tags: [mcp, protocol, ai, integration, python, typescript]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# MCP Server

> Build Model Context Protocol servers to connect Claude with external tools and data sources.

## Quick Start
```python
from mcp.server import Server, stdio_server
from mcp.types import TextContent, Tool

@stdio_server()
class MyServer(Server):
    async def list_tools(self) -> list[Tool]:
        return [
            Tool(
                name="calculator",
                description="Perform arithmetic",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "expr": {"type": "string"}
                    }
                }
            )
        ]

    async def call_tool(self, name: str, args: dict) -> list[TextContent]:
        if name == "calculator":
            result = eval(args["expr"])
            return [TextContent(type="text", text=str(result))]
```

## Key Concepts
MCP servers expose tools, resources, and prompts to AI clients via a standardized JSON-RPC protocol. Servers run as subprocesses and communicate over stdio or SSE.

## When to Use
- Exposing internal APIs to Claude for agentic workflows
- Building custom tool integrations for domain-specific tasks
- Creating read-only resource providers (files, databases, APIs)

## Validation
1. Server starts and responds to `initialize` handshake
2. Tools appear in Claude's tool listing and execute correctly
3. Resources are discoverable and return valid content
