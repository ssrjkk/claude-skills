---
name: performance-k6
description: Проводит нагрузочное тестирование API и веб-приложений с k6. Используется для проверки производительности под нагрузкой.
category: qa
tags: [performance, k6, load-testing, qa]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Performance k6

> Нагрузочное тестирование с k6 и анализом метрик производительности.

## 🚀 Quick Start
```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

export default function() {
    let res = http.get('https://example.com');
    check(res, { 'status was 200': (r) => r.status == 200 });
    sleep(1);
}
```

## 📋 Когда использовать
- ✅ Нагрузочное тестирование API
- ✅ Проверка производительности под нагрузкой
- ❌ Не использовать для функционального тестирования

## 🔧 Пошаговая инструкция
1. Установи k6: `brew install k6`
2. Напиши сценарий нагрузки
3. Запусти: `k6 run script.js`
4. Анализируй метрики в отчете

## 📦 Зависимости
```bash
# Windows: https://k6.io/docs/getting-started/installation/
# Mac: brew install k6
# Linux: sudo apt-get install k6
```

## 🧪 Примеры
Input: `k6 run load-test.js` → Output: Метрики: avg response time, p95, error rate

## 🔗 Ресурсы
- [k6 Docs](https://k6.io/docs/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Тест запускается без ошибок
2. Метрики собираются корректно
3. Thresholds срабатывают при превышении лимитов
