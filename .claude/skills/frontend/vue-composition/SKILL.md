---
name: vue-composition
description: Creates Vue 3 components with Composition API and TypeScript. Use for modern Vue applications with reactive state.
category: frontend
tags: [vue, composition-api, typescript, frontend]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Vue Composition API

> Modern Vue component creation with reactivity and TypeScript.

## 🚀 Quick Start
```vue
<script setup lang="ts">
import { ref, computed } from 'vue';

interface User {
    name: string;
    email: string;
}

const user = ref<User>({ name: 'John', email: 'john@test.com' });
const displayName = computed(() => user.value.name.toUpperCase());
</script>

<template>
    <div>
        <h3>{{ displayName }}</h3>
        <p>{{ user.email }}</p>
    </div>
</template>
```

## 📋 When to Use
- ✅ Vue 3 projects with modern syntax
- ✅ Need reactivity and composition
- ❌ Not for Vue 2 without migration

## 🔧 Step-by-Step Instructions
1. Create project: `npm create vue@latest`
2. Choose TypeScript and Composition API
3. Create components with `script setup`
4. Run: `npm run dev`

## 📦 Dependencies
```bash
npm create vue@latest
```

## 🧪 Examples
Input: Change `user.name` → `displayName` updates reactively

## 🔗 Resources
- [Vue 3 Docs](https://vuejs.org/)
- [Examples](./examples/)

## ✅ Validation
1. Component renders without errors
2. Reactivity works correctly
3. TypeScript types respected
