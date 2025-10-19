---
aliases: []
category: DEVOPS
date modified: 19-10-2025
tags:
  - data_management
  - data_pipeline
  - data_storage
---
When reloading data from external sources, you may need to refresh existing tables.

**Methods:**

1. **Drop and recreate:**

   ```python
   spark.sql("DROP TABLE IF EXISTS example.databricks.my_table")
   df.write.saveAsTable("example.databricks.my_table")
   ```
2. **Overwrite with schema handling:**

   ```python
   df.write.option("overwriteSchema", "true").mode("overwrite").saveAsTable("example.databricks.my_table")
   ```

**Best Practices:**

* Use `DROP TABLE` for inconsistent or manually edited sources (e.g., spreadsheets).
* Use `mergeSchema` for additive schema changes.
* Always preview with `df.show()` before writing.