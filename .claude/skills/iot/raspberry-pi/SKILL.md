---
name: raspberry-pi
description: "Configures and deploys applications on Raspberry Pi, including GPIO, camera, and headless setup."
category: iot
tags: [raspberry-pi, gpio, python, embedded, linux]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Raspberry Pi
> Single-board computer for embedded projects and IoT.
## Quick Start
```bash
# Enable SSH & WiFi on fresh SD card
touch /boot/ssh
cat > /boot/wpa_supplicant.conf << EOF
network={ ssid="MyWiFi" psk="mypassword" }
EOF
```
## GPIO Python
```python
import RPi.GPIO as GPIO; import time
GPIO.setmode(GPIO.BCM); GPIO.setup(18, GPIO.OUT); GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    if GPIO.input(23) == GPIO.LOW: GPIO.output(18, GPIO.HIGH); time.sleep(1); GPIO.output(18, GPIO.LOW)
```
## When to Use
- IoT sensor projects; Home automation; Media centers; Robotics
## Validation
1. Pi boots and SSH accessible; 2. GPIO Python scripts work; 3. Camera captures images
