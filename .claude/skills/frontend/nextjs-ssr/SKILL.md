---
name: nextjs-ssr
description: Генерирует Next.js приложения с SSR, SSG и API роутами. Используется для SEO-оптимизированных React приложений.
category: frontend
tags: [nextjs, react, ssr, ssg, seo]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# Next.js SSR

> React framework для production с SSR, SSG и оптимизацией производительности.

## 🚀 Quick Start
```typescript
// pages/api/users.ts
import { NextApiRequest, NextApiResponse } from 'next';

export default function handler(req: NextApiRequest, res: NextApiResponse) {
    res.status(200).json([{ id: 1, name: 'John' }]);
}

// pages/users.tsx
export async function getServerSideProps() {
    const res = await fetch('http://localhost:3000/api/users');
    const users = await res.json();
    return { props: { users } };
}
```

## 📋 Когда использовать
- ✅ SEO-критичные React приложения
- ✅ Нужен SSR или статическая генерация
- ❌ Не использовать для простых SPA без SSR

## 🔧 Пошаговая инструкция
1. Создай проект: `npx create-next-app@latest`
2. Создай страницы в `pages/` или `app/`
3. Добавь API роуты в `pages/api/`
4. Запусти: `npm run dev`

## 📦 Зависимости
```bash
npx create-next-app@latest
```

## 🧪 Примеры
Input: `GET /users` → SSR страница со списком пользователей

## 🔗 Ресурсы
- [Next.js Docs](https://nextjs.org/docs)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Страницы генерируются на сервере
2. API роуты отвечают корректно
3. SEO метаданные присутствуют
