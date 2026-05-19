---
name: firebase
description: Builds serverless applications with Firebase, including Firestore, Auth, Cloud Functions, and Realtime Database.
category: database
tags: [firebase, google, serverless, realtime, auth]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Firebase

> Google's app development platform with backend services.

## Quick Start
```javascript
import { initializeApp } from 'firebase/app'
import { getFirestore, collection, addDoc, getDocs, query, where } from 'firebase/firestore'
const app = initializeApp({ /* config */ })
const db = getFirestore(app)
await addDoc(collection(db, 'users'), { name: 'Alice', email: 'alice@example.com' })
const q = query(collection(db, 'users'), where('name', '==', 'Alice'))
const snap = await getDocs(q)
```

## Auth & Functions
```javascript
import { getAuth, signInWithPopup, GoogleAuthProvider } from 'firebase/auth'
const auth = getAuth(app)
const result = await signInWithPopup(auth, new GoogleAuthProvider())
```

## When to Use
- Rapid prototyping
- Real-time collaborative apps
- Mobile app backends
- Serverless architectures

## Validation
1. Firebase app initializes
2. Firestore read/write operations succeed
3. Auth providers authenticate users
