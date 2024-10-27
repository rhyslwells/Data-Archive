---
title: What are Data Processing Techniques (row-based, columnar, vectorized)?
tags:
  - database
  - data_processing
---

A collection of concepts and technologies that encompass various methods and optimizations for storing, retrieving, and processing data in database systems. 

This glossary page includes definitions for **columnar storage, row-based storage, and vectorized engines**, which are all techniques that aim to improve the efficiency and performance of different types of workloads, such as 
- transactional, 
- analytical, 
- and large-scale data processing tasks. 

Summary of Use Cases:
- **Columnar Storage**: Best for analytical queries that focus on aggregates or specific fields from large datasets, e.g., calculating total sales, customer behavior analysis, etc.
- **Row-based Storage**: Best for transactional operations where entire records are inserted, updated, or deleted frequently, e.g., processing orders or user updates in a web application.

## Columnar Storage

A database storage technique that stores ==data by columns== rather than rows, allowing for more efficient compression and faster querying for analytical workloads. Columnar storage is particularly useful for read-heavy operations and ==large-scale data analytics==, as it enables the retrieval of specific columns without the need to access the entire row. This contrasts with traditional row-based storage, where data is stored row by row, making it more suited for transactional workloads and operations that involve frequent updates and inserts.

Columnar Storage Example (Analytical Workloads)**:
Imagine a data warehouse table for an e-commerce company that tracks customer orders, with columns like `order_id`, `customer_id`, `order_date`, and `order_amount`.

**Table (columnar storage)**:

| `order_id`  | `customer_id` | `order_date` | `order_amount` |
|-------------|---------------|--------------|----------------|
| 1           | 101           | 2024-10-01   | $100           |
| 2           | 102           | 2024-10-02   | $150           |
| 3           | 103           | 2024-10-03   | $200           |
In **columnar storage**, the data would be stored by columns, like:
- `order_id`: [1, 2, 3]
- `customer_id`: [101, 102, 103]
- `order_date`: [2024-10-01, 2024-10-02, 2024-10-03]
- `order_amount`: [$100, $150, $200]

If you're querying for the total sales (`order_amount`) in a specific period, only the `order_amount` and `order_date` columns are accessed. This minimizes the amount of data read from disk, improving query performance for analytical workloads.

Use case: **Data Analytics/OLAP (Online Analytical Processing)**
- Running a query to get the **total sales for October** only needs to scan the `order_amount` and `order_date` columns, rather than scanning entire rows, leading to faster query execution and less data movement.
## Row-based Storage

A traditional database storage technique where data is stored in consecutive rows, allows for efficient processing of operations that involve entire records, such as inserts, updates, and deletions. Row-based storage is well-suited for transactional systems ([[OLTP]]) that require fast access to individual records. However, it can be less efficient for analytical workloads and large-scale data processing, where columnar storage offers better performance due to its ability to selectively retrieve specific columns without accessing the entire row.

Here’s an example of both **columnar storage** and **row-based storage**, highlighting their respective strengths:

Row-based Storage Example (Transactional Workloads)**:
For the same table, if the goal is to efficiently handle transactions like inserting or updating an order, **row-based storage** organizes data row by row.

| `order_id` | `customer_id` | `order_date` | `order_amount` |
| ---------- | ------------- | ------------ | -------------- |
| 1          | 101           | 2024-10-01   | $100           |
| 2          | 102           | 2024-10-02   | $150           |
| 3          | 103           | 2024-10-03   | $200           |

In **row-based storage**, entire records (rows) are stored together. For example:
- Row 1: [1, 101, 2024-10-01, $100]
- Row 2: [2, 102, 2024-10-02, $150]
- Row 3: [3, 103, 2024-10-03, $200]

When performing an **insert** or **update**, the entire row can be read and written back quickly, making this method ideal for transactional operations where complete records need to be processed together.

Use case: **Transactional Systems/OLTP (Online Transactional Processing)**
- For instance, inserting a new order or updating an existing one (like modifying `order_amount` or `customer_id`) is efficient because all the data for a single record is stored together in a row.

## Vectorized Engine

A modern database query execution engine designed to optimize data processing by leveraging vectorized operations and SIMD (Single Instruction, Multiple Data) capabilities of modern CPUs. Vectorized engines, such as Databricks' Photon Engine or [DuckDB](term/duckdb.md), process data in large blocks or batches, allowing for improved parallelism, cache locality, and reduced overhead compared to traditional row-at-a-time processing engines.

In summary, **vectorized engines** significantly enhance performance for read-heavy, analytical workloads by processing data in larger batches and taking advantage of SIMD instructions. They are a natural fit for **columnar storage** systems and are ideal for environments that require high-speed, large-scale data processing.