---
name: ionic
description: Builds cross-platform mobile apps with Ionic, Angular/React/Vue, and Capacitor. Use for hybrid apps with native-like UI.
category: mobile
tags: [ionic, mobile, hybrid, angular, capacitor]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Ionic

> Cross-platform mobile SDK with native-style UI components.

## Quick Start
```bash
npm install -g @ionic/cli
ionic start my-app blank --type=angular
cd my-app && ionic serve
```

## Pages
```typescript
import { Component } from '@angular/core'
@Component({
  selector: 'app-home',
  template: `<ion-header><ion-toolbar><ion-title>Home</ion-title></ion-toolbar></ion-header>
    <ion-content><ion-list><ion-item *ngFor="let item of items">{{ item.name }}</ion-item></ion-list></ion-content>`
})
export class HomePage { items = [{name: 'Item 1'}, {name: 'Item 2'}] }
```

## Navigation
```typescript
import { NavController } from '@ionic/angular'
this.navCtrl.navigateForward('/details', { state: { id: 1 } })
```

## When to Use
- Rapid cross-platform development
- Web-to-mobile conversion
- Enterprise mobile apps
- Prototypes with native feel

## Validation
1. App runs in browser with ionic serve
2. Platform builds succeed for iOS/Android
3. UI components render with correct styling
