---
name: dynamodb
description: "Designs NoSQL tables, writes efficient queries, and manages capacity with AWS DynamoDB. Use for serverless applications at scale."
category: database
tags: [dynamodb, aws, nosql, serverless, database]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# DynamoDB

> AWS NoSQL database with single-digit millisecond performance.

## Quick Start
```javascript
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, PutCommand } from "@aws-sdk/lib-dynamodb";

const client = DynamoDBDocumentClient.from(new DynamoDBClient({}));
await client.send(new PutCommand({
  TableName: "Users",
  Item: { id: "123", name: "Alice", email: "alice@example.com" }
}));
```

## When to Use
- Serverless applications
- High-scale read/write workloads
- Key-value access patterns
- Time-series data

## Step-by-Step
1. Define table with partition key
2. Choose secondary indexes
3. Provision capacity or use on-demand
4. Query with key or index

## Dependencies
```bash
npm install @aws-sdk/client-dynamodb @aws-sdk/lib-dynamodb
```

## Examples
```javascript
const result = await client.send(new QueryCommand({
  TableName: "Users",
  KeyConditionExpression: "id = :id",
  ExpressionAttributeValues: { ":id": "123" }
}));
```

## Resources
- [DynamoDB Docs](https://docs.aws.amazon.com/dynamodb)

## Validation
1. Table creation succeeds
2. Put/Get/Query operations work
3. Capacity matches workload
