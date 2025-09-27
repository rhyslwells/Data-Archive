---
aliases:
- null
category: DE
date modified: 27-09-2025
tags:
- database
- python
---
To use **DuckDB** in Python, you can follow these steps to install the DuckDB library and perform basic operations such as creating a database, running queries, and manipulating data. Here's a simple guide:

### Step 1: Install DuckDB

You can install DuckDB using pip. Open your terminal or command prompt and run:

```bash
pip install duckdb
```
### Example: Full Code

Here’s a complete example that incorporates all the steps:

```python
import duckdb

# Step 1: Connect to an in-memory database
conn = duckdb.connect(database=':memory:')

# Step 2: Create a table
conn.execute("""
CREATE TABLE users (
    id INTEGER,
    name VARCHAR,
    age INTEGER
)
""")

# Step 3: Insert data
conn.execute("""
INSERT INTO users VALUES
(1, 'Alice', 30),
(2, 'Bob', 25),
(3, 'Charlie', 35)
""")

# Step 4: Query data
result = conn.execute("SELECT * FROM users").fetchall()

# Print the results
for row in result:
    print(row)

# Step 5: Close the connection
conn.close()
```

### Additional Features

DuckDB also supports advanced features such as:

- **Reading from CSV and Parquet files**: You can load data directly from these formats using commands like `READ_CSV` or `READ_PARQUET`.
- **Integration with Pandas**: You can easily convert DuckDB query results to Pandas DataFrames for further analysis.

### Example of Reading from a CSV

```python
# Load data from a CSV file into a DuckDB table
conn.execute("CREATE TABLE my_data AS SELECT * FROM read_csv_auto('path/to/your/file.csv')")
```