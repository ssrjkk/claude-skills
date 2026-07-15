---
name: go-generics
description: "Go generics patterns and best practices"
category: backend
tags: [go, golang, generics, types, patterns]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Go Generics

> Write type-safe, reusable Go code with generics — patterns and best practices.

## Quick Start
```go
package main

import (
	"cmp"
	"fmt"
	"slices"
)

// Generic data structures
type Stack[T any] struct {
	items []T
}

func (s *Stack[T]) Push(item T) {
	s.items = append(s.items, item)
}

func (s *Stack[T]) Pop() (T, bool) {
	if len(s.items) == 0 {
		var zero T
		return zero, false
	}
	item := s.items[len(s.items)-1]
	s.items = s.items[:len(s.items)-1]
	return item, true
}

// Generic utility functions
func Map[T, U any](input []T, fn func(T) U) []U {
	result := make([]U, len(input))
	for i, v := range input {
		result[i] = fn(v)
	}
	return result
}

func Filter[T any](input []T, fn func(T) bool) []T {
	var result []T
	for _, v := range input {
		if fn(v) {
			result = append(result, v)
		}
	}
	return result
}

func Reduce[T, U any](input []T, initial U, fn func(U, T) U) U {
	result := initial
	for _, v := range input {
		result = fn(result, v)
	}
	return result
}

// Type constraints
type Number interface {
	~int | ~int64 | ~float64
}

func Sum[T Number](values []T) T {
	var sum T
	for _, v := range values {
		sum += v
	}
	return sum
}

// Constraint with ordering
func Max[T cmp.Ordered](a, b T) T {
	if a > b {
		return a
	}
	return b
}

func main() {
	// Usage
	ints := []int{1, 2, 3, 4, 5}
	doubled := Map(ints, func(i int) int { return i * 2 })
	fmt.Println(doubled) // [2, 4, 6, 8, 10]

	stack := Stack[string]{}
	stack.Push("hello")
	stack.Push("world")
	val, _ := stack.Pop()
	fmt.Println(val) // "world"

	// Using standard library generics
	names := []string{"alice", "bob", "charlie"}
	slices.Sort(names)
	fmt.Println(names) // [alice bob charlie]
}
```

## Key Concepts
Go 1.18+ supports type parameters `[T any]`, type constraints (interfaces with type sets), and type inference. Use generics for data structures and algorithms, not for everything. Keep it simple.

## When to Use
- Collection types (Stack, Queue, Tree, Graph)
- Functional patterns (Map, Filter, Reduce)
- Type-safe wrappers around serialization/DB operations
- Reducing code duplication for similar implementations

## Validation
1. Code compiles with `go build` (Go 1.18+)
2. Type inference works without explicit type parameters where expected
3. Generic functions work with multiple concrete types
4. Interface constraints correctly restrict allowed types
