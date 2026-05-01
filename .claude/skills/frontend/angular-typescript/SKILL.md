---
name: angular-typescript
description: Создает Angular приложения с TypeScript, компонентами и сервисами. Используется для enterprise frontend разработки.
category: frontend
tags: [angular, typescript, frontend, components, rxjs]
models: [opus]
version: 1.0.0
created: 2026-05-01
---
# Angular TypeScript

> Структурированные enterprise приложения на Angular с TypeScript.

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

## 📋 Когда использовать
- ✅ Enterprise Angular проекты
- ✅ Нужна строгая структура и dependency injection
- ❌ Не использовать для простых SPA (лучше React/Vue)

## 🔧 Пошаговая инструкция
1. Установи CLI: `npm install -g @angular/cli`
2. Создай проект: `ng new myproject`
3. Генерируй компоненты: `ng generate component user`
4. Запусти: `ng serve`

## 📦 Зависимости
```bash
npm install -g @angular/cli
```

## 🧪 Примеры
Input: `ng generate component hero` → Output: Созданы файлы HeroComponent

## 🔗 Ресурсы
- [Angular Docs](https://angular.io/docs)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Приложение собирается без ошибок TypeScript
2. Компоненты рендерятся корректно
3. Сервисы инжектятся правильно
