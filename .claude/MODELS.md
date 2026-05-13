# Claude Models Compatibility Matrix

This document shows which Claude models work best with each skill.

## Model Capabilities

| Model | Speed | Context | Best For |
|-------|-------|---------|----------|
| Haiku | Fast | 200K | Simple, repetitive tasks |
| Sonnet | Balanced | 200K | Most skills |
| Opus | Powerful | 200K | Complex reasoning, architecture |

## Skills by Model

### Haiku (Good)
No skills are exclusive to Haiku. Skills compatible with Haiku also work with Sonnet.

### Sonnet (Better)
- accessibility
- airflow-dags
- ansible-automation
- api-testing
- arduino
- astro-ssg
- aws-lambda
- ci-cd-setup
- contract-testing-pact
- cypress-e2e
- data-validation
- database-migration
- design-tokens
- django-rest
- docker-optimization
- dotnet
- e2e-playwright
- electron
- embedding-chunking
- esp32
- etl-pipeline
- figma-plugin
- go-gin
- godot
- graphql-api
- jenkins-pipeline
- laravel
- metrics-dora
- mongodb
- monitoring-prometheus
- mqtt
- nodejs-express
- oauth2-jwt
- performance-k6
- prd-template
- prisma-orm
- python-fastapi
- react-native-expo
- react-typescript
- redis
- remix
- ruby-rails
- sbom-generation
- secrets-management
- security-scan
- selenium-grid
- solidjs
- sprint-retro
- stripe-payments
- supabase
- svelte-kit
- tailwind-css
- tauri
- terraform-aws
- test-reporting
- user-story-mapping
- vue-composition
- web3js

### Opus (Best)
- agent-design
- android-kotlin
- angular-typescript
- argocd-rollback
- compliance-gdpr
- flutter-clean-arch
- gitops-argocd
- huggingface
- ios-swiftui
- java-spring
- k8s-helm-deploy
- kafka-streams
- langchain-rag
- llm-eval
- llm-finetuning
- logging-elk
- ml-model-training
- nextjs-ssr
- pentest-checklist
- prompt-engineering
- security-owasp
- smart-contracts
- solidity
- unity
- unreal
- vector-db-rag

## Recommendation

For most users: **Sonnet** provides the best balance of performance and cost.

For complex tasks (architecture, AI agents): Use **Opus**.

For simple, repetitive tasks: **Haiku** is sufficient.
