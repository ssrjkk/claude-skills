---
name: react-native-expo
description: Generates React Native applications using Expo and TypeScript. Use for cross-platform mobile development.
category: mobile
tags: [react-native, expo, mobile, typescript]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# React Native Expo

> Cross-platform mobile development with React Native and Expo.

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

## 📋 When to Use
- ✅ Cross-platform mobile apps (iOS + Android)
- ✅ Quick start with Expo managed workflow
- ❌ Not for native modules without Expo

## 🔧 Step-by-Step Instructions
1. Create project: `npx create-expo-app@latest my-app`
2. Write components with React Native API
3. Test on device or simulator
4. Run: `npx expo start`

## 📦 Dependencies
```bash
npx create-expo-app@latest my-app
```

## 🧪 Examples
Input: App launch → Output: "Hello React Native!" displayed

## 🔗 Resources
- [React Native Docs](https://reactnative.dev/)
- [Expo Docs](https://docs.expo.dev/)
- [Examples](./examples/)

## ✅ Validation
1. App runs in simulator/device
2. Hot reload works correctly
3. Styles applied properly
