---
name: platform-engineering
description: "Platform engineering with Backstage/Port"
category: devops
tags: [platform-engineering, backstage, port, developer-portal, internal-developer-platform]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Platform Engineering

> Build internal developer platforms with Backstage and Port for streamlined developer workflows.

## Quick Start
```yaml
# app-config.yaml — Backstage configuration
app:
  title: Internal Developer Platform
  baseUrl: https://developer.example.com

backend:
  baseUrl: https://developer.example.com
  listen:
    port: 7007

organization:
  name: My Company

integrations:
  github:
    - host: github.com
      token: ${GITHUB_TOKEN}

techdocs:
  builder: 'local'
  generators:
    techdocs: 'docker'

catalog:
  rules:
    - allow: [Component, API, Resource, System, Domain]
  locations:
    - type: url
      target: https://github.com/org/service-catalog/blob/main/catalog-info.yaml
      rules:
        - allow: [Component, API]
```

```yaml
# catalog-info.yaml — Service entity definition
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: payment-service
  description: Payment processing service
  annotations:
    github.com/project-slug: org/payment-service
    backstage.io/techdocs-ref: dir:.
    jenkins.io/github-folder: org/payment-service
spec:
  type: service
  lifecycle: production
  owner: platform-team
  system: payment-platform
  dependsOn:
    - resource:default/postgres-main
    - api:default/payment-api
  providesApis:
    - payment-api
  consumedApis:
    - fraud-detection-api
```

## Key Concepts
Platform engineering treats the developer platform as a product. Backstage/Port provide service catalogs, software templates, tech docs, and scorecards. Golden paths reduce cognitive load on developers.

## When to Use
- Organizations with 10+ microservices needing standardized management
- Teams spending too much time on infrastructure configuration
- Standardizing deployment workflows and environments
- Improving developer experience and reducing onboarding time

## Validation
1. Backstage/Port starts and renders the service catalog
2. Software templates create repositories with correct scaffolding
3. TechDocs renders documentation from code repositories
4. Scorecards track service maturity metrics
