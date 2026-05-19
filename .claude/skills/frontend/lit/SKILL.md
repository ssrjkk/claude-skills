---
name: lit
description: Builds fast, standard-compliant web components with Lit, reactive properties, and Shadow DOM. Use for framework-agnostic UI.
category: frontend
tags: [lit, web-components, shadow-dom, reactive, standards]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Lit

> Simple library for building fast, lightweight web components.

## Quick Start
```javascript
import { LitElement, html, css } from 'lit'
class MyElement extends LitElement {
  static properties = { name: { type: String } }
  static styles = css`h1 { color: blue; }`
  render() { return html`<h1>Hello, ${this.name}!</h1>` }
}
customElements.define('my-element', MyElement)
```

## Reactive Properties & Lifecycle
```javascript
static properties = { count: { type: Number } }
constructor() { super(); this.count = 0 }
connectedCallback() { super.connectedCallback(); console.log('mounted') }
updated(changedProperties) { if (changedProperties.has('count')) console.log('count changed') }
```

## When to Use
- Framework-agnostic components
- Design system elements
- Micro-frontend architectures
- Shadow DOM encapsulation

## Validation
1. Custom elements register and render
2. Properties update reactively
3. Shadow DOM isolates styles
