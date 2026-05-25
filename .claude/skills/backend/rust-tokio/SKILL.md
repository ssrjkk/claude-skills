---
name: rust-tokio
description: Async Rust with Tokio runtime
category: backend
tags: [rust, tokio, async, concurrency, runtime]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Rust Tokio

> Build high-performance async applications in Rust using the Tokio runtime.

## Quick Start
```rust
use tokio::net::TcpListener;
use tokio::io::{AsyncBufReadExt, AsyncWriteExt, BufReader};
use std::sync::Arc;
use tokio::sync::Mutex;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let listener = TcpListener::bind("127.0.0.1:8080").await?;
    let counter = Arc::new(Mutex::new(0u64));

    println!("Server listening on :8080");

    loop {
        let (socket, addr) = listener.accept().await?;
        let counter = counter.clone();
        
        tokio::spawn(async move {
            println!("New connection: {}", addr);
            
            let (reader, mut writer) = socket.into_split();
            let mut buf_reader = BufReader::new(reader);
            let mut line = String::new();

            loop {
                line.clear();
                match buf_reader.read_line(&mut line).await {
                    Ok(0) => break, // EOF
                    Ok(_) => {
                        let response = format!("Echo: {}", line.trim());
                        
                        // Update shared counter
                        let mut count = counter.lock().await;
                        *count += 1;
                        drop(count);

                        if let Err(e) = writer.write_all(response.as_bytes()).await {
                            eprintln!("Write error: {}", e);
                            break;
                        }
                        if let Err(e) = writer.write_all(b"\n").await {
                            eprintln!("Write error: {}", e);
                            break;
                        }
                    }
                    Err(e) => {
                        eprintln!("Read error: {}", e);
                        break;
                    }
                }
            }
            println!("Connection closed: {}", addr);
        });
    }
}
```

```rust
// Async HTTP client
use reqwest;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Concurrent requests with join
    let urls = vec![
        "https://api.example.com/users",
        "https://api.example.com/products",
        "https://api.example.com/orders",
    ];

    let mut handles = Vec::new();
    for url in urls {
        handles.push(tokio::spawn(async move {
            reqwest::get(url).await.unwrap().text().await.unwrap()
        }));
    }

    // Join all concurrent requests
    for handle in handles {
        let result = handle.await?;
        println!("Got response: {} bytes", result.len());
    }

    Ok(())
}
```

## Key Concepts
Tokio is an async runtime for Rust providing I/O, timers, synchronization primitives, and task scheduling. Use `#[tokio::main]` to enter async context. `tokio::spawn` creates concurrent tasks. Use `Mutex`/`RwLock` for shared state.

## When to Use
- High-throughput network services (HTTP servers, proxies)
- Real-time systems (chat, gaming, streaming)
- Concurrent data processing pipelines
- Microservices requiring maximum performance

## Validation
1. `cargo run` starts server without panics
2. Multiple concurrent connections are handled
3. Shared state synchronization is race-condition free
4. Performance benchmarks show expected throughput
