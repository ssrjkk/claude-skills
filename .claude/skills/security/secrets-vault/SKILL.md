---
name: secrets-vault
description: Manages secrets with HashiCorp Vault for dynamic secrets, encryption, and access policies.
category: security
tags: [vault, secrets, hashicorp, encryption, security]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# HashiCorp Vault
> Secrets management, encryption, and access control.
## Quick Start
```bash
vault server -dev; export VAULT_ADDR='http://127.0.0.1:8200'; vault login <root-token>
```
## KV & Dynamic Secrets
```bash
vault secrets enable -path=secret kv-v2
vault kv put secret/myapp/config api_key=abc123
vault write database/config/my-db plugin_name=postgresql-database-plugin allowed_roles="readonly" connection_url="postgresql://..."
```
## Policies
```hcl
path "secret/data/myapp/*" { capabilities = ["read", "list"] }
```
## When to Use
- API key storage; Dynamic database credentials; Encryption as a service
## Validation
1. Vault unseals; 2. Secrets read/write correctly; 3. Policies enforce access control
