---
name: apache-flink
description: "Builds real-time stream processing applications with Apache Flink, event time, and exactly-once semantics."
category: data
tags: [flink, stream-processing, realtime, events, java]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# Apache Flink

> Stream processing framework for real-time data pipelines.

## Quick Start
```java
StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
DataStream<String> stream = env.socketTextStream("localhost", 9999);
stream.flatMap((line, out) -> { for (String word : line.split(" ")) out.collect(word); })
    .keyBy(word -> word).sum(1).print();
env.execute("WordCount");
```

## Windows
```java
stream.keyBy(event -> event.getUserId())
    .window(TumblingEventTimeWindows.of(Time.hours(1)))
    .aggregate(new AverageAggregate())
```

## When to Use
- Real-time data pipelines
- Event-driven applications
- Streaming ETL
- Fraud detection

## Validation
1. Job submits to Flink cluster
2. Stream processes events correctly
3. Checkpoints restore state on failure
