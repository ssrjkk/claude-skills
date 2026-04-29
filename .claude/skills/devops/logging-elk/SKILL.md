---
name: logging-elk
description: Настраивает централизованный сбор и анализ логов с ELK стеком (Elasticsearch, Logstash, Kibana). Используется для отладки и мониторинга логов.
category: devops
tags: [elk, elasticsearch, logstash, kibana, logging]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# Logging ELK

> Централизованный сбор, хранение и анализ логов с ELK стеком.

## 🚀 Quick Start
```yaml
# docker-compose.yml
version: '3'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.x
    ports:
      - "9200:9200"
  kibana:
    image: docker.elastic.co/kibana/kibana:8.x
    ports:
      - "5601:5601"
```

## 📋 Когда использовать
- ✅ Централизованный сбор логов с множества сервисов
- ✅ Нужен поиск и анализ логов
- ❌ Не использовать для простых приложений с одним лог-файлом

## 🔧 Пошаговая инструкция
1. Запусти ELK через docker-compose
2. Настрой логирование приложения в JSON формате
3. Настрой Logstash pipeline для парсинга
4. Создавай дашборды в Kibana

## 📦 Зависимости
```bash
docker-compose up -d
```

## 🧪 Примеры
Input: Логи приложения отправляются в Logstash
Output: Логи индексируются в Elasticsearch и видны в Kibana

## 🔗 Ресурсы
- [ELK Stack Docs](https://www.elastic.co/guide/index.html)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Elasticsearch отвечает на запросы
2. Логи появляются в Kibana
3. Поиск по логам работает корректно
