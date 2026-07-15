---
name: ant-design
description: "Builds enterprise UIs with Ant Design, including pre-built components, theming, and i18n support."
category: design
tags: [ant-design, react, ui-library, enterprise, components]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Ant Design
> Enterprise UI design system with React components.
## Quick Start
```tsx
import { Button, DatePicker, Table, Space } from 'antd'
export default function App() {
  return <Space><Button type="primary">Search</Button><DatePicker /></Space>
}
```
## Theming
```tsx
import { ConfigProvider } from 'antd'
<ConfigProvider theme={{ token: { colorPrimary: '#00b96b', borderRadius: 6 } }}>
  <App />
</ConfigProvider>
```
## When to Use
- Enterprise dashboards; Admin panels; Data-heavy interfaces
## Validation
1. Components render without errors; 2. Theme tokens apply; 3. Pagination and sorting work
