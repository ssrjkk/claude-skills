---
name: stripe-payments
description: "Integrates Stripe payment processing — checkout sessions, subscriptions, webhooks, and customer portals."
category: payments
tags: [stripe, payments, subscriptions, checkout, saas]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Stripe Payments

> Payment processing with Stripe — one-time, subscriptions, and webhooks.

## Quick Start
```javascript
import Stripe from 'stripe';
const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);

// Create checkout session
const session = await stripe.checkout.sessions.create({
  line_items: [{ price: 'price_abc123', quantity: 1 }],
  mode: 'payment',
  success_url: 'https://example.com/success',
  cancel_url: 'https://example.com/cancel',
});

// Handle webhook
app.post('/webhook', express.raw({ type: 'application/json' }), async (req, res) => {
  const sig = req.headers['stripe-signature'];
  const event = stripe.webhooks.constructEvent(req.body, sig, process.env.STRIPE_WEBHOOK_SECRET);
  
  if (event.type === 'checkout.session.completed') {
    const session = event.data.object;
    // Fulfill order
  }
  res.json({ received: true });
});
```

## When to Use
- ✅ One-time payments and subscriptions
- ✅ SaaS billing with recurring revenue
- ❌ Not for crypto payments

## Step-by-Step Instructions
1. Create Stripe account and get API keys
2. Install: `npm install stripe`
3. Create products and prices in Stripe Dashboard
4. Implement checkout sessions and webhooks

## Dependencies
```bash
npm install stripe
# Stripe CLI for webhook testing: https://stripe.com/docs/stripe-cli
```

## Examples
Input: Checkout session created → Output: Customer redirected to Stripe Checkout

## Resources
- [Stripe API Docs](https://stripe.com/docs/api)
- [Examples](./examples/)

## Validation
1. Test mode payments succeed
2. Webhooks receive events
3. Subscriptions renew correctly
