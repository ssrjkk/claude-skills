---
name: radix-ui
description: Builds accessible React UI primitives with Radix UI, including dialogs, dropdowns, and tooltips.
category: design
tags: [radix-ui, react, accessibility, headless, components]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Radix UI
> Headless React UI primitives with full accessibility support.
## Quick Start
```bash
npm install @radix-ui/react-dialog @radix-ui/react-dropdown-menu @radix-ui/react-tooltip
```
## Dialog
```tsx
import * as Dialog from '@radix-ui/react-dialog'
<Dialog.Root><Dialog.Trigger asChild><button>Open</button></Dialog.Trigger>
<Dialog.Portal><Dialog.Overlay /><Dialog.Content>
  <Dialog.Title>Edit Profile</Dialog.Title>
  <Dialog.Close asChild><button>Close</button></Dialog.Close>
</Dialog.Content></Dialog.Portal></Dialog.Root>
```
## When to Use
- Accessible components; Custom design systems; ARIA-compliant UIs
## Validation
1. Keyboard navigation works; 2. Screen reader announces roles; 3. Focus management correct
