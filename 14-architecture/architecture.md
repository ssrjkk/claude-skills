# Architecture

## Well-Architected

**What it is**  
Framework от AWS для проектирования инфры. 

**Why it matters**  
5 pillars: operational excellence, security, reliability, performance, cost. 

**Must know**  
Каждый pillar имеет design principles. 

**Must be able to do**  
Пройти Well-Architected review. 

**Where it is used**  
Проектирование любой инфры. 

**Trade-offs**  
+Best practices. -Время на review. 

**Common mistakes**  
Игнорирование security pillar. 

**Interview check**  
Q: 5 pillars? A: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization. 

**Mini example**  
Review: Security pillar -> enable MFA, encrypt data.

## Patterns

**What it is**  
Типовые решения (microservices, event-driven, etc). 

**Why it matters**  
Проверенные подходы. 

**Must know**  
Microservices, monolith, event-driven, serverless. 

**Must be able to do**  
Выбрать паттерн под задачу. 

**Where it is used**  
Проектирование систем. 

**Trade-offs**  
Зависит от паттерна. 

**Common mistakes**  
Microservices для простого приложения. 

**Interview check**  
Q: Event-driven pattern? A: Компоненты общаются через events (SQS, SNS). 

**Mini example**  
E-commerce: order placed -> SQS -> inventory service.

## Anti-Patterns

**What it is**  
Чего НЕ делать. 

**Why it matters**  
Избежание типичных ошибок. 

**Must know**  
Manual changes, single AZ, no backups, hardcoded secrets. 

**Must be able to do**  
Определить anti-pattern в инфре. 

**Where it is used**  
Все системы. 

**Trade-offs**  
+Надежность. -Нужно знать. 

**Common mistakes**  
Игнорирование anti-patterns. 

**Interview check**  
Q: Anti-pattern? A: Практика, которая приводит к проблемам. 

**Mini example**  
Manual deploy вместо CI/CD.