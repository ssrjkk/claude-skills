---
name: auth0
description: Integrates Auth0 for authentication, authorization, and user management with social login and MFA.
category: security
tags: [auth0, authentication, authorization, sso, identity]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Auth0
> Authentication and authorization as a service.
## Quick Start
```javascript
import { createAuth0 } from '@auth0/auth0-vue'
const app = createApp(App)
app.use(createAuth0({ domain: 'YOUR_DOMAIN.auth0.com', clientId: 'YOUR_CLIENT_ID', authorizationParams: { redirect_uri: window.location.origin } }))
```
## Login & API Protection
```javascript
const { loginWithRedirect, logout, user, isAuthenticated, getAccessTokenSilently } = useAuth0()
const handleLogin = () => loginWithRedirect({ authorizationParams: { screen_hint: 'signup' } })
const token = await getAccessTokenSilently()
const response = await fetch('/api/protected', { headers: { Authorization: Bearer ${token} } })
```
## When to Use
- Social login (Google, GitHub); Enterprise SSO; MFA; User management
## Validation
1. Auth0 tenant configures correctly; 2. Login flow redirects; 3. API tokens authenticate
