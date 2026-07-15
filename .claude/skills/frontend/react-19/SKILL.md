---
name: react-19
description: "React 19 features (Actions, use, etc.)"
category: frontend
tags: [react, react-19, hooks, actions, server-components]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# React 19

> Leverage React 19's groundbreaking features including Actions, the `use` hook, and enhanced server components.

## Quick Start
```tsx
// React 19 Actions — form handling made simple
'use client';

import { useActionState } from 'react';
import { createUser } from './actions';

export function SignupForm() {
  // useActionState: pending state, error handling, progressive enhancement
  const [state, formAction, isPending] = useActionState(
    async (prevState: { error?: string }, formData: FormData) => {
      const result = await createUser(formData);
      if (result.error) return { error: result.error };
      return { success: true };
    },
    {}
  );

  return (
    <form action={formAction}>
      <input name="email" type="email" required />
      <input name="password" type="password" required />
      <button type="submit" disabled={isPending}>
        {isPending ? 'Creating...' : 'Sign Up'}
      </button>
      {state.error && <p className="text-red-500">{state.error}</p>}
    </form>
  );
}

// use hook — read async resources in render
import { use } from 'react';

function Comments({ commentsPromise }: { commentsPromise: Promise<Comment[]> }) {
  // Suspends until promise resolves — no useEffect needed
  const comments = use(commentsPromise);
  
  return (
    <ul>
      {comments.map(comment => (
        <li key={comment.id}>{comment.text}</li>
      ))}
    </ul>
  );
}

// Server Actions (App Router)
// app/actions.ts
'use server';

import { revalidatePath } from 'next/cache';

export async function likePost(postId: string) {
  await db.post.update({
    where: { id: postId },
    data: { likes: { increment: 1 } },
  });
  revalidatePath(`/posts/${postId}`);
}
```

## Key Concepts
React 19 introduces: `useActionState` for form handling, `use` hook for reading promises/context in render, Server Actions for mutations, `useOptimistic` for optimistic UI, and refs as props.

## When to Use
- Building forms with pending/error states
- Streaming data with Suspense boundaries
- Server mutations without API route boilerplate
- Optimistic UI patterns

## Validation
1. Actions update form state without manual event handling
2. `use` hook suspends correctly with Suspense boundary
3. Server Actions mutate data and revalidate cache
4. Optimistic updates roll back on error
