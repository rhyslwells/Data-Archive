---
tags:
  - database
  - data_storage
---


[link](https://www.youtube.com/watch?v=-bSkREem8dM)

### [[Database]]:
- **Definition**: A database, typically relational, captures and stores data through online transactional processing (==OLTP==).
- **Structure**: Data is organized into tables with columns and rows, offering detailed, real-time information.
- **Flexibility**: Databases boast a flexible schema, allowing for dynamic adjustments to accommodate evolving needs.
- **Use Case**: Primarily utilized for recording transactions and managing live data. slow for large queries.
### [[Data warehouse]]:
- **Definition**: A specialized database optimized for analytical processing or online analytical processing (==OLAP==).
- **Data Aggregation**: Aggregates data from multiple sources (databases) via an [[ETL]] (Extract, Transform, Load) process, summarizing it for analytical purposes.
- **Historical Data**: Maintains historical data but may not always include the latest updates unless refreshed by the ETL process.
- **Schema ==Rigidity==**: Features a rigid schema, necessitating careful planning for data integration.
- **Use Case**: Ideal for analytics and reporting, offering fast query performance for large datasets, summarised data. Fast for queries.

### [[Data Lake]]
- **Definition**: A repository that ==stores diverse data types==, including structured, semi-structured, and unstructured data. If cant fit into a database.
- **Versatility**: Can accommodate various data formats, including videos, images, documents, and more.
- **Raw Data Storage**: Preserves data in its raw form, suitable for advanced analytics, particularly in machine learning and AI.
- **Data Usability**: Raw data ==may require cleaning and transformation for analytical use==, often transferred to databases or data warehouses.
- **Use Case**: Valuable for storing large volumes of raw data, especially in contexts requiring advanced analytics and experimentation.

### Conclusion:
- Each option serves distinct purposes, with no one-size-fits-all solution.
- Databases are suited for transaction recording, while data warehouses excel in analytics and reporting.
- Data lakes offer versatility for storing raw data, particularly beneficial for advanced analytics applications.
- Companies may leverage all three options simultaneously to meet diverse data management needs.