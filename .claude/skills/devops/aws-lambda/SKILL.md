---
name: aws-lambda
description: Builds and deploys serverless functions with AWS Lambda, API Gateway, and SAM/CDK. Use for event-driven architectures.
category: devops
tags: [aws, lambda, serverless, api-gateway, sam]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# AWS Lambda

> Serverless functions with AWS Lambda, API Gateway, and event triggers.

## Quick Start
```typescript
import { Handler, APIGatewayProxyEvent, APIGatewayProxyResult } from 'aws-lambda';

export const handler: Handler = async (event: APIGatewayProxyEvent): Promise<APIGatewayProxyResult> => {
  return {
    statusCode: 200,
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      message: 'Hello from Lambda!',
      path: event.path,
      method: event.httpMethod,
    }),
  };
};
```

```yaml
# template.yaml (SAM)
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  HelloFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: src/
      Handler: index.handler
      Runtime: nodejs20.x
      Events:
        Api:
          Type: Api
          Properties:
            Path: /hello
            Method: GET
```

## When to Use
- ✅ Event-driven serverless APIs
- ✅ Background processing (resize images, send emails)
- ❌ Not for long-running processes (>15 min)

## Step-by-Step Instructions
1. Install AWS SAM CLI
2. Create SAM template with Lambda functions
3. Write handler code
4. Deploy: `sam deploy --guided`

## Dependencies
```bash
# Install AWS SAM CLI
# https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html
npm install aws-lambda @types/aws-lambda
```

## Examples
Input: GET /hello → Output: `{ "message": "Hello from Lambda!" }`

## Resources
- [AWS Lambda Docs](https://docs.aws.amazon.com/lambda/)
- [Examples](./examples/)

## Validation
1. Function deploys successfully
2. API Gateway endpoint responds
3. CloudWatch logs show execution
