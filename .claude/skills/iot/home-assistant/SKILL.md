---
name: home-assistant
description: "Automates smart home devices with Home Assistant, integrations, automations, and custom dashboards."
category: iot
tags: [home-assistant, smart-home, automation, iot, dashboard]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Home Assistant
> Open-source home automation platform.
## Quick Start
```bash
docker run -d --name home-assistant -p 8123:8123 -v ./config:/config ghcr.io/home-assistant/home-assistant:stable
```
## Automations
```yaml
automation:
  - alias: "Turn on lights at sunset"
    trigger: [{ platform: sun, event: sunset }]
    action: [{ service: light.turn_on, target: { entity_id: "light.living_room" }, data: { brightness: 200 } }]
```
## When to Use
- Smart home integration; Automated routines; Energy monitoring
## Validation
1. UI loads on port 8123; 2. Devices discovered; 3. Automations trigger correctly
