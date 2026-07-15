---
name: go-gin
description: "Creates high-performance HTTP APIs on Go using Gin framework. Use for microservices requiring high throughput."
category: backend
tags: [go, gin, rest, microservice, high-performance]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Go Gin

> Fast HTTP web framework for Go with middleware and routing.

## 🚀 Quick Start
```go
package main

import "github.com/gin-gonic/gin"

func main() {
    r := gin.Default()
    
    r.GET("/ping", func(c *gin.Context) {
        c.JSON(200, gin.H{"message": "pong"})
    })
    
    r.Run(":8080")
}
```

## 📋 When to Use
- ✅ High-load API services on Go
- ✅ Microservices with minimal overhead
- ❌ Not for simple scripts or CLI tools

## 🔧 Step-by-Step Instructions
1. Init Go module: `go mod init myapp`
2. Install Gin: `go get github.com/gin-gonic/gin`
3. Create `main.go` with routes
4. Run: `go run main.go`

## 📦 Dependencies
```bash
go get github.com/gin-gonic/gin
```

## 🧪 Examples
Input: `GET /ping`
Output: `{"message": "pong"}`

## 🔗 Resources
- [Gin Documentation](https://gin-gonic.com/docs/)
- [Examples](./examples/)

## ✅ Validation
1. Application compiles without errors
2. Server responds to requests correctly
3. Middleware works as expected
