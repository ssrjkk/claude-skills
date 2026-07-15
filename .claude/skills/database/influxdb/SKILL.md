---
name: influxdb
description: "Collects and queries time-series data with InfluxDB, Flux language, and continuous queries."
category: database
tags: [influxdb, time-series, metrics, monitoring, database]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# InfluxDB

> Purpose-built time-series database for metrics and events.

## Quick Start
```bash
docker run -d -p 8086:8086 influxdb:2.0
# UI at http://localhost:8086
```

## Line Protocol
```
weather,location=us-east,sensor=temp-a temperature=72.5,humidity=0.45 1705312800000000000
```

## Flux Query
```flux
from(bucket: "sensor-data")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "weather" and r._field == "temperature")
  |> aggregateWindow(every: 5m, fn: mean)
```

## When to Use
- Infrastructure monitoring metrics
- IoT sensor data
- Application performance tracking
- Real-time analytics

## Validation
1. InfluxDB responds on port 8086
2. Data writes via line protocol succeed
3. Flux queries return time-bucketed results
