---
name: e2e-playwright
description: Создает E2E тесты с Playwright и генерацией Allure отчетов. Используется для автоматизированного тестирования пользовательских сценариев.
category: qa
tags: [e2e, playwright, testing, allure]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# E2E Playwright

> Автоматизированное E2E тестирование с Playwright и Allure.

## 🚀 Quick Start
```typescript
import { test, expect } from '@playwright/test';

test('basic test', async ({ page }) => {
    await page.goto('https://example.com');
    await expect(page.locator('h1')).toHaveText('Example Domain');
});
```

## 📋 Когда использовать
- ✅ E2E тестирование веб-приложений
- ✅ Нужны скриншоты и видео при падениях
- ❌ Не использовать для unit-тестов

## 🔧 Пошаговая инструкция
1. Установи: `npm init playwright@latest`
2. Создай тесты в `tests/` папке
3. Запусти: `npx playwright test`
4. Сгенерируй Allure отчет

## 📦 Зависимости
```bash
npm init playwright@latest
npm install allure-playwright
```

## 🧪 Примеры
Input: Запуск теста → Output: Успешный проход, скриншот сохранен

## 🔗 Ресурсы
- [Playwright Docs](https://playwright.dev/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Тесты проходят без ошибок
2. Allure отчеты генерируются корректно
3. Скриншоты/видео сохраняются при падениях
