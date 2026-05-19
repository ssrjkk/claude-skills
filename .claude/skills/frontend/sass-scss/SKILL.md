---
name: sass-scss
description: Writes maintainable CSS with Sass/SCSS, including variables, mixins, nesting, and partials. Use for scalable stylesheets.
category: frontend
tags: [sass, scss, css, preprocessor, styling]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Sass/SCSS

> Professional CSS preprocessor with variables, mixins, and nesting.

## Quick Start
```scss
$primary: #007bff;
.card { font-family: 'Inter', sans-serif; padding: 1rem;
  &-header { font-size: 1.25rem; }
  &-body { padding: 0.5rem 0; }
}
```

## Mixins & Functions
```scss
@mixin respond-to($bp) {
  @if $bp == md { @media (min-width: 768px) { @content; } }
}
@function rem($px) { @return $px / 16px * 1rem; }
.element { font-size: rem(16px); @include respond-to(md) { width: 50%; } }
```

## When to Use
- Large CSS codebases
- Design system foundations
- Reusable style patterns
- Team-scale CSS projects

## Validation
1. SCSS compiles to valid CSS
2. Mixins output correct styles
3. Variables cascade properly
