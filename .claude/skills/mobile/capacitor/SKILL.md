---
name: capacitor
description: Builds cross-platform mobile apps with Capacitor, bridging web apps to native device features. Use for hybrid mobile development.
category: mobile
tags: [capacitor, mobile, hybrid, ios, android]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Capacitor

> Cross-platform native runtime for web apps with access to device APIs.

## Quick Start
```bash
npm install @capacitor/core @capacitor/cli
npx cap init MyApp com.example.myapp
npx cap add ios
npx cap add android
```

## When to Use
- Web to mobile app migration
- Accessing native device features
- Sharing code across platforms
- Progressive Web Apps to stores

## Step-by-Step
1. Build web app (React, Vue, etc.)
2. Add Capacitor: `npx cap init`
3. Add platforms: `npx cap add ios`
4. Sync: `npx cap sync`

## Dependencies
```bash
npm install @capacitor/core @capacitor/cli @capacitor/ios @capacitor/android
```

## Examples
```javascript
import { Camera } from '@capacitor/camera'

const image = await Camera.getPhoto({
  quality: 90,
  resultType: CameraResultType.Uri
})
```

## Resources
- [Capacitor Docs](https://capacitorjs.com/docs)

## Validation
1. App builds for iOS/Android
2. Native features work (camera, etc.)
3. Hot reload works: `npx cap run ios`
