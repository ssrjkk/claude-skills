---
name: ios-swiftui
description: Creates iOS applications using SwiftUI and modern Apple patterns. Use for native iOS development.
category: mobile
tags: [ios, swiftui, swift, apple, mobile]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# iOS SwiftUI

> Modern declarative UI framework for native iOS apps.

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

## 📋 When to Use
- ✅ Native iOS development
- ✅ Modern declarative UI
- ❌ Not for Android or cross-platform

## 🔧 Step-by-Step Instructions
1. Open Xcode and create new SwiftUI project
2. Define View structures with modifiers
3. Add state with `@State` or `@ObservableObject`
4. Run in simulator: Cmd + R

## 📦 Dependencies
Install Xcode from App Store

## 🧪 Examples
Input: Button tap → Counter increments by 1

## 🔗 Resources
- [SwiftUI Docs](https://developer.apple.com/xcode/swiftui/)
- [Examples](./examples/)

## ✅ Validation
1. Project builds in Xcode without errors
2. Preview works correctly
3. State updates reactively
