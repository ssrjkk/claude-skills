---
name: mqtt
description: Sets up MQTT brokers and clients for messaging in IoT systems. Use for lightweight messaging in IoT.
category: iot
tags: [mqtt, iot, messaging, broker, mosquitto]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# MQTT

> Lightweight messaging protocol for IoT systems.

## Quick Start
```bash
# Install Mosquitto broker
sudo apt-get install mosquitto mosquitto-clients

# Subscribe to topic
mosquitto_sub -h localhost -t "sensors/temperature"

# Publish message
mosquitto_pub -h localhost -t "sensors/temperature" -m "23.5"
```

## When to Use
- ✅ IoT devices with limited resources
- ✅ Pub/Sub pattern for data exchange
- ❌ Not for large files or complex RPC

## Step-by-Step Instructions
1. Install MQTT broker (Mosquitto)
2. Configure broker settings
3. Connect clients to broker
4. Publish and subscribe to topics

## Dependencies
```bash
sudo apt-get install mosquitto mosquitto-clients
# or for Python: pip install paho-mqtt
```

## Examples
Input: `mosquitto_pub -t "test" -m "hello"` → Output: Subscriber receives "hello"

## Resources
- [MQTT Docs](https://mqtt.org/documentation/)
- [Examples](./examples/)

## Validation
1. Broker starts and listens on port 1883
2. Messages delivered between clients
3. QoS levels work correctly
