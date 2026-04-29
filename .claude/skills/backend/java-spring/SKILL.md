---
name: java-spring
description: Генерирует структуру Spring Boot приложений с REST контроллерами и JPA репозиториями. Используется для создания enterprise-grade Java приложений.
category: backend
tags: [java, spring, spring-boot, rest, jpa]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# Java Spring Boot

> Enterprise Java framework для создания production-ready приложений с минимальной конфигурацией.

## 🚀 Quick Start
```java
@RestController
@RequestMapping("/api/users")
public class UserController {
    
    @GetMapping("/{id}")
    public ResponseEntity<User> getUser(@PathVariable Long id) {
        return ResponseEntity.ok(new User(id, "John"));
    }
}

@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

## 📋 Когда использовать
- ✅ Enterprise Java приложения
- ✅ Нужна интеграция с БД через JPA/Hibernate
- ❌ Не использовать для простых скриптов или микросервисов на других языках

## 🔧 Пошаговая инструкция
1. Сгенерируй проект через [Spring Initializr](https://start.spring.io)
2. Добавь зависимости: Spring Web, Spring Data JPA
3. Создай контроллеры и сущности
4. Запусти: `mvn spring-boot:run`

## 📦 Зависимости
```xml
<!-- pom.xml -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

## 🧪 Примеры
Input: `GET /api/users/1`
Output: `{"id": 1, "name": "John"}`

## 🔗 Ресурсы
- [Spring Boot Docs](https://spring.io/projects/spring-boot)
- [Примеры кода](./examples/)

## ✅ Валидация
1. Приложение запускается без ошибок контекста
2. Эндпоинты доступны и работают корректно
3. БД подключается успешно (если настроена)
