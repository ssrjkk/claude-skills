---
name: react-typescript
description: Создает компоненты React с TypeScript, типизацией props и хуками. Используется для разработки типобезопасного UI.
category: frontend
tags: [react, typescript, frontend, components, hooks]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# React TypeScript

> Типобезопасные React компоненты с полной поддержкой TypeScript.

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

## 📋 Когда использовать
- ✅ Новые React проекты с TypeScript
- ✅ Нужна строгая типизация props и состояния
- ❌ Не использовать для простых HTML страниц без интерактивности

## 🔧 Пошаговая инструкция
1. Создай проект: `npx create-react-app my-app --template typescript`
2. Определи интерфейсы для props
3. Создай компоненты с типизацией
4. Запусти: `npm start`

## 📦 Зависимости
```bash
npx create-react-app my-app --template typescript
```

## 🧪 Примеры
Input: `<UserCard name="John" email="john@test.com" onSelect={console.log} />`
Output: Отрисованная карточка пользователя с обработчиком клика

## 🔗 Ресурсы
- [React TypeScript Docs](https://react-typescript-cheatsheet.netlify.app/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Проект компилируется без ошибок TypeScript
2. Props валидируются корректно
3. IntelliSense предлагает правильные типы
