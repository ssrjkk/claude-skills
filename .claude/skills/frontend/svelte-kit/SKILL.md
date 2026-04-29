---
name: svelte-kit
description: Создает SvelteKit приложения с файловой маршрутизацией и серверным рендерингом. Используется для легковесных, быстрых веб-приложений.
category: frontend
tags: [svelte, sveltekit, frontend, ssr]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# SvelteKit

> Быстрый фреймворк для создания Svelte приложений с серверным рендерингом.

## 🚀 Quick Start
```svelte
<!-- src/routes/+page.svelte -->
<script>
    let count = 0;
    function increment() {
        count += 1;
    }
</script>

<button on:click={increment}>
    Clicked {count} times
</button>
```

## 📋 Когда использовать
- ✅ Легковесные, производительные приложения
- ✅ Нужен SSR с минимальным JS бандлом
- ❌ Не использовать если команда знает только React/Vue

## 🔧 Пошаговая инструкция
1. Создай проект: `npm create svelte@latest my-app`
2. Создай роуты в `src/routes/`
3. Добавь серверную логику в `+page.server.js`
4. Запусти: `npm run dev`

## 📦 Зависимости
```bash
npm create svelte@latest my-app
```

## 🧪 Примеры
Input: Клик по кнопке → счетчик увеличивается реактивно

## 🔗 Ресурсы
- [SvelteKit Docs](https://kit.svelte.dev/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Приложение собирается без ошибок
2. Роутинг работает по файловой структуре
3. Реактивность Svelte функционирует
