There are several types of database schemas commonly used in data warehousing and database design.

[[Star Schema]]

[[Snowflake Schema]]

Galaxy Schema (or Fact Constellation Schema):
   - This schema consists of multiple fact tables that share dimension tables. It is useful for complex data models that require analysis across different business processes. The galaxy schema allows for more flexibility in querying and reporting.

[[Normalised Schema]]

Denormalized Schema:
   - A denormalized schema combines data from multiple tables into fewer tables to improve query performance. This approach is often used in data marts and data warehouses where read performance is prioritized over write performance.

Entity-Relationship Model ([[ER Diagrams]])
   - This is a conceptual schema that represents the data and its relationships in a graphical format. It is often used during the design phase of a database to visualize how entities (tables) relate to one another.

Columnar Schema:
   - In a [[Columnar Storage]] database, data is stored in columns rather than rows. This schema is optimized for read-heavy operations and analytical queries, making it suitable for data warehousing applications. Examples include Apache Cassandra and Google BigQuery.

