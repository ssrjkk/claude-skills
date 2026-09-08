---
name: prisma-orm
description: "Models databases and writes type-safe queries with Prisma ORM. Use for modern Node.js/TypeScript database access."
category: database
tags: [prisma-orm, database, russian]
models: [sonnet, opus]
version: "1.0"
language: ru
original: prisma-orm
---
# Prisma ORM

> Type-safe доступ к БД с автоматически генерируемыми запросами.

## Быстрый старт
```prisma
// schema.prisma
model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
  posts Post[]
}

model Post {
  id        Int      @id @default(autoincrement())
  title     String
  content   String?
  author    User     @relation(fields: [authorId], references: [id])
  authorId  Int
}
```

```typescript
import { PrismaClient } from '@prisma/client';
const prisma = new PrismaClient();

// Type-safe запрос
const user = await prisma.user.create({
  data: {
    email: 'alice@example.com',
    posts: { create: { title: 'Hello Prisma' } }
  },
  include: { posts: true }
});
```

## Когда использовать
- Type-safe доступ к БД
- Быстрая эволюция схемы с миграциями
- Не для сложных сырых SQL-запросов

## Пошаговые инструкции
1. Установка: `npm install prisma @prisma/client`
2. Инициализация: `npx prisma init`
3. Опишите модели в `schema.prisma`
4. Миграция: `npx prisma migrate dev`

## Зависимости
```bash
npm install prisma @prisma/client
npx prisma init
```

## Примеры
Вход: `prisma.user.findMany({ where: { email: { contains: "@" } } })` → Выход: все пользователи с @ в email

## Ресурсы
- [Prisma Docs](https://www.prisma.io/docs)
- [Examples](./examples/)

## Устранение неполадок
- **`PrismaClientInitializationError`** — схема не синхронизирована.
  Повторно выполните `npx prisma generate` и проверьте `DATABASE_URL`.
- **Интроспекция перезаписывает кастомные типы** — `prisma db pull`
  работает как черновик; заново наложите типы и связи вручную.
- **Медленные relation-запросы** — не хватает индекса. Добавьте `@@index`
  на внешние ключи и анализируйте запросы через Prisma Data Platform.
- **Миграции расходятся на командных ветках** — запускайте
  `prisma migrate dev` чаще и делайте rebase миграций, а не reset БД.

## Валидация
1. Схема валидна: `npx prisma validate`
2. Миграция применяется успешно
3. Сгенерированный клиент type-safe
