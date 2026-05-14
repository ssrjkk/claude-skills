---
name: websocket
description: Implements real-time bidirectional communication using WebSockets with Socket.IO, ws, or native WebSocket API. Use for chat, live updates, and collaborative apps.
category: backend
tags: [websocket, realtime, socketio, nodejs, python]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# WebSocket

> Real-time bidirectional communication for modern apps.

## Quick Start (Node.js + ws)
```javascript
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', (ws) => {
  ws.on('message', (msg) => {
    console.log('received:', msg.toString());
    ws.send(`Echo: ${msg}`);
  });
});
```

## When to Use
- Chat applications
- Live notifications
- Collaborative editing
- Real-time dashboards

## Step-by-Step
1. Install WebSocket library
2. Create server with connection handler
3. Handle messages and broadcast
4. Connect from client with `new WebSocket(url)`

## Dependencies
```bash
npm install ws socket.io
# or
pip install websockets
```

## Examples
Client: `new WebSocket("ws://localhost:8080")`
Server broadcasts to all connected clients.

## Resources
- [MDN WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)

## Validation
1. Server starts on ws://localhost:8080
2. Client connects successfully
3. Messages echo back correctly
