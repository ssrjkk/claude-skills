---
name: accessibility
description: Проверяет и улучшает доступность веб-приложений по стандартам WCAG. Используется для создания инклюзивного дизайна.
category: design
tags: [accessibility, wcag, a11y, inclusive-design]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# Accessibility (A11y)

> Обеспечение доступности веб-приложений по стандартам WCAG.

## 🚀 Quick Start
```html
<!-- Правильно -->
<button aria-label="Закрыть" onclick="closeModal()">
  <span aria-hidden="true">×</span>
</button>

<!-- Для скринридеров -->
<img src="chart.png" alt="График продаж за 2024 год">
```

## 📋 Когда использовать
- ✅ Веб-приложения с широкой аудиторией
- ✅ Compliance с законодательством (ADA, Section 508)
- ❌ Не использовать для внутренних админок без пользователей с ОВЗ

## 🔧 Пошаговая инструкция
1. Проведи аудит с axe DevTools
2. Добавь ARIA атрибуты где нужно
3. Обеспечь навигацию с клавиатуры
4. Проверь контрастность цветов

## 📦 Зависимости
```bash
npm install @axe-core/cli pa11y
```

## 🧪 Примеры
Input: Проверка формы → Output: 3 ошибки контрастности исправлены

## 🔗 Ресурсы
- [WCAG Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Сканеры не находят критических нарушений
2. Навигация с клавиатуры работает
3. Скринридеры корректно читают контент
