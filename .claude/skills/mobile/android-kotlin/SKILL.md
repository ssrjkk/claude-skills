---
name: android-kotlin
description: Generates Android applications using Kotlin and Jetpack Compose. Use for modern native Android development.
category: mobile
tags: [android, kotlin, jetpack-compose, mobile]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# Android Kotlin

> Modern Android development with Kotlin and Jetpack Compose.

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

## 📋 When to Use
- ✅ Native Android development
- ✅ Modern UI with Jetpack Compose
- ❌ Not for iOS or cross-platform

## 🔧 Step-by-Step Instructions
1. Install Android Studio and create new Compose project
2. Define Composable functions
3. Add state with `remember` and `mutableStateOf`
4. Run on emulator or device

## 📦 Dependencies
Install Android Studio

## 🧪 Examples
Input: `Greeting("Android")` → Output: "Hello Android!" displayed

## 🔗 Resources
- [Android Developers](https://developer.android.com/)
- [Examples](./examples/)

## ✅ Validation
1. Project compiles in Android Studio
2. Compose Preview shows UI
3. State updates correctly
