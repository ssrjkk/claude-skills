---
name: gatsby
description: Builds blazing-fast static sites and progressive web apps with Gatsby, React, and GraphQL. Use for content-driven sites and documentation.
category: frontend
tags: [gatsby, react, graphql, static-site, pwa]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Gatsby

> React-based static site generator with GraphQL data layer.

## Quick Start
```bash
npm init gatsby
cd my-site
npm run develop
```

## When to Use
- Blogs and marketing sites
- Documentation portals
- E-commerce storefronts
- Portfolio websites

## Step-by-Step
1. Create site: `npm init gatsby`
2. Add plugins for data sources
3. Query data with GraphQL
4. Build: `npm run build`

## Dependencies
```bash
npm install gatsby react react-dom
```

## Examples
```jsx
import { graphql, useStaticQuery } from "gatsby"

export default function Home() {
  const data = useStaticQuery(graphql`
    query { site { siteMetadata { title } } }
  `)
  return <h1>{data.site.siteMetadata.title}</h1>
}
```

## Resources
- [Gatsby Docs](https://www.gatsbyjs.com/docs)

## Validation
1. Dev server runs on port 8000
2. Build completes without errors
3. Pages render from GraphQL data
