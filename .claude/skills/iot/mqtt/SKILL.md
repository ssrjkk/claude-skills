---
name: mqtt
description: Настраивает MQTT брокеры и клиенты для обмена сообщениями в IoT системах. Используется для легковесного messaging в IoT.
category: iot
tags: [mqtt, iot, messaging, broker, mosquitto]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# MQTT

> Легковесный протокол messaging для IoT систем.

## 🚀 Quick Start
```bash
# Установка Mosquitto брокера
sudo apt-get install mosquitto mosquitto-clients

# Подписка на топик
mosquitto_sub -h localhost -t "sensors/temperature"

# Публикация сообщения
mosquitto_pub -h localhost -t "sensors/temperature" -m "23.5"
```

## 📋 Когда использовать
- ✅ IoT устройства с ограниченными ресурсами
- ✅ Pub/Sub паттерн для обмена данными
- ❌ Не использовать для больших файлов или сложных RPC

## 🔧 Пошаговая инструкция
1. Установи MQTT брокер (Mosquitto)
2. Настрой конфигурацию брокера
3. Подключай клиентов к брокеру
4. Публикуй и подписывайся на топики

## 📦 Зависимости
```bash
sudo apt-get install mosquitto mosquitto-clients
# или для Python: pip install paho-mqtt
```

## 🧪 Примеры
Input: `mosquitto_pub -t "test" -m "hello"` → Output: Подписчик получает "hello"

## 🔗 Ресурсы
- [MQTT Docs](https://mqtt.org/documentation/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Брокер запускается и слушает порт 1883
2. Сообщения доставляются между клиентами
3. QoS уровни работают корректно
