---
aliases: 
category: DE
date modified: 27-07-2025
tags:
  - transformation
title:
---
**ELT** (Extract, Load, Transform) is a data integration approach that involves three main steps:

1. **Extract (E)**: Data is extracted from a source system.
2. **Load (L)**: The raw data is loaded into a destination system, such as a data warehouse.
3. **Transform (T)**: Transformation of the data occurs within the destination system after the data has been loaded.

This approach contrasts with the traditional **ETL** (Extract, Transform, Load) method, where data is transformed before reaching the destination. For a detailed comparison, see [[ETL vs ELT]]

### Advantages of ELT
The shift from ETL to ELT has been facilitated by several factors:

- **Cost Efficiency**: The decreasing costs of cloud-based storage and computation have reduced the advantages of ETL's pre-loading data transformation.
  
- **Cloud-Based Data Warehouses**: The emergence of cloud-based data warehouses like Redshift, [[BigQuery]], and [[Snowflake]] has made the ELT approach more feasible and efficient.
### Historical Context
Historically, ETL was preferred for reasons that are now less relevant:

- **Cost Savings**: ETL was believed to save costs by filtering out unwanted data before loading. However, this is less significant with modern cloud solutions.
  
- **Complexity Management**: ETL minimizes the complexity of post-loading transformations. Yet, contemporary tools like [[dbt]] simplify this process, making it easier to perform transformations after loading.
