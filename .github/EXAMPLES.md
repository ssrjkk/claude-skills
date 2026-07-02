# Examples: Real-World Usage

This document shows real-world examples of using Claude Skills.

---

## Example 1: Building a REST API with FastAPI

### Scenario
You need to build a production-ready REST API with authentication, database integration, and tests.

### Solution
```
Use skills:
1. backend/fastapi/skill-0045 (FastAPI fundamentals)
2. database/postgresql/skill-0089 (Database design)
3. security/oauth2/skill-0067 (JWT authentication)
4. testing/pytest/skill-0123 (Unit testing)
5. devops/docker/skill-0089 (Containerization)

To build a complete REST API with:
- User registration and login
- CRUD operations for products
- JWT-based authorization
- PostgreSQL persistence
- Comprehensive test coverage
- Docker deployment
```

### What You Get
- Production-ready API code
- Database schema and migrations
- Authentication middleware
- Test suite with 90%+ coverage
- Dockerfile and docker-compose
- CI/CD pipeline

---

## Example 2: Building a React Dashboard

### Scenario
You need a responsive dashboard with real-time data, charts, and authentication.

### Solution
```
Use skills:
1. frontend/react/skill-0089 (React fundamentals)
2. frontend/tailwind/skill-0067 (UI styling)
3. frontend/performance/skill-0045 (Optimization)
4. testing/jest/skill-0123 (Testing)
5. devops/vercel/skill-0089 (Deployment)

Combined with:
- Data visualization libraries
- Real-time updates
- Responsive design
- Accessibility compliance
```

### Implementation
```javascript
// Use skill frontend/react/skill-0089 pattern
import React, { useState, useEffect } from 'react';
import { BarChart } from 'recharts';

export function Dashboard() {
 const [data, setData] = useState([]);
 
 useEffect(() => {
 // Fetch and update data
 }, []);
 
 return (
 <div className="dashboard">
 <BarChart data={data} />
 </div>
 );
}
```

---

## Example 3: Machine Learning Pipeline

### Scenario
You need to build an ML pipeline with data preprocessing, model training, and API serving.

### Solution
```
Use skills:
1. ai-ml/langchain/skill-0089 (LLM integration)
2. ai-ml/pytorch/skill-0045 (Model training)
3. data-engineering/spark/skill-0067(Data processing)
4. database/vector-db/skill-0123 (Embeddings storage)
5. backend/fastapi/skill-0089 (API serving)
6. devops/kubernetes/skill-0045 (Scaling)

To build:
- Data pipeline with Spark
- Fine-tuned ML models
- Vector embeddings storage
- REST API for inference
- Kubernetes deployment
- Monitoring and observability
```

---

## Example 4: Mobile App Development

### Scenario
You're building a cross-platform mobile app with offline support and push notifications.

### Solution
```
Use skills:
1. mobile/react-native/skill-0089 (React Native setup)
2. mobile/offline-first/skill-0045 (Offline storage)
3. mobile/push-notifications/skill-0067 (Push setup)
4. testing/testing-react-native/skill-0123 (Testing)
5. mobile/app-store/skill-0089 (Deployment)

Plus:
- Authentication integration
- Local data caching
- Push notification handling
- App store submissions
```

---

## Example 5: DevOps & Infrastructure

### Scenario
You need to set up a complete CI/CD pipeline with containerization, orchestration, and monitoring.

### Solution
```
Use skills:
1. devops/docker/skill-0089 (Containerization)
2. devops/kubernetes/skill-0045 (Orchestration)
3. devops/terraform/skill-0067 (Infrastructure as Code)
4. devops/github-actions/skill-0123 (CI/CD)
5. monitoring/prometheus/skill-0089 (Monitoring)
6. monitoring/grafana/skill-0045 (Dashboards)

To achieve:
- Automated testing on every commit
- Container building and registry push
- Blue-green deployments
- Auto-scaling based on metrics
- Comprehensive monitoring
- Alerting on failures
```

### Pipeline Flow
```
Git Push
 ↓
GitHub Actions (skill: devops/github-actions)
 ↓
Run Tests (skill: testing/*)
 ↓
Build Image (skill: devops/docker)
 ↓
Push to Registry
 ↓
Deploy to Kubernetes (skill: devops/kubernetes)
 ↓
Health Checks & Monitoring (skill: monitoring/*)
```

---

## Example 6: Security Hardening

### Scenario
You need to audit and harden your application for security.

### Solution
```
Use skills in order:
1. security/owasp/skill-0089 (OWASP Top 10)
2. security/oauth2/skill-0045 (Auth security)
3. security/tls-ssl/skill-0067 (HTTPS/TLS)
4. security/secrets/skill-0123 (Secret management)
5. security/api-security/skill-0089 (API security)
6. infrastructure-security/skill-0045 (Network security)

Audit checklist:
 No SQL injection vulnerabilities
 XSS prevention implemented
 CSRF tokens in place
 Rate limiting configured
 Secrets properly managed
 HTTPS enforced
 Headers secured (CSP, etc.)
 Input validation implemented
 Authentication strong
 Authorization proper
```

---

## Example 7: Performance Optimization

### Scenario
Your application is slow. You need comprehensive performance optimization.

### Solution
```
Use skills:
1. performance/profiling/skill-0089 (Identify bottlenecks)
2. performance/optimization/skill-0045 (General optimization)
3. frontend/performance/skill-0067 (Frontend optimization)
4. backend/caching/skill-0123 (Caching strategies)
5. database/optimization/skill-0089 (Query optimization)
6. devops/cdn/skill-0045 (Content delivery)

Optimization checklist:
 Profile to find bottlenecks
 Optimize hot paths
 Implement caching
 Optimize database queries
 Reduce bundle size
 Implement CDN
 Enable compression
 Lazy load assets
 Monitor in production
```

---

## Example 8: Testing Strategy

### Scenario
You need comprehensive test coverage across your stack.

### Solution
```
Use skills hierarchically:

Unit Tests (skill: testing/jest or testing/pytest)
 ├── Component tests
 ├── Function tests
 └── Module tests

Integration Tests (skill: testing/integration-testing)
 ├── API integration
 ├── Database integration
 └── Service integration

E2E Tests (skill: testing/e2e-testing)
 ├── Critical user flows
 ├── Cross-browser testing
 └── Mobile testing

Load Tests (skill: testing/load-testing)
 ├── Stress testing
 ├── Soak testing
 └── Spike testing

Security Tests (skill: security/vulnerability)
 ├── OWASP compliance
 ├── Injection testing
 └── Authentication testing
```

### Coverage Goals
- Unit: 80%+
- Integration: 60%+
- E2E: Key flows
- Load: Peak load × 2

---

## Example 9: Database Migration

### Scenario
You need to migrate from one database to another with zero downtime.

### Solution
```
Use skills:
1. database/[old-db]/skill-0089 (Export data)
2. database/[new-db]/skill-0045 (Import data)
3. database/migration/skill-0067 (Migration strategy)
4. testing/integration/skill-0123 (Validation)

Strategy:
1. Plan migration (skill: architecture/skill-*)
2. Set up parallel systems
3. Sync data (continuous)
4. Validate completeness
5. Run shadow traffic
6. Cutover at low-traffic window
7. Monitor closely
8. Rollback plan ready
```

---

## Example 10: Building an E-Commerce Platform

### Scenario
You're building a complete e-commerce platform from scratch.

### Solution
```
Use skills in layers:

Frontend Layer:
 - frontend/react or nextjs
 - frontend/tailwind
 - frontend/performance

Backend Layer:
 - backend/fastapi or express
 - ecommerce/checkout (skill-*)
 - ecommerce/inventory (skill-*)
 - payments/stripe or payments/paypal

Database Layer:
 - database/postgresql or mongodb
 - database/redis for caching
 - database/elasticsearch for search

DevOps Layer:
 - devops/docker containerization
 - devops/kubernetes orchestration
 - devops/github-actions CI/CD

Observability Layer:
 - monitoring/prometheus metrics
 - logging/structured logging
 - monitoring/grafana dashboards

Features:
 Product catalog
 Shopping cart
 Checkout process
 Payment integration
 Inventory management
 Order tracking
 Admin dashboard
 Search and filtering
```

---

## Example 11: Real-Time Chat Application

### Scenario
Build a scalable real-time chat system.

### Solution
```
Use skills:
1. backend/websockets/skill-0089 (WebSocket setup)
2. devops/kafka/skill-0045 (Message queue)
3. database/redis/skill-0067 (Caching)
4. frontend/react/skill-0123 (UI)
5. architecture/event-driven/skill-0089 (Architecture)

Features:
 Real-time messaging
 Presence detection
 Message persistence
 Read receipts
 Typing indicators
 Media sharing
 Message search
```

---

## Example 12: Analytics Platform

### Scenario
Build a data analytics platform with real-time dashboards.

### Solution
```
Use skills:
1. data-engineering/spark/skill-0089 (Data processing)
2. database/clickhouse/skill-0045 (OLAP database)
3. frontend/dashboards/skill-0067 (Visualization)
4. devops/kubernetes/skill-0123 (Scaling)

Pipeline:
Data Sources → ETL → ClickHouse → Dashboard
```

---

## Quick Reference: Skill Combinations

| Project Type | Core Skills |
|---|---|
| Web API | backend, database, security, testing, devops |
| Web App | frontend, backend, database, devops |
| Mobile App | mobile, backend, database, devops |
| ML Project | ai-ml, data-engineering, database, devops |
| Data Platform | data-engineering, database, devops, monitoring |
| E-Commerce | frontend, backend, ecommerce, payments, devops |
| Real-time App | backend/websockets, database/redis, devops |
| Full-Stack SaaS | frontend, backend, database, security, devops, billing |

---

## Tips for Success

1. **Start simple** - Use one skill at a time
2. **Build incrementally** - Add features progressively
3. **Test continuously** - Test after each skill application
4. **Monitor always** - Enable monitoring from day 1
5. **Refactor regularly** - Keep code quality high
6. **Document well** - Make it maintainable
7. **Get feedback early** - Share prototypes with users
8. **Plan for scale** - Think about growth early

---

## Need Help?

- [ray013lefe@gmail.com](mailto:ray013lefe@gmail.com)
- [GitHub Discussions](../../discussions)
- [Telegram: @ssrjkk](https://t.me/ssrjkk)

Happy building! 
