---
aliases: []
category: DATA_ANALYSIS
date modified: 27-09-2025
tags:
- storage
---
A **Parquet file** is a **columnar storage file format** specifically designed for storing large amounts of data efficiently. It is commonly used in [[Big Data]] ecosystems due to its optimised performance for both storage and querying.

[[Data Storage]]
### Key Features of Parquet:

1. **Columnar Storage Format:**
    - Data is stored **column by column** instead of row by row.
    - This design is highly efficient for analytical queries that access only specific columns, reducing the amount of data read.
      
2. **Optimised for Big Data:**
    - Parquet is designed for distributed systems like Apache [[Hadoop]], [[Apache Spark]], and other big data processing tools.
      
3. **Compression:**
    - It supports multiple compression algorithms (e.g., Snappy, GZIP) for reducing file size while maintaining fast read and write performance.
      
4. **[[Schema Evolution]]:**
    - Parquet supports flexible schemas, allowing fields to be added or modified without breaking compatibility with older data.
      
5. **Efficient [[Metadata Handling]]:**
    - Metadata is stored along with the data, making it easier to retrieve and query information about the dataset without scanning the entire file.

### Advantages of Parquet:

1. **Improved Query Performance:**
    - Since data is stored column-wise, queries that require only a few columns read less data compared to row-based formats like CSV.
      
2. **Lower Storage Costs:**
    - Built-in compression and columnar storage **significantly reduce file size.**
      
3. **Compatibility:**
    - Parquet is compatible with most big data processing tools, such as Hadoop, Spark, Hive, Presto, and AWS Athena.

1. **Efficient I/O:**
    - Parquet’s columnar format minimises disk I/O, making it faster to process large datasets.

---

### When to Use Parquet:
- **Analytical Workloads:** Ideal for scenarios where you need to perform aggregations, filtering, or processing large datasets.
- **Big Data Processing:** Frequently used with tools like Spark, Hive, and Presto in data lakes.
- **Cloud Storage:** Supported by [[Cloud Providers]] platforms.

### Example Use Case:

Imagine a dataset with 10 million rows and 100 columns.

- If you query just 3 columns in a row-based format (e.g., CSV), you must read all 100 columns for every row.
- In Parquet, only the 3 relevant columns are read, significantly improving performance.

---

### File Structure:

- **Row Group:** Data is divided into chunks called row groups, enabling efficient data retrieval.
- **Columns:** Each column in a row group is stored together for fast access.
- **Footer:** Contains metadata, such as schema definitions and row group locations, allowing quick navigation of the file.

---

### How to Work with Parquet in Python:

You can use libraries like **pandas** or **pyarrow**:

```python
import pandas as pd

# Write a DataFrame to a Parquet file
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df.to_parquet('example.parquet', engine='pyarrow')

# Read a Parquet file into a DataFrame
df_read = pd.read_parquet('example.parquet')
print(df_read)
```

---

In summary, Parquet is an efficient, compact, and scalable file format ideal for big data analytics and storage, providing faster performance and reduced costs.