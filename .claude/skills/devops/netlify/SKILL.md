---
name: netlify
description: "Deploys static sites and serverless functions with Netlify, including forms, identity, and split testing."
category: devops
tags: [netlify, deployment, static-site, jamstack, serverless]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Netlify

> All-in-one platform for static sites and serverless functions.

## Quick Start
```bash
npm install -g netlify-cli
netlify deploy --prod
```

## Functions
```javascript
// netlify/functions/hello.js
exports.handler = async (event, context) => ({
  statusCode: 200,
  body: JSON.stringify({ message: 'Hello from Netlify!' })
})
```

## Redirects (_redirects)
```
/api/*    https://api.example.com/:splat   200
/blog/*   /blog/:splat
/*        /index.html                       200
```

## When to Use
- Static site hosting
- JAMstack architectures
- Form handling without backend
- Branch-based previews

## Validation
1. Deploy succeeds via CLI or Git
2. Functions respond correctly
3. Redirects work as configured
