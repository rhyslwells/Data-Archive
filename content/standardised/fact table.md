A fact table is a central component of a star [[Database Schema|schema]] or snowflake schema in a [[data warehouse]], it stores [[Facts]].

Essential for [[data analysis]] in a data warehouse, providing the numerical data that can be analyzed in conjunction with the descriptive data stored in dimension tables.

1. **Measures**: Fact tables contain measurable, quantitative data known as "facts" or "measures." Examples include sales revenue, quantity sold, profit, or any other numeric data that can be aggregated.

2. **Foreign Keys**: Fact tables include foreign keys that reference [[Dimension Table]]s. These keys link the fact table to related dimensions, allowing for contextual analysis. For example, a sales fact table might include foreign keys for dimensions such as time, product, and customer.

3. **Granularity**: The [[granularity]] of a fact table refers to the level of detail stored in the table. For example, a sales fact table might store data at the transaction level (each sale) or at a higher level (daily sales totals).

4. **Large Size**: Fact tables can become quite large, as they often store a significant amount of transactional data over time. This is in contrast to dimension tables, which are usually smaller and contain descriptive attributes.

5. **Aggregation**: Fact tables are often used for aggregation and analysis, allowing users to perform operations such as summing, averaging, or counting the measures.

Example:
  - Columns: `DateKey`, `ProductKey`, `RegionKey`, `SalesAmount`, `UnitsSold`