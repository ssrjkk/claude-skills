---
name: strapi
description: Creates headless CMS backends with Strapi, content types, roles, and REST/GraphQL APIs. Use for rapid content management.
category: backend
tags: [strapi, cms, headless, api, content]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Strapi

> Open-source headless CMS with auto-generated APIs.

## Quick Start
```bash
npx create-strapi-app my-project --quickstart
# Admin UI at http://localhost:1337/admin
```

## Content Types
```json
{
  "kind": "collectionType",
  "attributes": {
    "title": { "type": "string", "required": true },
    "body": { "type": "richtext" },
    "author": { "type": "relation", "relation": "manyToOne", "target": "api::author.author" }
  }
}
```

## Custom Controllers
```javascript
// src/api/article/controllers/article.js
module.exports = createCoreController('api::article.article', ({ strapi }) => ({
  async popular(ctx) {
    const articles = await strapi.db.query('api::article.article').findMany({
      where: { views: { $gte: 1000 } },
      orderBy: { views: 'desc' }
    })
    return this.transformResponse(articles)
  }
}))
```

## When to Use
- Content-driven websites
- Mobile app backends
- Blog/News platforms
- Multi-channel content delivery

## Validation
1. Admin panel loads at /admin
2. Content types created and API responds
3. Role-based permissions work correctly
