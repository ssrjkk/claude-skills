---
name: ci-cd-setup
description: Настраивает CI/CD пайплайны для тестирования с использованием GitHub Actions. Используется для автоматизации запуска тестов, сборки и деплоя в QA-окружения.
category: qa
tags: [ci-cd, github-actions, automation, testing, pytest, qa]
models: [haiku, sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# CI/CD Setup

## 🚀 Quick Start
```yaml
# .github/workflows/qa-tests.yml
name: QA Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
      - run: pip install pytest
      - run: pytest
```

## 📋 Инструкция
1. Создай папку `.github/workflows/` в корне репозитория
2. Напиши YAML-файл пайплайна с шагами установки зависимостей и запуска тестов
3. Добавь шаги для настройки PostgreSQL и Allure (если используется)
4. Закоммить файл, пайплайн запустится автоматически

## 🔧 Скрипты/Инструменты
- `scripts/setup_env.sh` — настройка окружения в CI
- `scripts/run_tests.sh` — запуск тестов с параметрами

## 📚 Ресурсы
- `reference.md` — синтаксис GitHub Actions и доступные раннеры
- `examples.md` — примеры пайплайнов для pytest и Allure

## ✅ Валидация
1. Пайплайн успешно проходит при пуше в ветку
2. Тесты запускаются корректно, результаты доступны в интерфейсе GitHub
3. Нет ошибок конфигурации YAML
