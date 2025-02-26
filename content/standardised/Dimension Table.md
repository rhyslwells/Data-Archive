A dimension table is a key component of a [[star schema]] or snowflake schema in a data warehouse. It provides descriptive attributes (or dimensions) related to the [[Facts]] stored in a fact table.

They provide the context and descriptive information necessary for analyzing the quantitative data stored in fact tables (e.g., product names, customer demographics, time periods).

1. **Descriptive Attributes**: Dimension tables contain qualitative data that describe the entities involved in the business process. For example, a product dimension table might include attributes such as product name, category, brand, and manufacturer.

2. **Primary Key**: Each dimension table has a primary key that uniquely identifies each record in the table. This primary key is used as a foreign key in the [[Fact Table]] to establish relationships between the two.

3. **Hierarchies**: Dimension tables often include hierarchies that allow for data to be analyzed at different levels of granularity. For example, a time dimension might include attributes for year, quarter, month, and day, allowing users to drill down or roll up in their analysis.

4. **Smaller Size**: Compared to fact tables, dimension tables are typically smaller in size, as they contain descriptive data rather than large volumes of transactional data.

5. **Static Data**: Dimension tables usually contain relatively static data that does not change frequently, such as product details or customer information. However, they can be updated as needed to reflect changes in the business.

6. **Support for Filtering and Grouping**: Dimension tables enable users to filter and group data in reports and analyses. For example, users can analyze sales data by different dimensions such as time, geography, or product category.

Examples
  - **TimeDimension**: Contains information about the time period.
    - Columns: `DateKey`, `Year`, `Quarter`, `Month`, `Day`
  - **ProductDimension**: Contains product details.
    - Columns: `ProductKey`, `ProductName`, `ProductCategory`
  - **RegionDimension**: Contains regional information.
    - Columns: `RegionKey`, `RegionName`, `Country`





[[Dimension Table]]
   **Tags**: #data_modeling, #data_warehouse