---
name: paddle
description: "Integrates Paddle for SaaS payment processing, subscriptions, and checkout management."
category: payments
tags: [paddle, payments, subscriptions, saas, billing]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Paddle
> SaaS payment platform for global subscription billing.
## Quick Start
```javascript
import { initializePaddle } from '@paddle/paddle-js'
const paddle = await initializePaddle({ token: 'YOUR_CLIENT_TOKEN', environment: 'sandbox' })
paddle.Checkout.open({ items: [{ priceId: 'pri_123', quantity: 1 }] })
```
## Webhooks
```javascript
app.post('/webhooks/paddle', express.raw({type: 'application/json'}), (req, res) => {
  const event = req.body
  if (event.event_type === 'transaction.completed') {
    // Fulfill order
  }
  res.send('OK')
})
```
## When to Use
- SaaS subscription billing; Global payments; Tax and compliance handling
## Validation
1. Checkout opens correctly; 2. Webhook events received; 3. Subscription lifecycle works
