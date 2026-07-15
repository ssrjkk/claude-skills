---
name: keycloak
description: "Configures Keycloak for identity and access management, including SSO, OAuth2, SAML, and user federation."
category: security
tags: [keycloak, iam, sso, oauth2, authentication]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Keycloak
> Open-source identity and access management with SSO.
## Quick Start
```bash
docker run -d -p 8080:8080 -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:latest start-dev
```
## Client Setup
```json
{"clientId": "my-app", "protocol": "openid-connect", "publicClient": true, "redirectUris": ["http://localhost:3000/*"]}
```
## JS Integration
```javascript
const keycloak = new Keycloak({ url: 'http://localhost:8080', realm: 'my-realm', clientId: 'my-app' })
await keycloak.init({ onLoad: 'login-required' })
```
## When to Use
- Centralized authentication; SSO; Multi-tenant identity; Enterprise IAM
## Validation
1. Admin console loads; 2. Users log in via Keycloak; 3. JWT tokens have correct claims
