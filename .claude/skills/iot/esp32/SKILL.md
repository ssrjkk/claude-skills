---
name: esp32
description: Программирует ESP32 микроконтроллеры на C/C++ или MicroPython. Используется для IoT проектов с WiFi/Bluetooth.
category: iot
tags: [esp32, iot, microcontroller, wifi, bluetooth, micropython]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# ESP32

> Программирование ESP32 для IoT проектов с WiFi и Bluetooth.

## 🚀 Quick Start
```cpp
#include <WiFi.h>

const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);
}

void loop() {
    Serial.println(WiFi.localIP());
    delay(1000);
}
```

## 📋 Когда использовать
- ✅ IoT проекты с подключением к сети
- ✅ Нужен WiFi/Bluetooth в устройстве
- ❌ Не использовать для простых проектов без связи (лучше Arduino)

## 🔧 Пошаговая инструкция
1. Установи ESP32 board в Arduino IDE
2. Выбери плату: Tools → Board → ESP32 Arduino
3. Напиши код и загрузи через USB
4. Мониторь Serial порт

## 📦 Зависимости
Arduino IDE с ESP32 board manager

## 🧪 Примеры
Input: Подключение к WiFi → Output: IP адрес в Serial мониторе

## 🔗 Ресурсы
- [ESP32 Docs](https://docs.espressif.com/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Код загружается без ошибок
2. Устройство подключается к WiFi
3. Serial монитор показывает данные
