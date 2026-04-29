---
name: android-kotlin
description: Генерирует Android приложения с использованием Kotlin и Jetpack Compose. Используется для современной нативной разработки под Android.
category: mobile
tags: [android, kotlin, jetpack-compose, mobile]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# Android Kotlin

> Современная разработка Android приложений с Kotlin и Jetpack Compose.

## 🚀 Quick Start
```kotlin
import androidx.compose.foundation.layout.Column
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable

@Composable
fun Greeting(name: String) {
    Column {
        Text(text = "Hello $name!")
    }
}
```

## 📋 Когда использовать
- ✅ Нативная Android разработка
- ✅ Нужен современный UI с Jetpack Compose
- ❌ Не использовать для iOS или кроссплатформенных проектов

## 🔧 Пошаговая инструкция
1. Открой Android Studio и создай новый проект с Compose
2. Определи Composable функции
3. Добавь состояние через `remember` и `mutableStateOf`
4. Запусти на эмуляторе или устройстве

## 📦 Зависимости
Установи Android Studio

## 🧪 Примеры
Input: Вызов `Greeting("Android")` → отображается "Hello Android!"

## 🔗 Ресурсы
- [Android Developers](https://developer.android.com/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Приложение собирается в Android Studio
2. Compose Preview отображает UI
3. Состояние обновляется корректно
