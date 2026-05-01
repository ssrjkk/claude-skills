---
name: figma-plugin
description: Разрабатывает плагины для Figma с использованием TypeScript и Figma Plugin API. Используется для автоматизации дизайн-процессов.
category: design
tags: [figma, plugin, typescript, design, automation]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# Figma Plugin

> Создание плагинов для Figma на TypeScript.

## 🚀 Quick Start
```typescript
figma.showUI(__html__, { width: 300, height: 200 });

figma.ui.onmessage = async (msg) => {
    if (msg.type === 'create-rect') {
        const rect = figma.createRectangle();
        rect.x = 100;
        figma.currentPage.appendChild(rect);
    }
};
```

## 📋 Когда использовать
- ✅ Автоматизация задач в Figma
- ✅ Создание дизайн-токенов программно
- ❌ Не использовать для разработки веб-сайтов

## 🔧 Пошаговая инструкция
1. Создай плагин: `npx create-figma-plugin`
2. Напиши логику в `src/plugin.ts`
3. Создай UI в `src/ui.tsx`
4. Тестируй в Figma (Plugins → Development)

## 📦 Зависимости
```bash
npx create-figma-plugin
```

## 🧪 Примеры
Input: Запуск плагина → Output: Создан прямоугольник в Figma

## 🔗 Ресурсы
- [Figma Plugin API](https://www.figma.com/plugin-docs/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Плагин загружается в Figma
2. UI отображается корректно
3. Функции выполняются без ошибок
