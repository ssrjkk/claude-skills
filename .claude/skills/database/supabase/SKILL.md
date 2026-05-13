---
name: supabase
description: Builds apps with Supabase backend — PostgreSQL, auth, real-time subscriptions, and storage. Use as a Firebase alternative.
category: database
tags: [supabase, postgresql, auth, realtime, backend-as-a-service]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Supabase

> Open-source Firebase alternative with PostgreSQL, auth, and real-time.

## Quick Start
```typescript
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  process.env.SUPABASE_URL!,
  process.env.SUPABASE_ANON_KEY!
);

// Query
const { data: users, error } = await supabase
  .from('users')
  .select('*')
  .eq('active', true);

// Real-time subscription
supabase
  .channel('users-changes')
  .on('postgres_changes',
    { event: 'INSERT', schema: 'public', table: 'users' },
    (payload) => console.log('New user:', payload.new)
  )
  .subscribe();
```

## When to Use
- ✅ Rapid backend setup without DevOps
- ✅ Need auth, DB, real-time, storage in one place
- ❌ Not for complex custom backend logic

## Step-by-Step Instructions
1. Create project at supabase.com
2. Install: `npm install @supabase/supabase-js`
3. Set up schema in Supabase Dashboard
4. Configure Row Level Security (RLS)

## Dependencies
```bash
npm install @supabase/supabase-js @supabase/ssr
```

## Examples
Input: `supabase.from('products').select('*').limit(10)` → Output: First 10 products

## Resources
- [Supabase Docs](https://supabase.com/docs)
- [Examples](./examples/)

## Validation
1. Connection to Supabase succeeds
2. RLS policies work correctly
3. Real-time subscriptions receive events
