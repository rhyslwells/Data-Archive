---
aliases: []
category: DEVOPS
date modified: 19-10-2025
tags:
  - data_collection
  - data_integration
  - data_pipeline
  - data_storage
---
**Purpose:**
To import and persist data from a [[Google Sheets]] into a [[Databricks]] managed [[Delta Tables in Databricks|Delta Table]] for querying and integration with Spark-based workflows.

**Process Overview:**

1. Export the Google Sheet as CSV via its public link:

   ```python
   sheet_url = "https://docs.google.com/spreadsheets/d/.../export?format=csv&gid=0"
   ```
2. Read the CSV into a pandas DataFrame:

   ```python
   pdf = pd.read_csv(sheet_url)
   ```
3. Convert to a Spark DataFrame:

   ```python
   df = spark.createDataFrame(pdf)
   ```
4. Save the data as a managed table in Databricks:

   ```python
   df.write.mode("overwrite").saveAsTable("example.databricks.table_name")
   ```

**Applications:**
* Automating ingestion of lightweight reference data.
* Collaborative data entry pipelines.
* Quick [[ETL]] prototypes with spreadsheet-based inputs.