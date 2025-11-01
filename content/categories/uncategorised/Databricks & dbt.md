---
aliases: []
category:
date modified: 22-10-2025
tags:
  - data_integration
  - data_modeling
  - data_pipeline
  - governance
---
## How [[dbt]] and [[Databricks]] work together

When using dbt with Databricks, dbt becomes the transformation orchestration layer on top of the Databricks SQL engine (or Spark).

You connect dbt to Databricks using a dbt adapter (e.g., `dbt-databricks`). Then dbt compiles your SQL models into Databricks-compatible SQL and executes them there.

### The typical flow:

1. Data ingestion: Data lands in Databricks (raw zone) via ETL tools (e.g., Fivetran, Airbyte).
2. Transformation: dbt connects to Databricks, and executes transformations defined in dbt models — creating clean “silver” and “gold” tables.
3. Analytics/ML: Cleaned and modeled data is then used within Databricks notebooks, dashboards, or ML pipelines.

## Why you’d use dbt inside Databricks

Using dbt in Databricks gives you:

* Modular, version-controlled SQL transformations
* Data quality tests (e.g., assert non-null keys, unique constraints)
* Dependency management between models
* Documentation and lineage auto-generated from your models
* CI/CD integration for deployment and testing

In contrast, Databricks alone gives you:

* Raw compute and storage
* Execution of arbitrary data workloads
* Broader support for Python/ML pipelines

So dbt adds governance, structure, and maintainability to your SQL transformations in Databricks.

### Analogy

| Concept          | Databricks                         | dbt                                     |
| ---------------- | ---------------------------------- | --------------------------------------- |
| Primary function | Compute & storage (data lakehouse) | Transform & model data                  |
| Language focus   | SQL, Python, Scala, R              | SQL                                     |
| Execution        | Runs Spark jobs / SQL queries      | Orchestrates SQL models                 |
| Purpose          | Platform for all data workloads    | Framework for analytics transformations |
| Works with       | Delta tables, Unity Catalog        | Databricks SQL endpoint or cluster      |

### Example

Suppose you have a raw table in Databricks:
`raw.sales_transactions`

In dbt, you would define a model like this:

```sql
-- models/sales_summary.sql
SELECT 
  customer_id,
  SUM(amount) AS total_spent,
  COUNT(*) AS transactions
FROM {{ ref('raw_sales_transactions') }}
GROUP BY customer_id
```

dbt compiles this to Databricks SQL and materializes it as a Delta table in your catalog (e.g., `analytics.sales_summary`).