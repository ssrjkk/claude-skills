---
name: node-red
description: Creates IoT and automation flows with Node-RED, visual programming for event-driven applications.
category: iot
tags: [node-red, flow-based, iot, automation, visual-programming]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Node-RED
> Flow-based visual programming for IoT and automation.
## Quick Start
```bash
npm install -g node-red && node-red
# UI at http://localhost:1880
```
## Function Node (JavaScript)
```javascript
msg.payload = { temperature: (msg.payload.temp * 9/5) + 32, unit: "F", timestamp: Date.now() }
return msg;
```
## Flow Components
- Inject: Trigger events; Function: JS transformation; MQTT: Pub/sub; HTTP: REST endpoints; Dashboard: UI widgets
## When to Use
- Visual IoT pipelines; MQTT message processing; Home automation; API integrations
## Validation
1. Editor loads in browser; 2. Deployed flow executes; 3. Debug panel shows messages
