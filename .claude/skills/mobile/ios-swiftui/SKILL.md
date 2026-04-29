---
name: ios-swiftui
description: Создает iOS приложения с использованием SwiftUI и современных паттернов Apple. Используется для нативной разработки под iOS.
category: mobile
tags: [ios, swiftui, swift, apple, mobile]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# iOS SwiftUI

> Современный фреймворк Apple для создания нативных iOS интерфейсов декларативно.

## 🚀 Quick Start
```swift
import SwiftUI

struct ContentView: View {
    @State private var count = 0
    
    var body: some View {
        VStack {
            Text("Count: \(count)")
            Button("Increment") {
                count += 1
            }
        }
    }
}
```

## 📋 Когда использовать
- ✅ Нативная iOS разработка
- ✅ Нужен современный декларативный UI
- ❌ Не использовать для Android или кроссплатформенных проектов

## 🔧 Пошаговая инструкция
1. Открой Xcode и создай новый SwiftUI проект
2. Определи View структуры с модификаторами
3. Добавь состояние через `@State` или `@ObservableObject`
4. Запусти в симуляторе: Cmd + R

## 📦 Зависимости
Установи Xcode из App Store

## 🧪 Примеры
Input: Нажатие на кнопку → счетчик увеличивается на 1

## 🔗 Ресурсы
- [SwiftUI Docs](https://developer.apple.com/xcode/swiftui/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Проект собирается в Xcode без ошибок
2. Preview работает корректно
3. Состояние обновляется реактивно
