---
name: kafka-streams
description: Обрабатывает потоковые данные с Apache Kafka Streams. Используется для real-time обработки событий.
category: data
tags: [kafka, streams, real-time, events, java, scala]
models: [opus]
version: 1.0.0
created: 2026-05-01
---
# Kafka Streams

> Обработка потоковых данных в реальном времени с Kafka Streams.

## 🚀 Quick Start
```java
StreamsBuilder builder = new StreamsBuilder();
KStream<String, String> source = builder.stream("input-topic");
source.mapValues(value -> value.toUpperCase())
      .to("output-topic");

KafkaStreams streams = new KafkaStreams(builder.build(), config);
streams.start();
```

## 📋 Когда использовать
- ✅ Real-time обработка событий
- ✅ Потоковая аналитика
- ❌ Не использовать для batch обработки

## 🔧 Пошаговая инструкция
1. Добавь зависимость Kafka Streams
2. Создай StreamsBuilder с топиками
3. Определи трансформации
4. Запусти KafkaStreams приложение

## 📦 Зависимости
```xml
<dependency>
    <groupId>org.apache.kafka</groupId>
    <artifactId>kafka-streams</artifactId>
    <version>3.6.0</version>
</dependency>
```

## 🧪 Примеры
Input: Сообщение в "input-topic" → Output: UPPERCASE в "output-topic"

## 🔗 Ресурсы
- [Kafka Streams Docs](https://kafka.apache.org/documentation/streams/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Приложение подключается к Kafka
2. Сообщения обрабатываются в реальном времени
3. Ошибки обработки отлавливаются
