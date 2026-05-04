---
name: angular-typescript
description: Creates Angular applications with TypeScript, components, and services. Use for enterprise frontend development.
category: frontend
tags: [angular, typescript, frontend, components, rxjs]
models: [opus]
version: 1.0.0
created: 2026-05-01
---
# Angular TypeScript

> Structured enterprise applications with Angular and TypeScript.

## 🚀 Quick Start
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-user',
  template: `<h2>{{ title }}</h2>`
})
export class UserComponent {
  title = 'User Component';
  
  constructor(private userService: UserService) {}
}
```

## 📋 When to Use
- ✅ Enterprise Angular projects
- ✅ Need strict structure and dependency injection
- ❌ Not for simple SPAs (better React/Vue)

## 🔧 Step-by-Step Instructions
1. Install CLI: `npm install -g @angular/cli`
2. Create project: `ng new myproject`
3. Generate components: `ng generate component user`
4. Run: `ng serve`

## 📦 Dependencies
```bash
npm install -g @angular/cli
```

## 🧪 Examples
Input: `ng generate component hero` → Output: HeroComponent files created

## 🔗 Resources
- [Angular Docs](https://angular.io/docs)
- [Examples](./examples/)

## ✅ Validation
1. App builds without TypeScript errors
2. Components render correctly
3. Services injected properly
