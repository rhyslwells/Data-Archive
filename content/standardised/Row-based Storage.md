---
aliases: []
category:
date modified: 27-07-2025
tags: []
---
Data is stored in consecutive rows, allows [[CRUD]]

Row-based storage is well-suited for transactional systems ([[OLTP]]) 

Less efficient than [[Columnar Storage]] in largedatasets.

Row-based Storage Example (Transactional Workloads)**:
For the same table, if the goal is to efficiently handle transactions like inserting or updating an order, **row-based storage** organizes data row by row.

| `order_id` | `customer_id` | `order_date` | `order_amount` |
| ---------- | ------------- | ------------ | -------------- |
| 1          | 101           | 2024-10-01   | $100           |
| 2          | 102           | 2024-10-02   | $150           |
| 3          | 103           | 2024-10-03   | $200           |

In **row-based storage**, entire records (rows) are stored together. For example:
- Row 1: [1, 101, 2024-10-01, $100]

When performing an **insert** or **update**, the entire row can be read and written back quickly, making this method ideal for transactional operations where complete records need to be processed together.

Use case [[OLTP]]. For instance, inserting a new order or updating an existing one (like modifying `order_amount` or `customer_id`) is efficient because all the data for a single record is stored together in a row.