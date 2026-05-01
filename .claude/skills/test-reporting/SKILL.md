---
name: test-reporting
description: Генерирует отчеты о результатах тестирования с использованием Allure и pytest. Используется для визуализации результатов тестов, отслеживания багов и совместной работы QA-команды.
category: qa
tags: [testing, reporting, allure, pytest, qa, metrics]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Test Reporting

## 🚀 Quick Start
```bash
pip install pytest allure-pytest
pytest --alluredir=allure-results
allure serve allure-results
```

## 📋 Инструкция
1. Установи Allure CLI и плагин pytest-allure
2. Запусти тесты с флагом `--alluredir` для сохранения результатов
3. Сгенерируй и открой отчет: `allure serve allure-results`
4. Настрой интеграцию с CI/CD для автоматической генерации отчетов

## 🔧 Скрипты/Инструменты
- `scripts/generate_report.sh` — генерация статического отчета Allure
- `scripts/metrics.py` — сбор метрик тестирования

## 📚 Ресурсы
- `reference.md` — аннотации Allure и структура отчетов
- `examples.md` — примеры кастомизации отчетов

## ✅ Валидация
1. Отчет Allure открывается без ошибок
2. Все результаты тестов отображаются корректно
3. Метрики собираются и сохраняются
