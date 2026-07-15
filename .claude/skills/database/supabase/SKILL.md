---
name: supabase
description: "Supabase backend-as-a-service"
category: database
tags: [supabase, postgresql, backend, realtime, auth]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Supabase

> Build full-stack applications with Supabase — the open-source Firebase alternative.

## Quick Start
```typescript
// supabase.ts — Client setup and common patterns
import { createClient } from '@supabase/supabase-js';
import { Database } from './database.types'; // Generated types

const supabase = createClient<Database>(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
);

// Type-safe queries
export async function getPosts() {
  const { data, error } = await supabase
    .from('posts')
    .select(`
      *,
      author:profiles(name, avatar_url),
      comments(count)
    `)
    .order('created_at', { ascending: false })
    .limit(20);

  if (error) throw error;
  return data;
}

// Realtime subscriptions
export function subscribeToPost(postId: string) {
  return supabase
    .channel(`post:${postId}`)
    .on(
      'postgres_changes',
      {
        event: '*',
        schema: 'public',
        table: 'comments',
        filter: `post_id=eq.${postId}`,
      },
      (payload) => {
        console.log('New comment:', payload.new);
      }
    )
    .subscribe();
}

// Row Level Security (RLS) policy
/*
-- SQL in Supabase dashboard
CREATE POLICY "Users can only see their own posts"
  ON posts FOR SELECT
  USING (auth.uid() = user_id);

CREATE POLICY "Users can insert their own posts"
  ON posts FOR INSERT
  WITH CHECK (auth.uid() = user_id);
*/

// Server-side with Supabase (Next.js App Router)
export async function getServerSideProps() {
  const supabase = createClient(
    process.env.SUPABASE_URL!,
    process.env.SUPABASE_SERVICE_ROLE_KEY!
  );
  
  const { data } = await supabase.from('products').select('*');
  return { props: { products: data } };
}
```

## Key Concepts
Supabase provides: PostgreSQL database with REST API, authentication, real-time subscriptions, storage, and edge functions. RLS policies secure data at the database level. Type generation from database schema.

## When to Use
- Full-stack apps needing auth, DB, and real-time features
- Projects wanting PostgreSQL without server management
- Real-time collaborative features (chats, live updates)
- MVPs and products needing rapid backend development

## Validation
1. Supabase client connects and authenticates
2. CRUD operations return correct data with RLS enforced
3. Realtime subscriptions receive database changes
4. Type generation matches the database schema exactly
