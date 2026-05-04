---
name: java-spring
description: Generates Spring Boot application structure with REST controllers and JPA repositories. Use for creating enterprise-grade Java applications.
category: backend
tags: [java, spring, spring-boot, rest, jpa]
models: [opus]
version: 1.0.0
created: 2026-04-29
---
# Java Spring Boot

> Enterprise Java framework for production-ready applications with minimal configuration.

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

## 📋 When to Use
- ✅ Enterprise Java applications
- ✅ Need JPA/Hibernate database integration
- ❌ Not for simple scripts or microservices in other languages

## 🔧 Step-by-Step Instructions
1. Generate project via [Spring Initializr](https://start.spring.io)
2. Add dependencies: Spring Web, Spring Data JPA
3. Create controllers and entities
4. Run: `mvn spring-boot:run`

## 📦 Dependencies
```xml
<!-- pom.xml -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

## 🧪 Examples
Input: `GET /api/users/1`
Output: `{"id": 1, "name": "John"}`

## 🔗 Resources
- [Spring Boot Docs](https://spring.io/projects/spring-boot)
- [Examples](./examples/)

## ✅ Validation
1. Application starts without context errors
2. Endpoints accessible and working correctly
3. Database connects successfully (if configured)
