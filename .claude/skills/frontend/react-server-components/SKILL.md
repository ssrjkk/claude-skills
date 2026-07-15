---
name: react-server-components
description: "React Server Components and SSR"
category: frontend
tags: [react, server-components, ssr, nextjs, rsc]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# React Server Components

> Master React Server Components for efficient server-side rendering and data fetching.

## Quick Start
```tsx
// Server Component (can be async, fetches data directly)
// app/products/page.tsx — Next.js App Router
export default async function ProductsPage() {
  const products = await db.product.findMany({
    orderBy: { createdAt: 'desc' },
    take: 20,
  });

  return (
    <div>
      <h1>Products</h1>
      {/* Client component with interactivity */}
      <SearchBar />
      <div className="grid grid-cols-3 gap-4">
        {products.map((product) => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </div>
  );
}

// Client Component (interactive)
'use client';

import { useState } from 'react';

export function SearchBar() {
  const [query, setQuery] = useState('');
  
  return (
    <input
      value={query}
      onChange={(e) => setQuery(e.target.value)}
      placeholder="Search products..."
      className="border p-2 rounded"
    />
  );
}

// Server Component with async data
// app/products/[id]/page.tsx
export default async function ProductPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  const product = await db.product.findUnique({ where: { id } });

  if (!product) return <div>Product not found</div>;

  return (
    <div>
      <h1>{product.name}</h1>
      <p>{product.description}</p>
      <p className="text-lg font-bold">${product.price}</p>
      <AddToCartButton productId={product.id} />
    </div>
  );
}
```

## Key Concepts
Server Components render on the server, reducing client JS bundle. They can be async and access databases/files directly. `'use client'` boundary marks client components. Streaming enables progressive rendering.

## When to Use
- Data-heavy pages (dashboards, product listings)
- SEO-critical content (landing pages, blogs)
- Reducing client-side JavaScript bundle size

## Validation
1. Server components render data without client-side fetching
2. Client boundary correctly surrounds interactive elements
3. Streaming sends early UI before async data resolves
4. Bundle size shows minimal client JS for server components
