---
name: react-typescript
description: Creates React components with TypeScript, props typing, and hooks. Use for type-safe UI development.
category: frontend
tags: [react, typescript, frontend, components, hooks]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# React TypeScript

> Type-safe React components with full TypeScript support.

## 🚀 Quick Start
```typescript
import React from 'react';

interface UserCardProps {
    name: string;
    email: string;
    onSelect: (name: string) => void;
}

export const UserCard: React.FC<UserCardProps> = ({ name, email, onSelect }) => {
    return (
        <div onClick={() => onSelect(name)}>
            <h3>{name}</h3>
            <p>{email}</p>
        </div>
    );
};
```

## 📋 When to Use
- ✅ New React projects with TypeScript
- ✅ Need strict props and state typing
- ❌ Not for simple HTML pages without interactivity

## 🔧 Step-by-Step Instructions
1. Create project: `npx create-react-app my-app --template typescript`
2. Define interfaces for props
3. Create components with typing
4. Run: `npm start`

## 📦 Dependencies
```bash
npx create-react-app my-app --template typescript
```

## 🧪 Examples
Input: `<UserCard name="John" email="john@test.com" onSelect={console.log} />`
Output: Rendered user card with click handler

## 🔗 Resources
- [React TypeScript Docs](https://react-typescript-cheatsheet.netlify.app/)
- [Examples](./examples/)

## ✅ Validation
1. Project compiles without TypeScript errors
2. Props validated correctly
3. IntelliSense provides correct types
