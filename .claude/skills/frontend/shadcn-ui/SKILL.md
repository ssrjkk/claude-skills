---
name: shadcn-ui
description: Building with shadcn/ui component library
category: frontend
tags: [shadcn-ui, react, tailwind, components, design-system]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# shadcn/ui

> Build beautiful, accessible UIs with shadcn/ui — copy-paste components for React.

## Quick Start
```bash
# Initialize shadcn/ui in your project
npx shadcn@latest init

# Add components one at a time
npx shadcn@latest add button
npx shadcn@latest add card
npx shadcn@latest add dialog
npx shadcn@latest add table
npx shadcn@latest add form
npx shadcn@latest add toast

# Build with components
```

```tsx
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

export function LoginCard() {
  return (
    <Card className="w-[350px]">
      <CardHeader>
        <CardTitle>Login</CardTitle>
        <CardDescription>Enter your credentials below.</CardDescription>
      </CardHeader>
      <CardContent>
        <form>
          <div className="grid gap-4">
            <div className="grid gap-2">
              <Label htmlFor="email">Email</Label>
              <Input id="email" type="email" placeholder="m@example.com" />
            </div>
            <div className="grid gap-2">
              <Label htmlFor="password">Password</Label>
              <Input id="password" type="password" />
            </div>
          </div>
        </form>
      </CardContent>
      <CardFooter className="flex justify-between">
        <Button variant="outline">Cancel</Button>
        <Button>Login</Button>
      </CardFooter>
    </Card>
  );
}
```

## Key Concepts
shadcn/ui is not a package — it's copy-paste components built on Radix UI primitives with Tailwind CSS. You own the code and can customize everything. Components are accessible, composable, and tree-shakeable by default.

## When to Use
- Rapidly building production UIs with consistent design
- Projects that need customizable, accessible components
- Teams that want to avoid bloated component libraries

## Validation
1. `npx shadcn@latest init` configures components.json correctly
2. Added components render with correct styling
3. Dark mode works via Tailwind class strategy
4. Components are accessible (keyboard navigation, ARIA attributes)
