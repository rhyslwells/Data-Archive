---
title: What is Data Observability?
tags:
  - "#data_orchestration"
  - data_management
aliases:
  - monitoring
---
Data observability refers to the continuous monitoring and collection of metrics about your data to ensure its [[Data Quality]], reliability, and availability. 

It covers various aspects, such as data quality, pipeline health, metadata management, and infrastructure performance. By tracking key metrics and [[Outliers|anomalies]], it helps detect issues like data freshness problems, schema changes, or pipeline failures before they impact downstream processes or users.
### Categories of Observability

Auto-profiling Data:

Automatically tracks data attributes, such as row count, column types, data distributions, and schema changes.
 - Bigeye: Provides ML-driven threshold tests and automatic alerts when data drifts beyond expected ranges.
 - Datafold: Integrates with GitHub to run data diffs between environments, offering insights into differences between datasets during development.
 - Monte Carlo: Enterprise-focused with data lake integrations for comprehensive observability.
 - Metaplane: Offers a high level of configuration and both out-of-the-box and custom tests.

Pipeline Testing:

Ensures that data transformation pipelines are functioning correctly by verifying the quality and accuracy of data as it moves through different stages.
 - Great Expectations: An open-source tool that allows you to define tests and automatically generate documentation for those tests, promoting transparency in data quality checks.
 - Soda: Offers pipeline testing with the flexibility of a self-hosted option for more control over data quality monitoring.
 - [[dbt]]tests: Integrated with [[dbt]] Core and dbt Cloud, allowing testing during the transformation process in a dbt project.

 Infrastructure Monitoring:
 
Monitors the health and performance of the underlying data infrastructure, such as databases, pipelines, and servers, to prevent failures and bottlenecks.
 - DataDog: Provides deep monitoring capabilities, including for Airflow, containers, and custom metrics, allowing visibility at various layers of the data stack.

### Managing Metadata

Managing metadata is critical for observability, as it provides context and lineage for your data. Metadata can include:

- Technical Metadata: Information about the dataset’s structure, such as table schema, data types, and column descriptions.
- Operational Metadata: Information about the dataset’s freshness, when it was last updated, and the number of records processed.
- Business Metadata: Describes the meaning of data, such as field definitions and business rules, helping stakeholders understand the context and usage of the dataset.

How to Manage Metadata:

- Manual Documentation: Teams may manually document metadata, but this can be prone to human error and inconsistency.
- Automated Metadata Management: Many modern data tools, such as data catalogs (e.g., Atlan, Alation), automatically track and manage metadata, offering insights into data lineage, schema changes, and data usage.
- Integration with Data Pipelines: Tools like dbt also generate metadata about transformations, which can be included in downstream monitoring systems to ensure consistency and traceability.
