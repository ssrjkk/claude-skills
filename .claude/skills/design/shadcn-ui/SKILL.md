---
name: shadcn-ui
description: Builds modern UI components with shadcn/ui, a collection of re-usable components built with Radix UI and Tailwind CSS. Use for beautiful, accessible React apps.
category: design
tags: [shadcn-ui, react, tailwind, radix, components]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# shadcn/ui

> Beautifully designed components that you can copy and paste into your apps.

## Quick Start
```bash
npx shadcn@latest init
npx shadcn@latest add button card dialog
```

## When to Use
- Building React apps with Tailwind
- Need accessible, styled components
- Rapid UI development
- Consistent design system

## Step-by-Step
1. Init: `npx shadcn@latest init`
2. Add components: `npx shadcn@latest add button`
3. Import and use in your app
4. Customize with Tailwind classes

## Dependencies
```bash
npx shadcn@latest init
npx shadcn@latest add button card input dialog dropdown-menu
```

## Examples
```tsx
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader } from "@/components/ui/card"

export default function Login() {
  return (
    <Card>
      <CardHeader>Welcome Back</CardHeader>
      <CardContent>
        <Button variant="default">Sign In</Button>
      </CardContent>
    </Card>
  )
}
```

## Resources
- [shadcn/ui Docs](https://ui.shadcn.com)

## Validation
1. Components render correctly
2. Dark mode works via class toggle
3. Components are accessible (keyboard, screen reader)
