# Claude Models Compatibility Matrix

This document shows which Claude models work best with each skill.

## Model Capabilities

| Model | Speed | Context | Best For |
|-------|-------|---------|----------|
| Haiku | ⚡⚡⚡ | 200K | Simple, repetitive tasks |
| Sonnet | ⚡⚡ | 200K | Balanced - most skills |
| Opus | ⚡ | 200K | Complex reasoning, architecture |

## Skills by Model

### ✅ Haiku (Good)
- api-testing
- database-migration
- ci-cd-setup
- nodejs-express
- test-reporting

### ✅✅ Sonnet (Better)
- python-fastapi
- react-typescript
- vue-composition
- nextjs-ssr
- svelte-kit
- angular-typescript
- astro-ssg
- docker-optimization
- terraform-aws
- ansible-automation
- gitops-argocd
- argocd-rollback
- security-scan
- etl-pipeline
- data-validation
- airflow-dags
- embedding-chunking
- e2e-playwright
- contract-testing-pact
- performance-k6
- security-owasp
- selenium-grid
- cypress-e2e
- metrics-dora
- prd-template
- sprint-retro
- user-story-mapping
- secrets-management
- sbom-generation
- pentest-checklist
- compliance-gdpr
- web3js
- godot
- esp32
- arduino
- mqtt
- figma-plugin
- design-tokens
- accessibility

### ✅✅✅ Opus (Best)
- java-spring
- go-gin
- django-rest
- laravel
- flutter-clean-arch
- react-native-expo
- ios-swiftui
- android-kotlin
- k8s-helm-deploy
- monitoring-prometheus
- logging-elk
- jenkins-pipeline
- ml-model-training
- vector-db-rag
- kafka-streams
- prompt-engineering
- llm-eval
- agent-design
- solidity
- smart-contracts
- unity
- unreal

## Recommendation

For most users: **Sonnet** provides the best balance of performance and cost.

For complex tasks (architecture, AI agents): Use **Opus**.

For simple, repetitive tasks: **Haiku** is sufficient.
