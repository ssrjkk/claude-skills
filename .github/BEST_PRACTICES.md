# Best Practices for Using Claude Skills

## Overview

This guide covers best practices, patterns, and tips for getting maximum value from Claude Skills.

---

## 1. Skill Selection

### Choose the Right Skill
```
 Bad: "Build an API"
 Good: "Use skill backend/fastapi/skill-0089 to build a REST API with JWT auth"
```

### Know Your Domain
- Spend 15 minutes browsing [.claude/skills/INDEX.md](.claude/skills/INDEX.md)
- Identify 3-5 skills relevant to your project
- Bookmark them for quick reference

### Match Skill to Your Tech Stack
```
For Python backend? → backend/fastapi or backend/django
For Node.js? → backend/express or backend/fastify
For React frontend? → frontend/react
For Kubernetes deployment? → devops/kubernetes
```

---

## 2. Prompting Patterns

### Pattern 1: Single Skill Reference
```
Use skill backend/fastapi/skill-0045 to implement:
- User registration endpoint
- Input validation
- Error handling
- Proper logging
```

### Pattern 2: Skill Combination
```
Use skills:
1. backend/fastapi/skill-0089
2. database/postgresql/skill-0156
3. security/oauth2/skill-0042

To build a complete authentication system with:
- Secure password storage
- JWT token management
- Refresh token rotation
- Rate limiting on login
```

### Pattern 3: Skill Adaptation
```
From skill database/postgresql/skill-0123 (JSON querying), 
show me the advanced pattern and adapt it for:
[Your specific use case]
```

### Pattern 4: Cross-Domain Integration
```
Take the architecture from skill architecture/microservices/skill-0078
and implement it using:
- backend/fastapi (API layer)
- database/postgres (Data)
- devops/docker (Containerization)
- devops/kubernetes (Orchestration)
```

---

## 3. Code Quality

### Always Include Tests
```
"Use skill backend/fastapi/skill-0045 to build [feature]
AND use skill testing/pytest/skill-0089 to test it completely"
```

### Request Error Handling
```
"Include comprehensive error handling covering:
- Input validation errors
- Database connection failures
- Timeout scenarios
- Permission denied cases"
```

### Demand Documentation
```
"Include clear docstrings and comments for all functions
following the style from skill engineering/code-review/skill-0067"
```

### Performance First
```
"Use the optimization patterns from skill performance/skill-0089
to ensure this scales to 1M+ users"
```

---

## 4. Security Best Practices

### Always Request Security Review
```
"Implement this using security patterns from:
- skill security/oauth2/skill-0042
- skill security/tls-ssl/skill-0089
- skill security/owasp/skill-0123"
```

### Validate Inputs
```
"Include input validation as shown in 
skill backend/fastapi/skill-0067 (request validation)"
```

### Handle Secrets
```
"Use the secrets management pattern from 
skill security/secrets/skill-0045"
```

### Assume Breach
```
"Follow zero-trust security principles from 
skill infrastructure-security/zero-trust/skill-0089"
```

---

## 5. Architecture Decisions

### For APIs
```
Use skills in this order:
1. architecture/api/skill-* (design)
2. backend/[framework]/skill-* (implementation)
3. database/skill-* (persistence)
4. testing/skill-* (validation)
5. devops/skill-* (deployment)
```

### For Web Applications
```
Use skills:
1. frontend/[framework]/skill-* (UI)
2. backend/[framework]/skill-* (API)
3. devops/docker/skill-* (containers)
4. devops/github-actions/skill-*(CI/CD)
```

### For Data Systems
```
Use skills:
1. data-engineering/skill-* (pipelines)
2. database/skill-* (storage)
3. monitoring/skill-* (observability)
4. devops/kubernetes/skill-* (orchestration)
```

### For ML Systems
```
Use skills:
1. ai-ml/[framework]/skill-* (model)
2. database/vector-db/skill-* (embeddings)
3. devops/kubernetes/skill-* (serving)
4. monitoring/skill-* (metrics)
```

---

## 6. Testing Strategy

### Unit Tests
```
"Use skill testing/jest/skill-0045 for frontend
or skill testing/pytest/skill-0089 for backend
to write unit tests for [component]"
```

### Integration Tests
```
"Use skill testing/integration-testing/skill-0067
to test the interaction between:
[list your components]"
```

### End-to-End Tests
```
"Use skill testing/e2e-testing/skill-0123
to write E2E tests using Playwright covering:
[user journeys]"
```

### Load Testing
```
"Use skill testing/load-testing/skill-0045
to load test [endpoint] for:
- 10,000 concurrent users
- 100 requests/second
- Network failures"
```

---

## 7. Performance Optimization

### Frontend Performance
```
"Use skill performance/optimization/skill-0089
and skill frontend/performance/skill-0045
to optimize [component] for:
- First Contentful Paint < 1s
- Largest Contentful Paint < 2.5s
- Cumulative Layout Shift < 0.1"
```

### Backend Performance
```
"Use skill performance/profiling/skill-0067
to profile [endpoint] and optimize for:
- Sub-100ms response times
- <50MB memory usage
- <10ms database queries"
```

### Database Performance
```
"Use skill database/optimization/skill-0123
to optimize [query]:
- Add appropriate indexes
- Use query plan analysis
- Implement caching where needed"
```

---

## 8. Deployment Strategy

### Development
```
Use skill devops/docker/skill-0045
to containerize your application
```

### Testing
```
Use skill devops/docker/skill-0067
with skill devops/github-actions/skill-0089
to run automated tests
```

### Staging
```
Use skill devops/kubernetes/skill-0123
to deploy staging environment
```

### Production
```
Use skill devops/kubernetes/skill-0156
with skill monitoring/skill-0089
for production deployment and monitoring
```

---

## 9. Monitoring & Observability

### Logging
```
"Use skill logging/structured/skill-0045
to implement structured logging for [service]:
- Request tracking
- Error details
- Performance metrics"
```

### Metrics
```
"Use skill monitoring/apm/skill-0089
to monitor [service]:
- Response time percentiles
- Error rates
- Resource utilization"
```

### Alerting
```
"Use skill monitoring/alerts/skill-0123
to set up alerts for:
- P99 latency > 1s
- Error rate > 1%
- CPU > 80%"
```

---

## 10. Skill Combinations

### Recommended Combinations

#### Full-Stack Web App
```
frontend/react/skill-0089
+ backend/fastapi/skill-0123
+ database/postgresql/skill-0045
+ testing/jest/skill-0067
+ testing/pytest/skill-0089
+ devops/docker/skill-0045
+ devops/github-actions/skill-0067
```

#### Real-Time System
```
backend/websockets/skill-0045
+ devops/kafka/skill-0089
+ database/redis/skill-0067
+ monitoring/skill-0123
+ devops/kubernetes/skill-0045
```

#### ML Pipeline
```
ai-ml/langchain/skill-0089
+ ai-ml/pytorch/skill-0045
+ database/vector-db/skill-0123
+ data-engineering/spark/skill-0067
+ devops/kubernetes/skill-0089
+ monitoring/observability/skill-0045
```

#### Microservices Architecture
```
architecture/microservices/skill-0089
+ backend/fastapi/skill-0045 (for each service)
+ database/postgresql/skill-0067
+ devops/docker/skill-0123
+ devops/kubernetes/skill-0045
+ communications/skill-0067
+ monitoring/skill-0089
```

---

## 11. Common Mistakes to Avoid

### Mistake 1: Ignoring Skill Dependencies
```
Wrong: Use skill frontend/react/skill-0045 without setup
Right: Set up build system first, then use the skill
```

### Mistake 2: Skipping Error Handling
```
Wrong: Copy code example without adding error handling
Right: Request error handling AND tests
```

### Mistake 3: Not Testing
```
Wrong: Deploy without tests
Right: Use testing skills before deployment
```

### Mistake 4: Ignoring Performance
```
Wrong: Ship without optimization
Right: Use performance skills to optimize first
```

### Mistake 5: Security Shortcuts
```
Wrong: Skip authentication/authorization
Right: Use security skills from day one
```

---

## 12. Tips for Maximum Productivity

### Tip 1: Know Your Tech Stack
```
Pick 5 core skills for your stack and master them.
Example:
- backend/fastapi/skill-0045
- frontend/react/skill-0089
- database/postgresql/skill-0123
- testing/pytest/skill-0067
- devops/docker/skill-0089
```

### Tip 2: Build Incrementally
```
1. Use skill for core feature
2. Add tests with testing skill
3. Optimize with performance skill
4. Deploy with devops skill
```

### Tip 3: Create a Checklist
```
Before shipping:
 Used appropriate skill
 Included tests
 Added error handling
 Optimized performance
 Implemented security
 Added logging
 Documented code
```

### Tip 4: Reference Patterns
```
Before each feature, check if there's a skill.
Keep the skill file open while coding.
Follow the patterns exactly.
```

### Tip 5: Share Knowledge
```
After using a skill successfully:
- Share with team
- Document learnings
- Contribute improvements
```

---

## 13. Troubleshooting

### Problem: "Claude isn't following the skill"
**Solution**: Include the full path and be explicit
```
"Use skill backend/fastapi/skill-0045 to build..."
(not "use the fastapi skill")
```

### Problem: "The code doesn't work"
**Solution**: Ask Claude to validate
```
"Show me the complete working example from skill X"
```

### Problem: "Missing functionality"
**Solution**: Combine skills
```
"Use skill A and skill B together to..."
```

### Problem: "Performance issues"
**Solution**: Use performance skills
```
"Use skill performance/skill-0089 to optimize this"
```

---

## 14. Contribution Tips

### When to Create a Skill
- You've solved a problem 3+ times
- It takes >30 minutes to implement
- It has best practices to share

### How to Share a Skill
```bash
python scripts/create-skill.py --domain backend --category fastapi
# Edit the skill file
python scripts/validate-all.py
# Submit PR
```

---

## Quick Reference

| Task | Skill |
|------|-------|
| Create REST API | backend/fastapi/skill-* |
| Build React UI | frontend/react/skill-* |
| Setup Postgres | database/postgresql/skill-* |
| Write Tests | testing/pytest/skill-* |
| Deploy to Docker | devops/docker/skill-* |
| Setup Kubernetes | devops/kubernetes/skill-* |
| Implement Auth | security/oauth2/skill-* |
| Monitor System | monitoring/apm/skill-* |
| Optimize Code | performance/optimization/skill-* |

---

## Resources

- [Getting Started](.github/GETTING_STARTED.md)
- [Full Catalog](.claude/skills/INDEX.md)
- [Contributing](.github/CONTRIBUTING.md)
- [FAQ](.github/FAQ.md)
- [Examples](.github/EXAMPLES.md)

---

**These best practices will help you get 3x more value from Claude Skills! **
