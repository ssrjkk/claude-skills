---
name: react-native-bare
description: "Develops React Native applications without Expo, using native modules, libraries, and custom builds. Use for advanced RN projects."
category: mobile
tags: [react-native, mobile, native-modules, typescript, ios]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# React Native (Bare)

> React Native without Expo — full control over native code.

## Quick Start
```bash
npx react-native init MyApp --template react-native-template-typescript
cd MyApp && npx react-native run-ios
```

## Native Modules (iOS)
```objectivec
// MyModule.m
#import <React/RCTBridgeModule.h>
@interface RCT_EXTERN_MODULE(MyModule, NSObject)
RCT_EXTERN_METHOD(doSomething:(NSString *)input resolver:(RCTPromiseResolveBlock)resolve rejecter:(RCTPromiseRejectBlock)reject)
@end
```

## Third-Party Libraries
```bash
npm install react-native-vision-camera react-native-reanimated react-native-gesture-handler
cd ios && pod install
```

## When to Use
- Custom native module requirements
- Maximum performance control
- Existing native codebases
- Complex native integrations

## Validation
1. App builds for iOS and Android
2. Native modules link correctly
3. Metro bundler starts without errors
