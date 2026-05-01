---
name: design-tokens
description: Управляет дизайн-токенами с использованием Style Dictionary или Theo. Используется для поддержания консистентности дизайн-систем.
category: design
tags: [design-tokens, design-system, style-dictionary, theming]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# Design Tokens

> Управление дизайн-токенами для консистентных UI систем.

## 🚀 Quick Start
```json
{
  "color": {
    "primary": { "value": "#007AFF" },
    "secondary": { "value": "#5856D6" }
  },
  "spacing": {
    "small": { "value": "8px" },
    "medium": { "value": "16px" }
  }
}
```

## 📋 Когда использовать
- ✅ Дизайн-системы с множеством платформ
- ✅ Нужна консистентность цветов, отступов, шрифтов
- ❌ Не использовать для одноразовых проектов

## 🔧 Пошаговая инструкция
1. Определи токены в JSON/YAML файле
2. Настрой Style Dictionary конфигурацию
3. Сгенерируй платформ-специфичные файлы
4. Интегрируй в проект

## 📦 Зависимости
```bash
npm install style-dictionary
```

## 🧪 Примеры
Input: Токен `color.primary` → Output: CSS переменная `--color-primary: #007AFF;`

## 🔗 Ресурсы
- [Style Dictionary](https://amzn.github.io/style-dictionary/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Токены сгенерированы для всех платформ
2. Значения применяются корректно
3. Темы (light/dark) переключаются
