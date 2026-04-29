---
name: nodejs-express
description: Генерирует boilerplate для Express.js приложений с TypeScript и middleware. Используется при создании Node.js API или веб-сервисов.
category: backend
tags: [nodejs, express, typescript, javascript, rest]
models: [haiku, sonnet]
version: 1.0.0
created: 2026-04-29
---
# Node.js Express

> Минималистичный веб-фреймворк для Node.js с поддержкой TypeScript.

## 🚀 Quick Start
```typescript
import express, { Request, Response } from 'express';

const app = express();
app.use(express.json());

app.get('/api/users', (req: Request, res: Response) => {
    res.json([{ id: 1, name: 'John' }]);
});

app.listen(3000, () => console.log('Server running on port 3000'));
```

## 📋 Когда использовать
- ✅ Создание REST API на Node.js
- ✅ Нужна простая и гибкая настройка middleware
- ❌ Не использовать для сложных GraphQL серверов (лучше Apollo)

## 🔧 Пошаговая инструкция
1. Инициализируй проект: `npm init -y`
2. Установи зависимости: `npm install express typescript @types/node`
3. Создай `tsconfig.json` и файл сервера
4. Запусти: `npx tsc && node dist/server.js`

## 📦 Зависимости
```bash
npm install express typescript @types/express @types/node ts-node
```

## 🧪 Примеры
Input: `GET /api/users`
Output: `[{"id": 1, "name": "John"}]`

## 🔗 Ресурсы
- [Express.js Documentation](https://expressjs.com)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Сервер запускается без ошибок компиляции TypeScript
2. Эндпоинты отвечают корректно
3. JSON парсинг работает правильно
