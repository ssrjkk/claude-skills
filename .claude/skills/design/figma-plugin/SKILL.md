---
name: figma-plugin
description: Develops Figma plugins using TypeScript and Figma Plugin API. Use for automating design processes.
category: design
tags: [figma, plugin, typescript, design, automation]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# Figma Plugin

> Create plugins for Figma using TypeScript.

## Quick Start
```typescript
figma.showUI(__html__, { width: 300, height: 200 });

figma.ui.onmessage = async (msg) => {
    if (msg.type === 'create-rect') {
        const rect = figma.createRectangle();
        rect.x = 100;
        figma.currentPage.appendChild(rect);
    }
};
```

## When to Use
- ✅ Automate tasks in Figma
- ✅ Programmatically create design tokens
- ❌ Not for website development

## Step-by-Step Instructions
1. Create plugin: `npx create-figma-plugin`
2. Write logic in `src/plugin.ts`
3. Create UI in `src/ui.tsx`
4. Test in Figma (Plugins → Development)

## Dependencies
```bash
npx create-figma-plugin
```

## Examples
Input: Run plugin → Output: Rectangle created in Figma

## Resources
- [Figma Plugin API](https://www.figma.com/plugin-docs/)
- [Examples](./examples/)

## Validation
1. Plugin loads in Figma
2. UI displays correctly
3. Functions execute without errors
