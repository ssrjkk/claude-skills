---
name: framer-motion
description: Creates animations in React with Framer Motion, including layout, gesture, and scroll animations.
category: design
tags: [framer-motion, animation, react, gestures, ui]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Framer Motion
> Production-ready animation library for React.
## Quick Start
```bash
npm install framer-motion
```
```tsx
import { motion } from 'framer-motion'
<motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, scale: 0.5 }}>Content</motion.div>
```
## Gestures & Layout
```tsx
<motion.div whileHover={{ scale: 1.1 }} whileTap={{ scale: 0.9 }} drag="x" dragConstraints={{ left: -100, right: 100 }} />
<AnimatePresence mode="wait">{selected && <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} />}</AnimatePresence>
```
## When to Use
- UI micro-interactions; Page transitions; Gesture-based interactions; Scroll animations
## Validation
1. Animations play without jank; 2. Gestures respond to input; 3. AnimatePresence handles mount/unmount
