---
title: 
tags:
  - data_orchestration
aliases: 
category:
---
>[!Summary]
> **Data Streaming** is used for **real-time data processing**, allowing continuous flow and processing of data as it arrives. This is different from batch processing, which handles data in chunks.

- The key to data streaming is the ==**Publish-Subscribe== (Pub/Sub) model**:
  - **Producers** publish messages to specific channels called **Topics**.
  - **Consumers** subscribe to these Topics to receive the data in real-time.
  
- [[Apache Kafka]] is a widely-used framework for data streaming. It has several key features:
  - **High throughput**: Kafka can process millions of messages per second.
  - **Scalability**: It can scale to thousands of brokers (servers) to handle large data streams.
  - **Immutable commit log**: Kafka maintains an append-only log of messages, which ensures data integrity and replayability.

- **Real-world example**:
  - Companies like **Netflix** use Kafka to handle billions of messages daily, powering real-time recommendations, analytics, and user activity tracking.
