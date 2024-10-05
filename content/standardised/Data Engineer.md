---
title: 
tags:
  - data
  - engineering
  - career
  - data engineering
aliases: Data Engineering
category:
---
## Role of a Data Engineer

Resources:
- [Link](https://www.youtube.com/watch?v=qWru-b6m030)

**Primary Goal:**  
The primary responsibility of a data engineer is to take data from its source and make it available for analysis. They focus on automating the data collection, processing, and analysis workflows while solving how systems manage and handle the flow of data.

### Key Responsibilities:

1. **Infrastructure Design and Maintenance:**  
   Data engineers **design, build, and maintain** the necessary infrastructure to collect, process, and store large amounts of data. This infrastructure is crucial for ensuring data is accessible and usable for analysis and reporting.

2. **Data Pipelines:** 
   They **develop data pipelines** that integrate data from various sources, ensuring **data quality, consistency,** and **timely availability** for downstream use, such as analytics and reporting.

3. **Support Role:**  
   Data engineers **act as a bridge between ==data producers and consumers**==, ensuring smooth and reliable data flow. They support business operations through scalable and efficient [[Data Management]] solutions, contributing indirectly to product delivery and decision-making.

### Core Activities:

- **Build and Optimize Systems:**  
   Design and optimize systems that allow analysts and other consumers to access well-organized, high-quality data.
   
- **Pipeline Development and Testing:**  
   Develop, test, and maintain **data pipelines** to manage data flows efficiently. This includes integrating with external APIs and ensuring data is prepared for further analysis.

What engineers do & interact with:
- [[Batch Processing]]
- [[Data Streaming]]
- [[Big Data]]
- [[Distributed Computing]]
- [[Storage solutions]]
- [[ETL]]
- [[Data Warehouse]]
- [[SQL]]
- Command line
- [[Data storage]]
- [[Full Lifecycle Management]]

Stakeholders they interact with:
- **Data Scientists:** Collaborate to provide data pipelines and pre-processed data for advanced analytics.
- **Business Analysts:** Ensure data is structured and accessible for analysis and reporting.
- **Senior Stakeholders and Business Ambassadors:** Communicate requirements, progress, and solutions to align with business goals.
- **Software Engineers and Data Teams:** Coordinate on data production and integration processes.

Tasks They Are Usually Given
  - **Project Management:** Tracking tasks, bugs, and progress through Azure Boards.
  - **Collaboration:** Facilitating teamwork with shared repositories and continuous integration workflows.
  - **Continuous Learning:** Keeping up-to-date with the latest technologies and updating pipelines due to obsolescence of tech
  - **Documentation and Security**: Creating documentation, implementing security measures, and exploring system upgrades for enhanced efficiency.

Tools they use:
  - **Snowflake:** [[Cloud]]-based data warehousing for scalable storage and processing.
  - **Microsoft SQL Server:** SQL-based relational database management.
  - **Azure SQL Database:** Managed relational database service on Azure.
  - **Azure Data Lake Storage:** Scalable storage for big data analytics.
  - **SQL and T-SQL:** Query languages for managing and querying relational databases.
  - **AWS S3:** Storage for data lakes.

## What is Data Engineering

The definition from the [Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/), as it’s one of the most recent and complete: 
> Data engineering is the development, implementation, and maintenance of systems and processes that take in raw data and produce high-quality, consistent information that supports downstream use cases, such as analysis and machine learning. Data engineering intersects security, [[data management]], DataOps, data architecture, orchestration, and software engineering.

A [[Data Engineer]] today oversees the whole data engineering process, from collecting data from various sources to making it available for downstream processes. The role requires familiarity with the multiple stages of the [Data Engineering Lifecycle](term/data%20engineering%20lifecycle.md) and an aptitude for evaluating data tools for optimal performance across several dimensions, including price, speed, flexibility, scalability, simplicity, reusability, and interoperability.

Data Engineering helps also overcome the bottlenecks of [Business Intelligence](term/business%20intelligence.md):
- More transparency as tools are open-source mostly
- More frequent data loads
- Supporting [Machine Learning](Machine%20Learning.md) capabilities 

Compared to existing roles it would be a **software engineering plus business intelligence engineer including big data abilities** as the [Hadoop](term/apache%20hadoop.md) ecosystem, streaming, and computation at scale. Business creates more reporting artifacts themselves but with more data that needs to be collected, cleaned, and updated near real-time and complexity is expanding every day.

With that said more programmatic skills are needed similar to software engineering. **The emerging language at the moment is [Python](term/python.md)** which is used in engineering with tools alike [[Apache Airflow]], [dagster](dagster.md), [[Prefect]] as well as data science with powerful libraries.

As a data engineer, you use mainly [SQL](term/sql.md) for almost everything except when using external data from an API. Here you'd use [ELT](term/elt.md) tools or write some [[data pipelines]] with the tools mentioned above.



