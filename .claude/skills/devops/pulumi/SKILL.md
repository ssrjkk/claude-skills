---
name: pulumi
description: "Provisions cloud infrastructure with Pulumi using TypeScript, Python, Go, or C#. Use for modern IaC with real programming languages."
category: devops
tags: [pulumi, iac, typescript, cloud, infrastructure]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Pulumi

> Infrastructure as code using general-purpose programming languages.

## Quick Start
```typescript
import * as aws from '@pulumi/aws'
const bucket = new aws.s3.Bucket('my-bucket', { website: { indexDocument: 'index.html' } })
export const bucketName = bucket.id
export const bucketUrl = bucket.websiteEndpoint
```

## Resources & Export
```typescript
const cluster = new aws.ecs.Cluster('cluster')
const service = new aws.ecs.Service('service', { cluster: cluster.arn, taskDefinition: taskDef.arn, desiredCount: 2 })
export const serviceArn = service.arn
```

## When to Use
- TypeScript/Python/Go-native IaC
- Complex infrastructure logic
- Cloud-native applications
- Team-familiar languages

## Validation
1. pulumi up completes without errors
2. Resources created correctly
3. pulumi destroy cleans up all resources
