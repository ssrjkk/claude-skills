---
name: docusaurus
description: Creates documentation websites with Docusaurus, MDX, versioning, and search. Use for open-source docs and knowledge bases.
category: frontend
tags: [docusaurus, docs, mdx, documentation, static-site]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Docusaurus

> Build optimized documentation websites with React and MDX.

## Quick Start
```bash
npx create-docusaurus@latest my-docs classic
cd my-docs && npm start
```

## Sidebar Configuration
```javascript
module.exports = { tutorialSidebar: ['intro', { type: 'category', label: 'Getting Started', items: ['installation', 'quickstart'] }] }
```

## MDX Features
```mdx
import Tabs from '@theme/Tabs'; import TabItem from '@theme/TabItem'
<Tabs><TabItem value="npm" label="npm">npm install</TabItem><TabItem value="yarn" label="yarn">yarn add</TabItem></Tabs>
```

## When to Use
- Open-source project documentation
- API reference sites
- Internal knowledge bases
- Product documentation portals

## Validation
1. Dev server starts on port 3000
2. Search indexes content correctly
3. Versioning works with multiple docs versions
