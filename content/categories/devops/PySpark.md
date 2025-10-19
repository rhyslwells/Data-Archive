---
aliases: []
category: DEVOPS
created:
date modified: 27-09-2025
tags:
  - "#orchestration"
  - python
type:
---
PySpark is the Python API for [[Apache Spark]], allowing users to write distributed data processing tasks using familiar Python syntax.

Purpose: It enables [[big data]] computation by splitting large datasets across a cluster and processing them in parallel.

Key Components:
* SparkSession: Main entry point for Spark functionality.
* RDDs: Low-level distributed datasets.
* DataFrames: High-level structured data abstraction similar to [[pandas]].
* Catalyst Optimizer: Optimizes DataFrame and [[SQL]] operations for performance.

Example:

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Example").getOrCreate()
df = spark.read.csv("data.csv", header=True, inferSchema=True)
df.show()
```

Use Context: Used within environments such as [[Databricks|Databricks]], which manage Spark clusters and simplify [[distributed computing]] workflows.

### pyspark.sql Module

Definition:
`pyspark.sql` is the core module for structured data in PySpark, supporting both DataFrame operations and SQL queries.

Key Features:
* Provides the DataFrame API for manipulating tabular data.
* Enables SQL [[Querying|queries]] through temporary views.
* Performs lazy evaluation and query optimization via Catalyst.
* Integrates with other Spark components like MLlib and Structured Streaming.

Why Important: Allows analysts and engineers to work with massive structured datasets efficiently using a familiar SQL-like interface.

### PySpark vs pandas

| Feature              | pandas                     | PySpark                                 |
| -------------------- | -------------------------- | --------------------------------------- |
| Data scale       | In-memory (single machine) | Distributed (cluster)                   |
| Execution        | Eager (immediate)          | Lazy (optimized plan)                   |
| Integration      | Python only                | SQL, MLlib, Streaming, Databricks       |
| Failure handling | Limited                    | Fault-tolerant (lineage-based recovery) |

Analogy:

> PySpark is like *pandas + SQL*, but distributed and scalable.

Usage Pattern:
- For local, small datasets → use pandas.
- For large-scale or production data → use PySpark.

### SparkSession

Definition:
A `SparkSession` is the entry point for all Spark functionality in PySpark.

Responsibilities:

* Creates and manages DataFrames.
* Executes SQL queries.
* Connects to the cluster for distributed execution.

Example:

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("MyApp").getOrCreate()
```

Importance: Without a `SparkSession`, you cannot use Spark DataFrames, read data, or run SQL queries.
### PySpark Use Cases

1. ETL and Data Cleaning
2. Data Aggregation and Reporting
3. Joining Large Datasets
4. SQL Query Execution
5. Machine Learning Preparation
### Related

[[Why Use PySpark in Databricks]]