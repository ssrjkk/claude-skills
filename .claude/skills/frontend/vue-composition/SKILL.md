---
name: vue-composition
description: Создает Vue 3 компоненты с Composition API и TypeScript. Используется для современных Vue приложений с реактивным состоянием.
category: frontend
tags: [vue, composition-api, typescript, frontend]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Vue Composition API

> Современный подход к созданию Vue компонентов с реактивностью и TypeScript.

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

## 📋 Когда использовать
- ✅ Vue 3 проекты с современным синтаксисом
- ✅ Нужна реактивность и композиция логики
- ❌ Не использовать с Vue 2 без миграции

## 🔧 Пошаговая инструкция
1. Создай проект: `npm create vue@latest`
2. Выбери TypeScript и Composition API
3. Создай компоненты с `script setup`
4. Запусти: `npm run dev`

## 📦 Зависимости
```bash
npm create vue@latest
```

## 🧪 Примеры
Input: Изменение `user.name` → `displayName` обновляется автоматически

## 🔗 Ресурсы
- [Vue 3 Docs](https://vuejs.org/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Компонент рендерится без ошибок
2. Реактивность работает корректно
3. TypeScript типы соблюдаются
