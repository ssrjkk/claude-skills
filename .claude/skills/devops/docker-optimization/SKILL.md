---
name: docker-optimization
description: "Optimizes Docker images with multi-stage builds, layer caching, and size reduction. Use for CI/CD acceleration and disk savings."
category: devops
tags: [docker, optimization, multi-stage, caching]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Docker Optimization

> Create minimal, secure, and fast Docker images.

## 🚀 Quick Start
```dockerfile
# Multi-stage build
FROM node:alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
```

## 📋 When to Use
- ✅ Need to reduce image size
- ✅ Speed up CI/CD with caching
- ❌ Not for simple single-file scripts

## 🔧 Step-by-Step Instructions
1. Use multi-stage builds (builder + runtime)
2. Order COPY/RUN for layer caching
3. Use .dockerignore to exclude unnecessary files
4. Build: `docker build -t myapp:optimized .`

## 📦 Dependencies
```bash
# Install Docker
# Windows: https://docs.docker.com/desktop/install/windows-install/
# Mac: https://docs.docker.com/desktop/install/mac-install/
# Linux: https://docs.docker.com/engine/install/
```

## 🧪 Examples
Input: `docker build -t myapp .` with optimized Dockerfile
Output: Image size < 50MB instead of > 500MB

## 🔗 Resources
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Examples](./examples/)

## ✅ Validation
1. Image size reduced by at least 50%
2. Container starts and works correctly
3. No source code or dev dependencies in image
