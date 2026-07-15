---
name: serverless-ai
description: "Serverless AI inference (Cloudflare Workers, Lambda)"
category: devops
tags: [serverless, ai, inference, cloudflare-workers, lambda, edge]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Serverless AI

> Run AI inference at the edge with serverless platforms like Cloudflare Workers and AWS Lambda.

## Quick Start
```typescript
// Cloudflare Workers AI — edge inference
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const { pathname } = new URL(request.url);

    if (pathname === "/generate") {
      const { prompt } = await request.json() as { prompt: string };
      
      const response = await env.AI.run("@cf/meta/llama-3.2-3b-instruct", {
        prompt: prompt,
        max_tokens: 500,
        temperature: 0.7
      });

      return Response.json(response);
    }

    // Text embeddings
    if (pathname === "/embed") {
      const { text } = await request.json() as { text: string | string[] };
      const embeddings = await env.AI.run("@cf/baai/bge-base-en-v1.5", {
        text: Array.isArray(text) ? text : [text]
      });
      return Response.json(embeddings);
    }

    return new Response("Not found", { status: 404 });
  }
};
```

```python
# AWS Lambda with SageMaker
import boto3
import json
import os

sagemaker = boto3.client("sagemaker-runtime")
ENDPOINT_NAME = os.environ["ENDPOINT_NAME"]

def lambda_handler(event, context):
    body = json.loads(event["body"])
    
    response = sagemaker.invoke_endpoint(
        EndpointName=ENDPOINT_NAME,
        ContentType="application/json",
        Body=json.dumps({
            "inputs": body["prompt"],
            "parameters": {
                "max_new_tokens": 200,
                "temperature": 0.7
            }
        })
    )
    
    result = json.loads(response["Body"].read().decode())
    return {
        "statusCode": 200,
        "body": json.dumps({"response": result})
    }
```

## Key Concepts
Serverless AI trades cold starts for zero idle cost. Cloudflare Workers run inference at the edge (near users). Lambda with SageMaker provides scalable GPU inference. Best for lightweight models and on-demand workloads.

## When to Use
- Lightweight inference (< 3B parameter models)
- Variable workloads with unpredictable traffic
- Edge-based applications (low latency requirements)
- Prototyping and low-cost deployments

## Validation
1. Function deploys and responds to requests
2. Cold start latency is acceptable for the use case
3. Inference quality matches expectations for the model size
4. Cost is lower than always-on GPU instances for variable traffic
