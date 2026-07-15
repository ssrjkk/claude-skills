---
name: actix-web
description: "Develops high-performance HTTP APIs in Rust with Actix Web, actors, and middleware. Use for maximum throughput web services."
category: backend
tags: [rust, actix-web, async, performance, api]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Actix Web

> Rust's powerful, pragmatic web framework with actor model.

## Quick Start
```rust
use actix_web::{get, web, App, HttpServer, Responder};
#[get("/health")]
async fn health() -> impl Responder { web::Json(json!({"status": "ok"})) }
#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| App::new().service(health))
        .bind(("127.0.0.1", 8080))?.run().await
}
```

## Extractors & State
```rust
use actix_web::web;
use std::sync::Mutex;
struct AppState { counter: Mutex<i32> }
async fn count(data: web::Data<AppState>) -> String {
    let mut c = data.counter.lock().unwrap(); *c += 1; format!("Count: {}", *c)
}
```

## Middleware
```rust
use actix_web::middleware::{Logger, Compress};
HttpServer::new(|| App::new().wrap(Logger::default()).wrap(Compress::default()))
```

## When to Use
- Maximum performance web services
- Rust-native APIs
- Concurrent workloads
- Low-latency requirements

## Validation
1. Server compiles and runs
2. Endpoints return correct status codes
3. Middleware chain executes properly
