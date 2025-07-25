---
tags:
  - data_storage
  - data_modeling
category:
---
Apache Iceberg is an open table format for huge analytic datasets. It manages large-scale data stored in files (like [[Parquet]] or ORC) on distributed storage systems (like HDFS, S3, or GCS).

In short, Iceberg turns your [[data lake]] into a [[data warehouse]]-like system with strong guarantees and high performance.
### Key Features:

* [[Schema evolution]] and partition evolution without rewriting data.
* Hidden partitioning: simplifies queries by abstracting partition logic.
* ACID transactions for consistency during concurrent reads/writes.
* Time travel and rollback via metadata snapshots.
* Optimized for engines like [[Apache Spark|Spark]], Trino, Flink, Dremio, and [[Snowflake]].


