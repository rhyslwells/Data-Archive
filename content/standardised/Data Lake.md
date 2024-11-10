---
title: What is a Data Lake?
tags:
  - data_storage
---
A Data Lake is a storage system with vast amounts of [[unstructured data]] and [[structured data]], stored as-is, without a specific purpose in mind, that can be built on multiple technologies such as Hadoop, NoSQL, Amazon Simple Storage Service, a relational database, or various combinations and different formats (e.g. Excel, CSV, Text, Logs, etc.).

**Definition**: A repository that ==stores diverse data types==, including structured, semi-structured, and unstructured data. If cant fit into a database.

Features:
- **Versatility**: Can accommodate various data formats, including videos, images, documents, and more.
- **Raw Data Storage**: Preserves data in its raw form, suitable for advanced analytics, particularly in machine learning and AI.
- **Data Usability**: Raw data ==may require cleaning and transformation for analytical use==, often transferred to databases or data warehouses.
- **Use Case**: Valuable for storing large volumes of raw data, especially in contexts requiring advanced analytics and experimentation.

[[unstructured data]] for predictive modeling and analysis. This leads to the creation of a **data lake**, which stores raw data without predefined schemas. 

The data lake supports the following capabilities:
-   To capture and store raw data at scale for a low cost
-   To store many types of data in the same repository
-   To perform [Data Transformation](Data%20Transformation.md) on the data where the purpose may not be defined
-   To perform new types of data processing
-   To perform single-subject analytics based on particular use cases

Components of a data lake
		1. [Storage Layer](term/storage%20layer%20object%20store.md)
		2. [Data Lake File Format](term/data%20lake%20file%20format.md)
		3. [Data Lake Table Format](term/data%20lake%20table%20format.md) with [Apache Parquet](term/apache%20parquet.md), [Apache Iceberg](term/apache%20iceberg.md), and [Apache Hudi](term/apache%20hudi.md)