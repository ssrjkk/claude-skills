---
name: secrets-management
description: Manages application secrets with HashiCorp Vault or AWS Secrets Manager. Use for secure credential storage.
category: security
tags: [secrets, vault, security, credentials]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# Secrets Management

> Secure storage and rotation of application secrets.

## Quick Start
```bash
# Vault: write secret
vault kv put secret/myapp api_key=12345

# Vault: read secret
vault kv get secret/myapp
```

## When to Use
- ✅ Storing API keys, DB passwords
- ✅ Secret rotation
- ❌ Not for storing user files

## Step-by-Step Instructions
1. Deploy Vault or setup AWS Secrets Manager
2. Define access policies
3. Integrate secret reading into application
4. Setup rotation

## Dependencies
```bash
# Vault
brew install vault
# AWS CLI
pip install awscli
```

## Examples
Input: `vault kv get secret/myapp` → Output: `api_key=12345`

## Resources
- [Vault Docs](https://www.vaultproject.io/docs)
- [Examples](./examples/)

## Validation
1. Secrets read by application without errors
2. Access restricted by policies
3. Rotation happens without downtime
