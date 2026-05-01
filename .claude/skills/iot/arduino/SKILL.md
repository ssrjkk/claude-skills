---
name: arduino
description: Программирует Arduino платы для аппаратных проектов и прототипирования. Используется для простых IoT и робототехнических проектов.
category: iot
tags: [arduino, iot, microcontroller, c, prototyping]
models: [haiku, sonnet]
version: 1.0.0
created: 2026-05-01
---
# Arduino

> Простое программирование микроконтроллеров для аппаратных проектов.

## 🚀 Quick Start
```cpp
void setup() {
    pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(1000);
    digitalWrite(LED_BUILTIN, LOW);
    delay(1000);
}
```

## 📋 Когда использовать
- ✅ Простые аппаратные проекты
- ✅ Быстрое прототипирование
- ❌ Не использовать для сложных IoT с облаком (лучше ESP32)

## 🔧 Пошаговая инструкция
1. Установи Arduino IDE
2. Подключи плату через USB
3. Выбери плату и порт в Tools
4. Загрузи скетч

## 📦 Зависимости
Скачай Arduino IDE с https://www.arduino.cc/en/software

## 🧪 Примеры
Input: Загрузка скетча → Output: Светодиод мигает раз в секунду

## 🔗 Ресурсы
- [Arduino Docs](https://www.arduino.cc/reference/en/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Скетч загружается успешно
2. Аппаратная часть работает
3. Serial монитор показывает данные (если используется)
