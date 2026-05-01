---
name: unity
description: Разрабатывает игры на Unity с использованием C# скриптов и компонентной архитектуры. Используется для 2D/3D игр под множество платформ.
category: gamedev
tags: [unity, csharp, game-dev, 2d, 3d]
models: [opus]
version: 1.0.0
created: 2026-05-01
---
# Unity

> Кроссплатформенная разработка игр на Unity с C#.

## 🚀 Quick Start
```csharp
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public float speed = 10.0f;
    
    void Update()
    {
        float move = Input.GetAxis("Vertical") * speed * Time.deltaTime;
        transform.Translate(0, 0, move);
    }
}
```

## 📋 Когда использовать
- ✅ Разработка 2D/3D игр
- ✅ Кроссплатформенный деплой (PC, Mobile, Console)
- ❌ Не использовать для простых приложений без графики

## 🔧 Пошаговая инструкция
1. Установи Unity Hub и выбери версию Unity
2. Создай проект (2D/3D Template)
3. Напиши C# скрипты в папке `Assets/Scripts/`
4. Тестируй в Play Mode

## 📦 Зависимости
Установи Unity Hub с https://unity.com/download

## 🧪 Примеры
Input: Нажатие клавиши W → Output: Персонаж движется вперед

## 🔗 Ресурсы
- [Unity Docs](https://docs.unity3d.com/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Сцена запускается без ошибок
2. Скрипты компилируются успешно
3. Игровые механики работают корректно
