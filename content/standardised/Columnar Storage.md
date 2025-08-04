---
aliases: 
category: 
date modified: 27-07-2025
tags:
  - storage
---
A database storage technique that stores ==data by columns== rather than rows, 

Useful for read-heavy operations and ==large-scale data analytics==, as it enables the retrieval of specific columns without the need to access the entire row. 

Columnar Storage Example (Analytical Workloads)**:

| `order_id`  | `customer_id` | `order_date` | `order_amount` |
|-------------|---------------|--------------|----------------|
| 1           | 101           | 2024-10-01   | $100           |
| 2           | 102           | 2024-10-02   | $150           |
| 3           | 103           | 2024-10-03   | $200           |
In **columnar storage**, the data would be stored by columns, like:
- `customer_id`: [101, 102, 103]

If you're querying for the total sales (`order_amount`) in a specific period, only the `order_amount` and `order_date` columns are accessed. 


Use case: **Data Analytics/OLAP (Online Analytical Processing)**
- Running a query to get the **total sales for October** only needs to scan the `order_amount` and `order_date` columns, rather than scanning entire rows, faster [[Querying]]