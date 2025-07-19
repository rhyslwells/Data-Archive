---
title: What is a Data Lakehouse?
tags:
  - data_storage
aliases:
  - Lakehouse
---
A Data Lakehouse open [[Data Management]] architecture that combines the flexibility, cost-efficiency, and scale of [[Data Lake]] with the data management and [[ACID Transaction]]s of [[Data Warehouse]]  with Data Lake Table Formats ([[Delta Lake]], [[Apache Iceberg]]) that enable Business Intelligence (BI) and Machine Learning (ML) on all data.

A data lakehouse is an emerging architectural approach that combines the best features of data lakes and data warehouses to provide a unified platform for storing, processing, and analyzing large volumes of structured and unstructured data.
### Key Characteristics

1. Unified Storage:
   - Data lakehouses store data in a single repository, accommodating both structured data (like tables in a database) and unstructured data (like images, videos, and text). This eliminates the need for separate systems, simplifying data management.

1. Support for Multiple Data Types:
   - They can handle various data formats, such as CSV, JSON, [[Parquet]], and Avro, enabling flexibility in how data is ingested and stored.

3. [[ACID Transaction]]:
   - Unlike traditional data lakes, data lakehouses provide [[ACID Transaction]] which ensure reliable data operations and integrity, even in concurrent processing environments.

1. Schema Enforcement:
   - Data lakehouses can enforce [[Database Schema|schema]] at the time of data write, allowing users to define data structures while still benefiting from the flexibility of a data lake.

1. Performance Optimization:
   - They incorporate various optimization techniques, such as indexing and caching, to improve query performance and provide faster access to data.

1. Integration with BI Tools:
   - Data lakehouses are designed to work seamlessly with business intelligence (BI) tools and data analytics platforms, enabling users to derive insights without needing extensive data preparation.

### Benefits

1. Cost-Effectiveness:
   - By merging the functionalities of data lakes and data warehouses, organizations can reduce the costs associated with maintaining separate systems for structured and unstructured data.

1. Scalability:
   - Data lakehouses leverage cloud storage solutions, allowing for scalable data storage that can grow with the organization’s needs.

1. Data Accessibility:
   - With a unified architecture, data from different sources can be accessed and analyzed together, breaking down silos and fostering a more holistic view of the organization’s data landscape.

1. Simplified Data Pipelines:
   - Data lakehouses streamline the [[data ingestion]] process, enabling organizations to build more efficient data pipelines that accommodate a variety of data sources.

1. Support for Advanced Analytics:
   - They provide a robust foundation for advanced analytics, including machine learning and real-time data processing, allowing organizations to extract actionable insights more effectively.

Platforms that implement the data lakehouse architecture include:
- [[Databricks]] Lakehouse Platform: Combines data engineering, data science, and BI capabilities with a focus on collaboration.
- [[Apache Iceberg]]: A high-performance table format for large analytic datasets that supports ACID transactions and [[schema evolution]].
- [[Apache Iceberg vs Databricks]]

