---
title: What is ETL?
tags:
  - data_transformation
---
- [[ETL Pipeline Example]]
- [[etl vs elt]]

This automated process reduces manual labor and enables continuous data flow into a [[database]]. Pipelines will be build using continuous deployment and integration. And be build so that they are scaleable.

**ETL Process (Extract, Transform, Load):**
  - **Extract:** Collecting data from different sources such as databases, APIs, or flat files. Set up API connections to pull data from multiple sources.
  - **Transform:** Cleaning and transforming the data into a usable format, including filtering, aggregating, and joining data. Combine data from different sources to create a unified dataset.
  - **Load:** Inserting the transformed data into a data warehouse (organised), database, or data lake(unorganised). Store data in a database like MySQL.

ETL (Extract, [Transform](Data%20Transformation.md), and Load) is a paradigm for moving data from one system to another. It involves reading data (Extract) from one system, modifying the data (Transform), and then sending it (Load) to a destination system. The ETL paradigm emerged in the 1970s. 

A key feature of ETL is that data is transformed before being sent to the destination, as demonstrated in the following image:

![](etl-tool.png)

During the [[ETL]] process necessary to:
- **[[Data Quality]] Assurance:** Ensure data passes quality checks and is standardized for use.

However in recent years, the preferred data movement paradigm has shifted to [ELT](term/elt.md) (Extract, Load, and Transform). The ELT philosophy dictates that data should be untouched – apart from minor cleaning and filtering – as it moves through the extraction and loading stages so that the raw data is always accessible in the destination [Data Warehouse](Data%20Warehouse.md). See [ETL vs ELT](term/etl%20vs%20elt.md) for a comparison of these approaches.
## ETL is Changing

ETL is done with [[Apache Airflow]], [[dagster]], and [Temporal](term/temporal.md). 

Historically **ETL was once preferred** over [[ELT]] for the following **no-longer-valid reasons**: 

- ETL could achieve cost savings by removing unwanted data before sending it to the destination –  however, with the plummeting cost of cloud-based computation and storage the value of this proposition is greatly reduced. 
- Because ETL transforms data ==before it is stored==, it avoids the complexity of transforming data _after_ sending it to the destination – however, new tools such as [[dbt]] (data build tool) make it preferable and easy to transform data in the destination.

