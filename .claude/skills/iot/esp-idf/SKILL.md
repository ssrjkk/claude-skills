---
name: esp-idf
description: Programs ESP32 microcontrollers using ESP-IDF framework with FreeRTOS, Wi-Fi, and Bluetooth.
category: iot
tags: [esp-idf, esp32, freertos, embedded, c]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# ESP-IDF
> Official development framework for ESP32 microcontrollers.
## Quick Start
```bash
git clone --recursive https://github.com/espressif/esp-idf.git
cd esp-idf && ./install.sh && . ./export.sh
idf.py create-project my_project; idf.py set-target esp32; idf.py build flash monitor
```
## Wi-Fi & GPIO
```c
#include "esp_wifi.h"; #include "driver/gpio.h"
void wifi_init_sta(void) { esp_netif_init(); esp_event_loop_create_default(); esp_netif_create_default_wifi_sta(); wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT(); esp_wifi_init(&cfg); }
gpio_set_direction(GPIO_NUM_2, GPIO_MODE_OUTPUT); gpio_set_level(GPIO_NUM_2, 1);
```
## When to Use
- Advanced ESP32 projects; Wi-Fi/Bluetooth apps; IoT gateways
## Validation
1. Firmware builds; 2. Device connects to Wi-Fi; 3. GPIO outputs change state
