Tasks:

- [x] LLRB: ER diagram and database creation, data collection method,

# Notes:

test

[[SQL]]
Command line

[[Data storage]]
### Description of a Data Engineer's Role

Resources:

[Link](https://www.youtube.com/watch?v=qWru-b6m030)


#### Goal:

Data engineering's primary goal is to take data from its source and save it for analysis. Data engineers come in once it is necessary to automate data gathering and analysis needs, and aim to solve how the systems handle the data flow.

#### **Role Description:**

A data engineer designs, builds, and maintains the ==infrastructure== needed to collect, process, and store large amounts of data. They ensure data is accessible and usable for analysis and reporting, ==supporting== the core business through scalable and efficient data management solutions. This role involves creating ==data pipelines, integrating data from various sources, and ensuring data quality and consistency==. Data engineers ==act as a bridge between data producers and consumers,== ensuring smooth data flow and supporting advanced analytics. They are a support role to product delivery.

Data Engineer: 
Build and optimise systems for analysts:
make pipelines and its stored. Make it accessable.
developing,testing,pipelines, integrating APIS, prep data
#### [[ETL]]
- **ETL Process (Extract, Transform, Load):**
  - **Extract:** Collecting data from different sources such as databases, APIs, or flat files. Set up API connections to pull data from multiple sources.
  - **Transform:** Cleaning and transforming the data into a usable format, including filtering, aggregating, and joining data. Combine data from different sources to create a unified dataset.
  - **Load:** Inserting the transformed data into a data warehouse (organised), database, or data lake(unorganised). Store data in a database like MySQL.

This automated process reduces manual labor and enables continuous data flow into a database. Pipelines will be build using continuous deployment and integration. And be build so that they are scaleable.

During this process they need to:
- **Data Quality Assurance:** Ensure data passes quality checks and is standardized for use.

Tech:
  - **Azure Data Factory:** Orchestration of ETL workflows.

#### Data collection


#### [[Storage solutions]]

- **Performance Optimization**: Enhancing database and data processing performance to handle large datasets effectively.

- **Data Warehousing:** Maintain and optimize data warehouses, databases, and data lakes for efficient storage and retrieval.

As the ==data grows,== the team needs a data warehouse, a repository optimized for complex analytical queries rather than simple transactions (data base). Data is organized into tables and schemas to make it meaningful for analysis. This transition from a regular database to a data warehouse improves performance and enables better insights.

Tools: 
  - **Snowflake:** [[Cloud]]-based data warehousing for scalable storage and processing.
  - **Microsoft SQL Server:** SQL-based relational database management.
  - **Azure SQL Database:** Managed relational database service on Azure.
  - **Azure Data Lake Storage:** Scalable storage for big data analytics.
  - **SQL and T-SQL:** Query languages for managing and querying relational databases.
  - **AWS S3:** Storage for data lakes.

Cost consideration
#### **Big Data**

[[Big data]] is characterized by the four V’s: ==Volume, Variety, Veracity, and Velocity==. Handling big data requires robust data engineering teams and specialized infrastructure, like distributed storage and computing.

- **Big Data Technologies:**
  - **Apache Spark:** Framework for large-scale data processing.
  - **Hadoop:** Framework for distributed storage and processing of large data sets.
  - **Scala:** Programming language for big data processing, often with Apache Spark.
  - **Databricks on Azure:** Collaborative platform for big data processing using Apache Spark.

**Distributed Computing**

Handling massive data volumes necessitates distributed computing frameworks like Hadoop, which allows data storage across clusters of servers, ensuring scalability and redundancy. Tools like Spark are used for processing data in these distributed environments.
#### [[Batch Processing]]


- Heavily intertwined with Data Processing technologies. **Apache Spark** is the gold standard
- Core idea is we have data growing at unmanageable sizes. We have tools that enable us to process them in a scalable way.
- **MapReduce** is a distributed framework within the Hadoop ecosystem
    - **Map**: split data between parallel tasks
    - **Reduce**: aggregate data
    - _The order does not matter_
- Cloud Infrastructure already exists: Amazon EMR, Databricks
- Don’t suggest learning specific tools. Instead, f

**Data Streaming and Pub/Sub Systems**

For real-time data processing, data streaming is essential. Unlike batch processing, data streaming uses a publish-subscribe (pub/sub) model. Systems like ==Kafka== allow asynchronous data flow, enabling real-time data handling and processing.
- Build real-time applications where multiple sources are feeding into a system
    - Publish + Subscribe model. Producers publish messages to Topics. Consumers subscribe to topics for information.
- **Apache Kafka** is one of the most popular frameworks.
    - High throughput. Process millions of messages per second.
    - High scalability. Thousands brokers
    - Maintains a commit log that is immutable
- Real world example
    - Netflix uses Apache Kafka for their messaging and streaming needs
    - Literally Billions of data points processed using Kafka each day
#### **Stakeholders:**

- **Data Scientists:** Collaborate to provide data pipelines and pre-processed data for advanced analytics.

Data scientists require detailed, often unstructured data for predictive modeling and analysis. This leads to the creation of a **data lake**, which stores raw data without predefined schemas. The ETL process adapts to extract, load into the lake, and then transform data as needed, providing a flexible environment for data scientists.

- **Business Analysts:** Ensure data is structured and accessible for analysis and reporting.
- **Senior Stakeholders and Business Ambassadors:** Communicate requirements, progress, and solutions to align with business goals.

**[[PowerBI]]:** Business analytics tool for data visualization and reporting.

- **Software Engineers and Data Teams:** Coordinate on data production and integration processes.

#### **Tasks They Are Usually Given:**

Soft:
  - **Project Management:** Tracking tasks, bugs, and progress through Azure Boards.
  - **Collaboration:** Facilitating teamwork with shared repositories and continuous integration workflows.
  - **Continuous Learning:** Keeping up-to-date with the latest technologies and updating pipelines due to obsolescence of tech.
- **Documentation and Security**: Creating documentation, implementing security measures, and exploring system upgrades for enhanced efficiency.