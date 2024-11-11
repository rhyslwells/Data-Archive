---
title: 
tags:
  - software
  - data_orchestration
aliases:
  - Kafka
category:
---
Apache Kafka is an open-source distributed event streaming platform used for building real-time data pipelines and streaming  applications. It is designed to handle high-throughput, fault-tolerant, and scalable messaging. 

1. [[Publish and Subscribe]]: Kafka allows applications to publish and subscribe to streams of records, similar to a message queue or enterprise messaging system.

2. Durability and Reliability: Kafka stores streams of records in a fault-tolerant way, ensuring data durability and reliability. It replicates data across multiple nodes to prevent data loss.

3. Scalability: Kafka is designed to scale horizontally by adding more brokers (servers) to the cluster, which can handle increased load and data volume.

4. High Throughput: Kafka is optimized for high throughput, making it suitable for processing large volumes of data in real-time.

5. Topics and Partitions: Data in Kafka is organized into topics, which are further divided into partitions. Each partition is an ordered, immutable sequence of records that is continually appended to.

6. Producers and Consumers: Producers are applications that publish data to Kafka topics, while consumers are applications that subscribe to topics and process the data.

7. Use Cases: Kafka is commonly used for log aggregation, real-time analytics, data integration, stream processing, and building event-driven architectures.

8. Integration: Kafka integrates well with various data processing frameworks like Apache Spark, Apache Flink, and Apache Storm, as well as with databases and other data storage systems.
