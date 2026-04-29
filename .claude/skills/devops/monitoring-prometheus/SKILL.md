---
name: monitoring-prometheus
description: Настраивает мониторинг приложений и инфраструктуры с Prometheus и Grafana. Используется для сбора метрик и алертинга.
category: devops
tags: [prometheus, grafana, monitoring, metrics]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Monitoring Prometheus

> Сбор метрик, алертинг и визуализация с Prometheus + Grafana.

## 🚀 Quick Start
```yaml
# prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'myapp'
    static_configs:
      - targets: ['localhost:8080']
```

```bash
# Запуск Prometheus
docker run -p 9090:9090 -v prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
```

## 📋 Когда использовать
- ✅ Нужен мониторинг приложений
- ✅ Сбор временных рядов метрик
- ❌ Не использовать для логирования (лучше ELK)

## 🔧 Пошаговая инструкция
1. Настрой экспортеры метрик в приложении
2. Создай prometheus.yml с scrape configs
3. Запусти Prometheus и Grafana контейнеры
4. Настрой дашборды в Grafana

## 📦 Зависимости
```bash
docker run -p 9090:9090 prom/prometheus
docker run -p 3000:3000 grafana/grafana
```

## 🧪 Примеры
Input: HTTP запрос к `/metrics` эндпоинту
Output: Метрики в формате Prometheus

## 🔗 Ресурсы
- [Prometheus Docs](https://prometheus.io/docs/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Prometheus собирает метрики с таргетов
2. Алерты срабатывают при условиях
3. Графики в Grafana отображают данные
