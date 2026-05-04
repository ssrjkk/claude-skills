---
name: arduino
description: Programs Arduino boards for hardware projects and prototyping. Use for simple IoT and robotics projects.
category: iot
tags: [arduino, iot, microcontroller, c, prototyping]
models: [haiku, sonnet]
version: 1.0.0
created: 2026-05-01
---
# Arduino

> Simple microcontroller programming for hardware projects.

## Quick Start
```cpp
void setup() {
    pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(1000);
    digitalWrite(LED_BUILTIN, LOW);
    delay(1000);
}
```

## When to Use
- ✅ Simple hardware projects
- ✅ Rapid prototyping
- ❌ Not for complex IoT with cloud (better use ESP32)

## Step-by-Step Instructions
1. Install Arduino IDE
2. Connect board via USB
3. Select board and port in Tools
4. Upload sketch

## Dependencies
Download Arduino IDE from https://www.arduino.cc/en/software

## Examples
Input: Upload sketch → Output: LED blinks once per second

## Resources
- [Arduino Docs](https://www.arduino.cc/reference/en/)
- [Examples](./examples/)

## Validation
1. Sketch uploads successfully
2. Hardware works correctly
3. Serial monitor shows data (if used)
