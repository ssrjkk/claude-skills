---
name: storybook
description: Develops UI components in isolation with Storybook, supporting multiple frameworks. Use for building component libraries and design systems.
category: frontend
tags: [storybook, components, design-system, react, vue]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Storybook

> UI component explorer for isolated development and testing.

## Quick Start
```bash
npx storybook@latest init
npm run storybook
```

## When to Use
- Building component libraries
- Design system documentation
- Visual regression testing
- Component-driven development

## Step-by-Step
1. Init: `npx storybook@latest init`
2. Write stories in `*.stories.tsx` files
3. Configure addons in `.storybook/main.ts`
4. Build: `npm run build-storybook`

## Dependencies
```bash
npm install @storybook/react @storybook/addon-essentials
```

## Examples
```tsx
import type { Meta, StoryObj } from '@storybook/react'
import { Button } from './Button'

const meta: Meta<typeof Button> = {
  component: Button,
  argTypes: { variant: { control: 'select' } },
}
export default meta

export const Primary: StoryObj<typeof Button> = {
  args: { variant: 'primary', children: 'Click me' },
}
```

## Resources
- [Storybook Docs](https://storybook.js.org/docs)

## Validation
1. Storybook opens on port 6006
2. All stories render without errors
3. Controls and actions work
