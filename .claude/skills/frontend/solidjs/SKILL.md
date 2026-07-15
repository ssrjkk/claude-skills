---
name: solidjs
description: "Creates reactive UIs with SolidJS, signals, and fine-grained reactivity. Use for high-performance web applications."
category: frontend
tags: [solidjs, javascript, reactivity, signals, frontend]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# SolidJS

> Reactive JavaScript library for performant UIs.

## Quick Start
```jsx
import { createSignal } from "solid-js";

function Counter() {
  const [count, setCount] = createSignal(0);
  
  return (
    <button onClick={() => setCount(c => c + 1)}>
      Count: {count()}
    </button>
  );
}
```

## When to Use
- ✅ High-performance reactive UIs
- ✅ Lightweight alternative to React
- ❌ Not for enterprise apps needing ecosystem (better React)

## Step-by-Step Instructions
1. Create project: `npx degit solidjs/templates/js my-app`
2. Create components with signals
3. Use For/Show control flow
4. Build: `npm run build`

## Dependencies
```bash
npm init solid@latest
```

## Examples
Input: `createSignal(0)` → Output: Reactive counter component

## Resources
- [SolidJS Docs](https://www.solidjs.com/docs/latest)
- [Examples](./examples/)

## Validation
1. App renders without errors
2. Reactivity updates correctly
3. Build produces optimized output
