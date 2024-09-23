---
tags:
  - database
  - engineering
title: What is a Data Warehouse?
---


[Designing a datawarehouse](https://www.youtube.com/watch?v=patBYUGwsHE)

[Why a data warehouse](https://www.youtube.com/watch?v=jmwGNhUXn_o)

==A data warehouse is for querying.==
A database is for recording the data quickly.


A data warehouse is a centralized repository that stores large volumes of ==structured data== from various sources within an organization. It is designed to facilitate reporting, analysis, and decision-making by providing a consolidated view of the data.

### Key Features of a [[uncleaned/Data Warehouse]]

1. **Integration**: Data from different sources (e.g., transactional databases, CRM systems, external data) is integrated into a single repository, ensuring consistency and reliability.

2. **Subject-Oriented**: Data is organized around key subjects or business areas, such as sales, finance, or customer data, rather than the operations or transactions of an organization.

3. **Non-Volatile**: Once data is entered into the data warehouse, it is not changed. This ensures that historical data is preserved for analysis over time.

4. **Time-Variant**: Data in a data warehouse is stored with a time dimension, which allows for historical analysis and trend identification. This is different from operational databases that are more focused on current, real-time data.

### Components of a Data Warehouse

1. **Data Sources**: The origin points of data, which can be internal (e.g., ERP systems, transactional databases) or external (e.g., market research data, web logs).

2. **[[ETL]] Process (Extract, Transform, Load)**:
   - **Extract**: Data is collected from various source systems.
   - **Transform**: Data is cleaned, formatted, and transformed to ensure consistency and compatibility.
   - **Load**: Transformed data is loaded into the data warehouse.

3. **Data Storage**: The actual storage where data is kept, often organized in a way that supports efficient querying and analysis. This can be structured in various schemas such as star schema or snowflake schema.

4. **Metadata**: Data about the data, which includes definitions, source information, and rules for data transformation. Metadata helps users understand and manage the data warehouse.

5. **Access Tools**: Tools that allow users to query, report, and analyze the data. These can include SQL clients, business intelligence tools, data visualization tools, and dashboards.

### Benefits of a Data Warehouse

- **Improved Decision-Making**: By providing a ==consolidated view of the organization’s data,== decision-makers have access to more accurate and comprehensive information.
- **Historical Intelligence**: The ability to analyze historical data helps identify trends, forecast future outcomes, and conduct time-series analysis.
- **Data Quality and Consistency**: The [[ETL]] process ensures that data is cleaned and standardized, improving overall data quality.
- **Performance**: Data warehouses are ==optimized for query performance==, allowing for faster retrieval and analysis compared to transactional systems.

### Example

Consider a retail company that wants to analyze sales performance across different regions and time periods. The company's transactional databases hold daily sales transactions, customer information, and inventory data. A data warehouse would:

1. **Extract**: ==Collect data== from these various transactional databases.
2. **Transform**: Clean and integrate this data, ensuring that sales data from all regions use the same formats and categorizations.
3. **Load**: Store the integrated data in a centralized data warehouse.
4. **Query**: Enable analysts to run complex queries, generate reports, and create visualizations to identify sales trends, regional performance, and customer buying behaviors over time.

In summary, a data warehouse is a powerful tool that supports strategic decision-making by providing a comprehensive and unified view of an organization’s data.

A Data Warehouse, in short DWH, also known as an Enterprise Data Warehouse (EDW), is the traditional way of collecting data as we do [since 30+ years](https://tdwi.org/articles/2016/02/01/data-warehousing-30.aspx). The DWH serves to be the [data integration](term/data%20integration.md) from many different sources, the single point of truth and the data management, meaning cleaning, historizing, and data joined together. It provides greater executive insight into corporate performance with management Dashboards, Reports, or Ad-Hoc Analyses.

Various types of business data are analyzed with Data Warehouses. The need for it often becomes evident when analytic requirements run afoul of the ongoing performance of operational databases. Running a complex query on a database requires the database to enter a temporarily fixed state. It is often untenable for transactional databases. A data warehouse is employed to do the analytical work, leaving the transactional database free to focus on transactions.

The other characteristic is analyzing data from multiple origins (e.g., your Google Analytics with your CRM data). It is highly [transformed](term/data%20transformation.md) and structured due to the [ETL (Extract Transform Load)](term/etl.md) process.

If you wonder about the difference between a Data Warehouse, Data Lake, and a Lakehouse, read more on our [Data Lake and Lakehouse Guide](https://airbyte.com/blog/data-lake-lakehouse-guide-powered-by-table-formats-delta-lake-iceberg-hudi).