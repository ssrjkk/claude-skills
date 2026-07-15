---
name: circleci
description: "Configures CI/CD pipelines with CircleCI using orbs, workspaces, and parallelism. Use for automating builds, tests, and deployments."
category: devops
tags: [circleci, ci-cd, pipelines, automation, devops]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# CircleCI

> Continuous integration and delivery platform with powerful pipeline configuration.

## Quick Start
```yaml
version: 2.1
jobs:
  build:
    docker:
      - image: cimg/node:20.0
    steps:
      - checkout
      - run: npm ci
      - run: npm test
workflows:
  version: 2
  test:
    jobs:
      - build
```

## When to Use
- Automated testing on every commit
- Multi-environment deployments
- Parallel test execution
- Docker image builds

## Step-by-Step
1. Add `.circleci/config.yml` to repo
2. Configure jobs and workflows
3. Set environment variables in UI
4. Push to trigger pipeline

## Dependencies
```bash
# Local validation
circleci local execute --job build
```

## Examples
```yaml
jobs:
  deploy:
    docker:
      - image: cimg/python:3.11
    steps:
      - checkout
      - run: pip install -r requirements.txt
      - run: python deploy.py
```

## Resources
- [CircleCI Docs](https://circleci.com/docs)

## Validation
1. Pipeline triggers on git push
2. All jobs pass successfully
3. Artifacts are accessible
