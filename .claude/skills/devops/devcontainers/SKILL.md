---
name: devcontainers
description: "Development containers with Dev Container spec"
category: devops
tags: [devcontainers, docker, development, environment, vscode]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Dev Containers

> Create reproducible development environments using the Dev Container specification.

## Quick Start
```json
// .devcontainer/devcontainer.json
{
  "name": "Python Data Science",
  "image": "mcr.microsoft.com/devcontainers/python:3.12",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.12"
    },
    "ghcr.io/devcontainers/features/docker-in-docker:2": {},
    "ghcr.io/devcontainers/features/git:1": {}
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.black-formatter",
        "ms-toolsai.jupyter",
        "GitHub.copilot"
      ],
      "settings": {
        "python.defaultInterpreterPath": "/usr/local/bin/python",
        "python.testing.pytestEnabled": true
      }
    }
  },
  "postCreateCommand": "pip install -r requirements.txt",
  "forwardPorts": [8000, 8501],
  "remoteUser": "vscode"
}
```

```dockerfile
# .devcontainer/Dockerfile — custom image
FROM mcr.microsoft.com/devcontainers/python:3.12
RUN apt-get update && apt-get install -y postgresql-client
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt
```

## Key Concepts
Dev containers define a complete development environment as code. Includes OS, tools, extensions, and configuration. Works with VS Code, GitHub Codespaces, and JetBrains. Ensures "works on my machine" becomes "works on every machine."

## When to Use
- Onboarding new team members (zero setup time)
- Open-source projects (consistent contributor environments)
- teams with mixed OS environments
- CI/CD parity with local development

## Validation
1. `devcontainer build` completes without errors
2. Container starts and VS Code attaches successfully
3. All specified extensions and tools are available
4. postCreateCommand runs and project builds successfully
