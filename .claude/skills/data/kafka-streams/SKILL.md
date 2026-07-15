---
name: kafka-streams
description: "Processes real-time data streams with Apache Kafka Streams. Use for real-time event processing."
category: data
tags: [kafka, streams, real-time, events, java, scala]
models: [opus]
version: 1.0.0
created: 2026-05-01
---
# Kafka Streams#

> Real-time stream processing with Kafka Streams.

## 🚀 Quick Start
```java
StreamsBuilder builder = new StreamsBuilder();
KStream<String, String> source = builder.stream("input-topic");
source.mapValues(value -> value.toUpperCase())
      .to("output-topic");

KafkaStreams streams = new KafkaStreams(builder.build(), config);
streams.start();
```

## 📋 When to Use
- ✅ Real-time event processing
- ✅ Stream analytics
- ❌ Not for batch processing#

## 🔧 Step-by-Step Instructions
1. Add Kafka Streams dependency
2. Create StreamsBuilder with topics
3. Define transformations
4. Start KafkaStreams application

## 📦 Dependencies
```xml
<dependency>
    <groupId>org.apache.kafka</groupId>
    <artifactId>kafka-streams</artifactId>
    <version>3.6.0</version>
</dependency>
```

## 🧪 Examples
Input: Message in "input-topic" → Output: UPPERCASE in "output-topic"

## 🔗 Resources
- [Kafka Streams Docs](https://kafka.apache.org/documentation/streams/)
- [Examples](./examples/)

## ✅ Validation
1. Application connects to Kafka
2. Messages processed in real-time
3. Processing errors caught
