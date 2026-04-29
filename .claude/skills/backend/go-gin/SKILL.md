---
name: go-gin
description: Создает высокопроизводительные HTTP API на Go с использованием фреймворка Gin. Используется для микросервисов, требующих высокой пропускной способности.
category: backend
tags: [go, gin, rest, microservice, high-performance]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Go Gin

> Быстрый HTTP веб-фреймворк для Go с поддержкой middleware и маршрутизации.

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

## 📋 Когда использовать
- ✅ Высоконагруженные API сервисы на Go
- ✅ Микросервисы с минимальными накладными расходами
- ❌ Не использовать для простых скриптов или CLI工具

## 🔧 Пошаговая инструкция
1. Инициализируй Go модуль: `go mod init myapp`
2. Установи Gin: `go get github.com/gin-gonic/gin`
3. Создай `main.go` с маршрутами
4. Запусти: `go run main.go`

## 📦 Зависимости
```bash
go get github.com/gin-gonic/gin
```

## 🧪 Примеры
Input: `GET /ping`
Output: `{"message": "pong"}`

## 🔗 Ресурсы
- [Gin Documentation](https://gin-gonic.com/docs/)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Приложение компилируется без ошибок
2. Сервер отвечает на запросы корректно
3. Middleware работает как ожидается
