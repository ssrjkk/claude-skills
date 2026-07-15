---
name: mcp-resources
description: "MCP resource providers and patterns"
category: ai
tags: [mcp, resources, data, providers, content]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# MCP Resources

> Expose structured data and content to Claude through MCP resource providers.

## Quick Start
```python
from mcp.server import Server, stdio_server
from mcp.types import Resource, ResourceTemplate, TextResourceContents

@stdio_server()
class DocServer(Server):
    async def list_resources(self) -> list[Resource]:
        return [
            Resource(
                uri="docs://README",
                name="Project README",
                mimeType="text/markdown"
            )
        ]

    async def list_resource_templates(self) -> list[ResourceTemplate]:
        return [
            ResourceTemplate(
                uriTemplate="docs://{path}",
                name="Documentation by path",
                mimeType="text/markdown"
            )
        ]

    async def read_resource(self, uri: str) -> TextResourceContents:
        path = uri.split("://")[1]
        content = read_doc_file(f"{path}.md")
        return TextResourceContents(
            uri=uri,
            mimeType="text/markdown",
            text=content
        )
```

## Key Concepts
Resources are URI-addressable data that Claude can read. Use resource templates for dynamic paths. Common patterns: file access, API responses, database queries, documentation.

## When to Use
- Providing reference documentation for Claude to consult
- Giving Claude read-only access to project files or databases
- Building knowledge bases that Claude can query contextually

## Validation
1. Resources list returns valid URIs and metadata
2. Template URIs match with parameter extraction
3. Read returns content with correct MIME type and encoding
