---
name: accessibility
description: "Checks and improves web application accessibility per WCAG standards. Use for creating inclusive design."
category: design
tags: [accessibility, wcag, a11y, inclusive-design]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# Accessibility (A11y)

> Ensure web application accessibility per WCAG standards.

## Quick Start
```html
<!-- Correct -->
<button aria-label="Close" onclick="closeModal()">
  <span aria-hidden="true">×</span>
</button>

<!-- For screen readers -->
<img src="chart.png" alt="Sales chart for 2024">
```

## When to Use
- ✅ Web applications with broad audience
- ✅ Compliance with legislation (ADA, Section 508)
- ❌ Not for internal admin panels without users with disabilities

## Step-by-Step Instructions
1. Conduct audit with axe DevTools
2. Add ARIA attributes where needed
3. Ensure keyboard navigation
4. Check color contrast

## Dependencies
```bash
npm install @axe-core/cli pa11y
```

## Examples
Input: Form check → Output: 3 contrast errors fixed

## Resources
- [WCAG Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [Examples](./examples/)

## Validation
1. Scanners find no critical violations
2. Keyboard navigation works
3. Screen readers read content correctly
