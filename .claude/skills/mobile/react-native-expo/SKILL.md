---
name: react-native-expo
description: Генерирует React Native приложения с использованием Expo и TypeScript. Используется для кроссплатформенной мобильной разработки.
category: mobile
tags: [react-native, expo, mobile, typescript]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# React Native Expo

> Кроссплатформенная мобильная разработка с React Native и Expo.

## 🚀 Quick Start
```typescript
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';

export default function App() {
    return (
        <View style={styles.container}>
            <Text>Hello React Native!</Text>
            <StatusBar style="auto" />
        </View>
    );
}

const styles = StyleSheet.create({
    container: { flex: 1, alignItems: 'center', justifyContent: 'center' }
});
```

## 📋 Когда использовать
- ✅ Кроссплатформенные мобильные приложения (iOS + Android)
- ✅ Быстрый старт с Expo managed workflow
- ❌ Не использовать для нативных модулей без Expo

## 🔧 Пошаговая инструкция
1. Создай проект: `npx create-expo-app@latest my-app`
2. Напиши компоненты с React Native API
3. Тестируй на устройстве или симуляторе
4. Запусти: `npx expo start`

## 📦 Зависимости
```bash
npx create-expo-app@latest my-app
```

## 🧪 Примеры
Input: Запуск приложения → отображается "Hello React Native!"

## 🔗 Ресурсы
- [React Native Docs](https://reactnative.dev/)
- [Expo Docs](https://docs.expo.dev/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Приложение запускается в симуляторе/устройстве
2. Hot reload работает корректно
3. Стили применяются правильно
