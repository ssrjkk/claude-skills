---
name: unreal
description: Создает игры на Unreal Engine с Blueprints или C++. Используется для AAA-качества и высокопроизводительных игр.
category: gamedev
tags: [unreal, cpp, blueprint, game-dev, aaa]
models: [opus]
version: 1.0.0
created: 2026-05-01
---
# Unreal Engine

> Профессиональный движок для AAA игр с Blueprints и C++.

## 🚀 Quick Start
```cpp
// MyActor.cpp
#include "MyActor.h"

void AMyActor::BeginPlay()
{
    Super::BeginPlay();
    UE_LOG(LogTemp, Warning, TEXT("Actor started!"));
}
```

## 📋 Когда использовать
- ✅ AAA игры с высокой графикой
- ✅ Сложные игровые механики
- ❌ Не использовать для простых мобильных игр (лучше Unity)

## 🔧 Пошаговая инструкция
1. Установи Unreal Engine через Epic Games Launcher
2. Создай проект (Blueprint или C++)
3. Используй Blueprints для быстрого прототипирования
4. Пиши C++ для производительности

## 📦 Зависимости
Установи Unreal Engine через Epic Games Launcher

## 🧪 Примеры
Input: Событие BeginPlay → Output: Сообщение в логе

## 🔗 Ресурсы
- [Unreal Docs](https://docs.unrealengine.com/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Проект компилируется без ошибок
2. Blueprints работают корректно
3. Игра запускается в Editor Mode
