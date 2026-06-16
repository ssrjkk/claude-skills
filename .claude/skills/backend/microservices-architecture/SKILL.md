---
name: microservices-architecture
description: Design and implement enterprise-grade microservices architectures with service discovery, load balancing, and distributed tracing
category: backend
tags: [microservices, architecture, backend, distributed-systems, service-discovery]
models: [sonnet, opus]
version: "1.0"
language: en
---

# Microservices Architecture Patterns

## Overview
Design and implement enterprise-grade microservices architectures with service discovery, load balancing, inter-service communication, and distributed tracing.

## Context
You are a backend architect designing scalable microservices systems. You understand service boundaries, data consistency, API contracts, and operational complexity.

## Key Principles
- **Single Responsibility**: Each service handles one business capability
- **Loose Coupling**: Services communicate via well-defined APIs
- **High Cohesion**: Related functionality grouped together
- **Resilience**: Handle failures gracefully
- **Observability**: Track requests across services

## Step-by-Step Instructions

### 1. Service Decomposition
```yaml
Identify Services By:
  - Business capability (user service, order service, payment service)
  - Scalability needs (high-traffic vs low-traffic)
  - Team ownership (one team = one service)
  - Data locality (separate databases)
  - Deployment frequency (how often you update)

Avoid:
  - One service per table
  - Shared database between services
  - Synchronous cycles (Aв†’Bв†’Cв†’A)
```

### 2. Communication Patterns
```
Synchronous:
  - REST API (simple, widely used)
  - gRPC (fast, typed, binary protocol)
  - GraphQL (flexible, single endpoint)

Asynchronous:
  - Message Queue (RabbitMQ, Kafka)
  - Event Bus (async events)
  - Task Queue (Celery, Bull)
```

### 3. Service Discovery
```
Pattern:
  Service A                    Service Registry
    в†“ register                      в†‘
  Service B в†ђ lookup service C    в†ђ register
    в†“ call                      
  Service C
```

### 4. Data Management
```yaml
Pattern: Database per Service
  User Service: users_db (PostgreSQL)
  Order Service: orders_db (PostgreSQL)
  Payment Service: payments_db (MongoDB)

Consistency:
  - Strong: ACID transactions (within service)
  - Eventual: Event-driven (across services)
  - Saga pattern: Distributed transactions
```

### 5. Resilience Patterns
```
Circuit Breaker:
  - Closed: Normal operation
  - Open: Fail fast after threshold
  - Half-open: Test recovery

Retry Logic:
  - Exponential backoff: 1s, 2s, 4s, 8s...
  - Max retries: 3-5 attempts
  - Jitter: Avoid thundering herd

Timeout:
  - Request timeout: 2-5 seconds
  - Service timeout: 10-30 seconds
```

## Real-World Examples

### Example 1: FastAPI Microservice
```python
from fastapi import FastAPI, HTTPException
from httpx import AsyncClient
import logging

app = FastAPI()
logger = logging.getLogger(__name__)

@app.get("/orders/{order_id}")
async def get_order(order_id: str):
    async with AsyncClient() as client:
        try:
            # Call payment service with timeout
            response = await client.get(
                f"http://payment-service/orders/{order_id}",
                timeout=5.0
            )
            response.raise_for_status()
            return response.json()
        except HTTPException as e:
            logger.error(f"Payment service error: {e}")
            raise HTTPException(status_code=503, detail="Service unavailable")
```

### Example 2: Service Discovery with Consul
```python
import consul

# Register service
c = consul.Consul(host='consul.example.com')
c.agent.service.register(
    name='order-service',
    service_id='order-1',
    address='192.168.1.100',
    port=8000,
    check=consul.Check.http(
        'http://192.168.1.100:8000/health',
        interval='10s'
    )
)

# Discover service
_, services = c.health.service('payment-service', passing=True)
for service in services:
    print(f"Service at {service['Service']['Address']}:{service['Service']['Port']}")
```

### Example 3: Event-Driven Communication
```python
from kafka import KafkaProducer, KafkaConsumer
import json

# Producer: Order service publishes event
producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

producer.send('order-created', {
    'order_id': '12345',
    'user_id': 'user-1',
    'total': 99.99,
    'timestamp': '2026-05-23T10:30:00Z'
})

# Consumer: Payment service listens
consumer = KafkaConsumer(
    'order-created',
    bootstrap_servers=['kafka:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    order = message.value
    print(f"Processing order {order['order_id']}")
    # Process payment
```

## Best Practices
- вњ… Define service boundaries carefully
- вњ… Use versioning for API contracts
- вњ… Implement circuit breakers
- вњ… Log request IDs for tracing
- вњ… Monitor service health
- вњ… Use eventual consistency where appropriate
- вњ… Document service APIs
- вќЊ Don't create too many services too early
- вќЊ Don't share databases between services
- вќЊ Don't skip error handling

## Advanced Patterns

### Saga Pattern (Distributed Transactions)
```
Choreography: Services publish events
  Order в†’ OrderCreated в†’ Payment в†’ PaymentProcessed в†’ Inventory

Orchestration: Central coordinator
  OrderService в†’ PaymentOrchestrator в†’ PaymentService
             в†’ InventoryService
             в†’ ShippingService
```

### API Gateway
```
Client
  в†“
API Gateway (authentication, rate limiting, routing)
  в†“
Service 1 | Service 2 | Service 3
```

### Bulkhead Pattern
```
Thread Pool A: User Service (10 threads)
Thread Pool B: Order Service (20 threads)
Thread Pool C: Payment Service (5 threads)
```

## Metrics to Track
- Service latency (p50, p95, p99)
- Error rate per service
- Availability (uptime %)
- Inter-service call count
- Message queue depth

## Common Pitfalls
1. **Too fine-grained services**: Over-engineering
2. **Tight coupling**: Services know too much about each other
3. **Synchronous everywhere**: Poor resilience
4. **No circuit breakers**: Cascading failures
5. **Shared database**: Scalability bottleneck

## Tools & Frameworks
- Spring Boot, Django, FastAPI (service frameworks)
- Docker, Kubernetes (deployment)
- Consul, Eureka (service discovery)
- Kafka, RabbitMQ (messaging)
- Jaeger, Zipkin (distributed tracing)

## Related Skills
- backend-python-async-api
- devops-kubernetes-network-security
- devops-docker-containers-production
- database-postgresql-transactions
