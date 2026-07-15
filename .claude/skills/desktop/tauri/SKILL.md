---
name: tauri
description: "Builds lightweight, secure desktop applications with Tauri, Rust backend, and web frontend. Use for small, fast native apps."
category: desktop
tags: [tauri, rust, desktop, native, lightweight]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Tauri

> Lightweight desktop apps with Rust backend and web frontend.

## Quick Start
```rust
// src-tauri/src/lib.rs
use tauri::Manager;

#[tauri::command]
fn greet(name: &str) -> String {
    format!("Hello, {}! You're using Tauri.", name)
}

pub fn run() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![greet])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

```typescript
// Frontend (React)
import { invoke } from '@tauri-apps/api/core';

const greeting = await invoke('greet', { name: 'Alice' });
console.log(greeting); // "Hello, Alice! You're using Tauri."
```

## When to Use
- ✅ Lightweight desktop apps (<10MB binaries)
- ✅ Security-focused applications
- ❌ Not for complex native API usage (better Electron)

## Step-by-Step Instructions
1. Install Tauri CLI: `npm install -D @tauri-apps/cli`
2. Init: `npx tauri init`
3. Add Rust commands in `src-tauri/src/lib.rs`
4. Build: `npx tauri build`

## Dependencies
```bash
npm install -D @tauri-apps/cli @tauri-apps/api
# Install Rust: https://www.rust-lang.org/tools/install
```

## Examples
Input: `npx tauri dev` → Output: Native window with hot-reload

## Resources
- [Tauri Docs](https://v2.tauri.app/)
- [Examples](./examples/)

## Validation
1. Dev server launches successfully
2. Rust commands are callable from frontend
3. Build produces single binary
