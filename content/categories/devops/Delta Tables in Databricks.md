---
aliases:
  - Delta Table
category:
date modified: 19-10-2025
tags:
  - data_engineering
  - data_management
  - databricks
---
A Delta Table is a storage format used in [[Databricks]] and [[Apache Spark]] that brings reliability, consistency, and performance to big data storage. It extends the traditional [[Parquet]] format with ACID transactions, schema enforcement, and time travel capabilities.

A Delta Table stores data in the Delta Lake format, which sits on top of a data lake (e.g., [[Azure Data Lake]], [[AWS S3]], or GCP Storage). It allows users to read, write, and modify large-scale datasets safely — similar to how a relational [[database]] table works.
### Key Features

[[ACID Transaction]]
   * Ensures *atomicity, consistency, isolation, and durability* for all operations.
   * Prevents data corruption during concurrent writes or failures.

[[Schema Evolution]] and Enforcement
   * Rejects writes that don’t match the table schema.
   * Optionally allows automatic schema evolution when new columns are added.

Time Travel
   * Enables querying historical versions of data using a timestamp or version number.
   * Useful for debugging, audits, or reproducing past results.

Upserts and Deletes (MERGE INTO)
   * Supports `UPDATE`, `DELETE`, and `MERGE` operations natively.
   * Simplifies data correction and change data capture (CDC) workflows.

Optimized Reads and Writes
   * Uses file-level metadata tracking and data skipping for efficient queries.

### Delta Table Structure

A Delta Table is stored as a directory containing:
* Data files (in Parquet format).
* A _delta_log/ directory that maintains the transaction history as JSON files.
### Example Usage

```python
# Create Delta table from a DataFrame
df.write.format("delta").mode("overwrite").saveAsTable("example.sales_transactions")

# Read Delta table
df = spark.read.format("delta").table("example.sales_transactions")

# Query historical data (time travel)
df_old = spark.read.format("delta").option("versionAsOf", 3).table("example.sales_transactions")
```

### Advantages Over [[Parquet]]

| Feature           | Parquet     | Delta Table   |
| ----------------- | ----------- | ------------- |
| ACID Transactions | ❌           | ✅             |
| Schema Evolution  | ⚠️ (manual) | ✅ (automatic) |
| Time Travel       | ❌           | ✅             |
| Updates/Deletes   | ❌           | ✅             |
| Data Skipping     | ⚠️          | ✅             |

### Related:
- [[Catalogs, Schemas, and Tables in Databricks]]