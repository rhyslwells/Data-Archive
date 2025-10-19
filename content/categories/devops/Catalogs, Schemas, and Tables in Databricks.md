---
aliases: []
category: DEVOPS
date modified: 19-10-2025
tags:
  - data_governance
  - data_management
  - data_storage
  - SQL
  - database
---
**Concept:**
Databricks organizes data using a **three-level namespace**: `catalog.schema.table`

**Structure:**

* **Catalog:** Top-level container (e.g., `example`).
* **Schema:** Logical grouping of related tables (e.g., `databricks`).
* **Table:** Dataset stored in Delta format (e.g., `databricks_test`).

**Example Commands:**

```python
spark.sql("CREATE CATALOG IF NOT EXISTS example")
spark.sql("CREATE SCHEMA IF NOT EXISTS example.databricks")
df.write.mode("overwrite").saveAsTable("example.databricks.databricks_test")
```

**Benefits:**

* Clear separation of data domains.
* Simplified access control and governance.
* Consistent naming and d[[Catalogs, Schemas, and Tables in Databricks]]- [[Delta Tables and Catalogs]]

In [[Databricks]], all managed data assets - including [[Delta Tables in Databricks]] are organized hierarchically within the **Unity Catalog** system.

### **Hierarchy**

```
catalog.schema.table
```

* **Catalog:** Top-level container (e.g., `main`, `example`, `samples`).
* **Schema:** Logical grouping of related tables within a catalog.
* **Table:** Actual data entity (e.g., Delta table, view, or external table).

Example:

```sql
SELECT * FROM example.sales.customers;
```

Here:

* `example` = catalog
* `sales` = schema
* `customers` = Delta Table
### **How Delta Tables Fit In**

A **Delta Table** can be:
**Managed (inside Databricks)** — stored within a specific catalog and schema.
   * Databricks manages both the metadata and physical files.
   * Example:

     ```python
     df.write.format("delta").saveAsTable("example.sales.transactions")
     ```
### **Why Catalogs Matter**

Catalogs in Databricks:
* Provide **governance** via Unity Catalog (access control, lineage, auditing).
* Enable **data discovery** across teams.
* Help enforce consistent naming conventions and permissions.

### **Typical Structure**

| Level           | Example Name   | Description                                      |
| --------------- | -------------- | ------------------------------------------------ |
| **Catalog**     | `example`      | Project or business domain                       |
| **Schema**      | `sales`        | Logical grouping (e.g., transactions, customers) |
| **Delta Table** | `transactions` | The actual dataset stored in Delta format        |