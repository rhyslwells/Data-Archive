---
aliases: []
category:
date modified: 19-10-2025
tags: [data_engineering, data_management, data_pipeline, pandas]
---
All data operations in Databricks are performed through **Spark DataFrames**, which provide distributed data structures for large-scale analytics.

Related:
- [[PySpark]]

**Typical Workflow:**

1. **Load external data:**

   ```python
   pdf = pd.read_csv(sheet_url)
   df = spark.createDataFrame(pdf)
   ```
2. **Transform and preview:**

   ```python
   df.show(5)
   df.select("Type", "Status").distinct().show()
   ```
3. **Write back to Delta:**

   ```python
   df.write.mode("overwrite").saveAsTable("example.databricks.databricks_test")
   ```

**Advantages:**

* Scalable beyond pandas limits.
* Integrates with SQL and machine learning tools.
* Native interoperability with Delta Lake.