---
name: selenium-grid
description: Настраивает Selenium Grid для распределенного тестирования веб-приложений. Используется для параллельного запуска тестов.
category: qa
tags: [selenium, grid, testing, parallel, webdriver]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# Selenium Grid

> Параллельное выполнение тестов с Selenium Grid.

## 🚀 Quick Start
```bash
# Запуск Selenium Grid
java -jar selenium-server.jar hub

# Регистрация ноды
java -jar selenium-server.jar node --hub http://localhost:4444
```

```python
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities.CHROME.copy()
driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=caps)
```

## 📋 Когда использовать
- ✅ Параллельное выполнение тестов
- ✅ Кросс-браузерное тестирование
- ❌ Не использовать для простых E2E тестов (лучше Playwright)

## 🔧 Пошаговая инструкция
1. Скачай Selenium Server
2. Запусти Hub и ноды
3. Настрой тесты для Remote WebDriver
4. Запусти тесты параллельно

## 📦 Зависимости
```bash
pip install selenium
# Скачать selenium-server.jar
```

## 🧪 Примеры
Input: Запуск 10 тестов → Output: Выполняются параллельно на нодах

## 🔗 Ресурсы
- [Selenium Grid Docs](https://www.selenium.dev/documentation/grid/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Grid доступен по HTTP
2. Ноды регистрируются успешно
3. Тесты выполняются параллельно
