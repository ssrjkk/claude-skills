---
name: webassembly
description: WebAssembly with Rust and JS
category: frontend
tags: [webassembly, wasm, rust, javascript, performance]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# WebAssembly

> Build high-performance browser and server applications using WebAssembly with Rust.

## Quick Start
```rust
// src/lib.rs — Rust WASM module
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub struct ImageProcessor {
    width: u32,
    height: u32,
}

#[wasm_bindgen]
impl ImageProcessor {
    pub fn new(width: u32, height: u32) -> Self {
        Self { width, height }
    }

    pub fn grayscale(&self, pixels: &mut [u8]) {
        for chunk in pixels.chunks_mut(4) {
            let gray = (chunk[0] as u32 + chunk[1] as u32 + chunk[2] as u32) / 3;
            chunk[0] = gray as u8;
            chunk[1] = gray as u8;
            chunk[2] = gray as u8;
        }
    }

    pub fn blur(&self, pixels: &mut [u8], width: u32, height: u32) {
        // Simple box blur implementation
        let mut copy = pixels.to_vec();
        for y in 1..height - 1 {
            for x in 1..width - 1 {
                for c in 0..4 {
                    let idx = (y * width + x) * 4 + c;
                    let sum =
                        copy[((y - 1) * width + (x - 1)) * 4 + c] as u32 +
                        copy[((y - 1) * width + x) * 4 + c] as u32 +
                        copy[((y - 1) * width + (x + 1)) * 4 + c] as u32 +
                        copy[(y * width + (x - 1)) * 4 + c] as u32 +
                        copy[(y * width + x) * 4 + c] as u32 +
                        copy[(y * width + (x + 1)) * 4 + c] as u32 +
                        copy[((y + 1) * width + (x - 1)) * 4 + c] as u32 +
                        copy[((y + 1) * width + x) * 4 + c] as u32 +
                        copy[((y + 1) * width + (x + 1)) * 4 + c] as u32;
                    pixels[idx] = (sum / 9) as u8;
                }
            }
        }
    }
}
```

```bash
# Build WASM
wasm-pack build --target web

# NPM package for Node.js
wasm-pack build --target nodejs
```

```javascript
// JavaScript usage
import init, { ImageProcessor } from "./wasm-image-processor.js";

await init();
const processor = ImageProcessor.new(800, 600);
const pixels = new Uint8Array(800 * 600 * 4);
processor.grayscale(pixels); // 10-50x faster than JS
```

## Key Concepts
WASM runs at near-native speed in browsers and Node.js. Rust + wasm-bindgen provides seamless JS interop. Best for compute-intensive tasks: image/video processing, cryptography, games, data compression.

## When to Use
- CPU-intensive computations in the browser
- Porting C/C++/Rust libraries to the web
- Performance-critical paths in web applications
- Game engines and 3D rendering

## Validation
1. `wasm-pack build` compiles without errors
2. WASM module loads and functions execute in browser
3. Performance benchmarks show 5-50x improvement over pure JS
4. Memory is properly managed (no leaks between JS and WASM)
