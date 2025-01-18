---
title: 
tags:
  - field
aliases: 
category:
---
The definition from the [Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/), as it’s one of the most recent and complete: 

> Data engineering is the development, implementation, and maintenance of systems and processes that take in raw data and produce high-quality, consistent information that supports downstream use cases, such as analysis and machine learning. Data engineering intersects security, [[Data Management]], DataOps, data architecture, orchestration, and software engineering.

A [[Data Engineer]] today oversees the whole data engineering process, from collecting data from various sources to making it available for downstream processes. The role requires familiarity with the multiple stages of the [Data Engineering Lifecycle](Full%20Lifecycle%20Management.md) and an aptitude for evaluating data tools for optimal performance across several dimensions, including price, speed, flexibility, scalability, simplicity, reusability, and interoperability.

Data Engineering helps also overcome the bottlenecks of [Business Intelligence](term/business%20intelligence.md):
- More transparency as tools are open-source mostly
- More frequent data loads
- Supporting [Machine Learning](Machine%20Learning.md) capabilities 

Compared to existing roles it would be a **software engineering plus business intelligence engineer including big data abilities** as the [Hadoop](term/apache%20hadoop.md) ecosystem, streaming, and computation at scale. Business creates more reporting artifacts themselves but with more data that needs to be collected, cleaned, and updated near real-time and complexity is expanding every day.

With that said more programmatic skills are needed similar to software engineering. **The emerging language at the moment is [Python](term/python.md)** which is used in engineering with tools alike [[Apache Airflow]], [dagster](dagster.md), [[Prefect]] as well as data science with powerful libraries.

As a data engineer, you use mainly [SQL](term/sql.md) for almost everything except when using external data from an API. Here you'd use [ELT](term/elt.md) tools or write some [[Data Pipeline]] with the tools mentioned above.