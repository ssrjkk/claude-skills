---
name: cypress-e2e
description: Создает E2E тесты с Cypress для современных веб-приложений. Используется для быстрого тестирования с отладкой.
category: qa
tags: [cypress, e2e, testing, javascript, typescript]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# Cypress E2E

> E2E тестирование с Cypress для современных веб-приложений.

## 🚀 Quick Start
```javascript
describe('My First Test', () => {
  it('Does not do much!', () => {
    cy.visit('https://example.com')
    cy.contains('Example Domain').should('be.visible')
  })
})
```

## 📋 Когда использовать
- ✅ E2E тестирование современных веб-приложений
- ✅ Нужна отладка в реальном времени
- ❌ Не использовать для мобильных приложений

## 🔧 Пошаговая инструкция
1. Установи: `npm install cypress --save-dev`
2. Открой Cypress: `npx cypress open`
3. Создай тесты в `cypress/e2e/`
4. Запусти: `npx cypress run`

## 📦 Зависимости
```bash
npm install cypress --save-dev
```

## 🧪 Примеры
Input: Запуск теста → Output: Тест проходит, скриншоты сохраняются

## 🔗 Ресурсы
- [Cypress Docs](https://docs.cypress.io/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Тесты проходят без ошибок
2. Скриншоты/видео сохраняются
3. Отладка работает в реальном времени
