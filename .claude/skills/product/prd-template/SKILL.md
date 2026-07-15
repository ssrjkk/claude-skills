---
name: prd-template
description: "Generates structured PRD (Product Requirements Document) with goals, features, and success criteria. Use for documenting requirements."
category: product
tags: [prd, product, requirements, documentation]
models: [sonnet, opus]
version: 1.0.0
created: 2026-04-29
---
# PRD Template

> Product Requirements Document template for structuring requirements.

## Quick Start
```markdown
# PRD: [Feature Name]

## Problem Statement
[Description of the problem]

## Goals
- Goal 1
- Goal 2

## Features
### F1: [Feature Name]
- Description: ...
- Priority: P0
- Metrics: ...
```

## When to Use
- ✅ Documenting new features
- ✅ Aligning requirements with team
- ❌ Not for technical design (better use TDD)

## Step-by-Step Instructions
1. Describe problem and context
2. Formulate goals and success criteria
3. Detail features with priorities
4. Add metrics and readiness criteria

## Dependencies
```bash
# Template in Markdown
```

## Examples
Input: "Create PRD for shopping cart" → Output: Complete PRD document

## Resources
- [PRD Guide](https://www.productplan.com/glossary/product-requirements-document/)
- [Examples](./examples/)

## Validation
1. Document contains all required sections
2. Goals are measurable and achievable
3. Features are prioritized
