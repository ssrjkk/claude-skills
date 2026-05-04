---
name: esp32
description: Programs ESP32 microcontrollers in C/C++ or MicroPython. Use for IoT projects with WiFi/Bluetooth.
category: iot
tags: [esp32, iot, microcontroller, wifi, bluetooth, micropython]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-01
---
# ESP32

> Program ESP32 for IoT projects with WiFi and Bluetooth.

## Quick Start
```cpp
#include <WiFi.h>

const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);
}

void loop() {
    Serial.println(WiFi.localIP());
    delay(1000);
}
```

## When to Use
- ✅ IoT projects with network connectivity
- ✅ Need WiFi/Bluetooth in device
- ❌ Not for simple projects without connectivity (better use Arduino)

## Step-by-Step Instructions
1. Install ESP32 board in Arduino IDE
2. Select board: Tools → Board → ESP32 Arduino
3. Write code and upload via USB
4. Monitor Serial port

## Dependencies
Arduino IDE with ESP32 board manager

## Examples
Input: Connect to WiFi → Output: IP address in Serial monitor

## Resources
- [ESP32 Docs](https://docs.espressif.com/)
- [Examples](./examples/)

## Validation
1. Code uploads without errors
2. Device connects to WiFi
3. Serial monitor shows data
