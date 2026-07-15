---
name: product-analytics
description: "Implements product analytics with Mixpanel, Amplitude, or PostHog for user behavior tracking."
category: product
tags: [analytics, mixpanel, amplitude, product, metrics]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Product Analytics
> User behavior analytics for product decisions.
## Quick Start (PostHog)
```javascript
import posthog from 'posthog-js'
posthog.init('YOUR_API_KEY', { api_host: 'https://app.posthog.com' })
posthog.capture('signup_completed', { plan: 'premium' })
posthog.identify('user_123', { email: 'alice@example.com' })
```
## Event Taxonomy
```javascript
[Object] [Action] [Context] — e.g., Project Created, Task Completed
Properties: user attributes, timestamps, device info
```
## Funnel Analysis
```javascript
const funnel = [{ event: 'app_opened' }, { event: 'signup_started' }, { event: 'signup_completed' }]
```
## When to Use
- User behavior understanding; Funnel optimization; Feature adoption; Retention analysis
## Validation
1. Events fire correctly in dev tools; 2. Funnel shows drop-offs; 3. User properties captured
