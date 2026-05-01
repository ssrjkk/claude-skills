---
name: astro-ssg
description: Создает статические сайты с Astro, поддерживающим любые UI фреймворки. Используется для быстрых контент-ориентированных сайтов.
category: frontend
tags: [astro, ssg, static-site, markdown, mdx]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# Astro SSG

> Быстрые статические сайты с Astro и любыми UI фреймворками.

## 🚀 Quick Start
```astro
---
// src/pages/index.astro
const title = "Hello Astro";
---
<html>
  <head><title>{title}</title></head>
  <body>
    <h1>{title}</h1>
  </body>
</html>
```

## 📋 Когда использовать
- ✅ Контент-сайты (блоги, документация)
- ✅ Нужна максимальная производительность
- ❌ Не использовать для сложных SPA с много состоянием

## 🔧 Пошаговая инструкция
1. Создай проект: `npm create astro@latest`
2. Добавь интеграции (React, Vue, Svelte)
3. Создай страницы в `src/pages/`
4. Запусти: `npm run dev`

## 📦 Зависимости
```bash
npm create astro@latest
```

## 🧪 Примеры
Input: Создание MDX страницы → Output: Статическая HTML страница

## 🔗 Ресурсы
- [Astro Docs](https://docs.astro.build/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Сайт собирается в статические HTML файлы
2. Markdown/MDX обрабатывается корректно
3. Интеграции с UI фреймворками работают
