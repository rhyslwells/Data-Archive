---
tags:
  - database
---

## Summary:

1. **Read and Clean the Data**: Load the data from the Excel sheet and clean it.
2. **Split the Data**: Separate the data into two DataFrames, one for customers and one for orders.
3. **Create Tables**: Create the SQLite tables with appropriate foreign key relationships.
4. **Insert Data**: Insert the cleaned and separated data into the respective tables.
5. **Verify Foreign Keys**: Ensure that the foreign key relationships are valid.

## Key Concepts

- **Primary Key (PK)**: A unique identifier for each record in a table.
- **Foreign Key (FK)**: A field in one table that uniquely identifies a row of another table.

## Example Data Structure

### Combined Excel Data (`Sheet1`):

| order_id | order_date | customer_id | customer_name | contact_name | country | amount |
|----------|------------|-------------|---------------|--------------|---------|--------|
| 1        | 2024-01-15 | 101         | John Doe      | Jane Doe     | USA     | 100.50 |
| 2        | 2024-02-20 | 102         | Alice Smith   | Bob Smith    | Canada  | 200.00 |
| 3        | 2024-03-10 | 101         | John Doe      | Jane Doe     | USA     | 150.75 |
| 4        | 2024-04-05 | 103         | Michael Brown | Sarah Brown  | UK      | 250.00 |

## Steps to Process and Split Data

### Step 1: Import Libraries and Read Data

```python
import pandas as pd
import sqlite3

# Example data for demonstration purposes
data = {
    'order_id': [1, 2, 3, 4],
    'order_date': ['2024-01-15', '2024-02-20', '2024-03-10', '2024-04-05'],
    'customer_id': [101, 102, 101, 103],
    'customer_name': ['John Doe', 'Alice Smith', 'John Doe', 'Michael Brown'],
    'contact_name': ['Jane Doe', 'Bob Smith', 'Jane Doe', 'Sarah Brown'],
    'country': ['USA', 'Canada', 'USA', 'UK'],
    'amount': [100.50, 200.00, 150.75, 250.00]
}

# Create a DataFrame from the example data
df = pd.DataFrame(data)
```

### Step 2: Clean Data

```python
# Example cleaning function
def clean_data(df):
    df.dropna(inplace=True)
    df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]
    return df

# Clean the data
df = clean_data(df)
```

### Step 3: Split Data into Customers and Orders

```python
# Extract unique customers
customers_df = df[['customer_id', 'customer_name', 'contact_name', 'country']].drop_duplicates()

# Extract orders
orders_df = df[['order_id', 'order_date', 'customer_id', 'amount']]
```

### Step 4: Create Tables with Foreign Keys in SQLite

```python
# Connect to SQLite database (or create it)
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Enable foreign key support
cursor.execute("PRAGMA foreign_keys = ON")

# Create 'customers' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    contact_name TEXT,
    country TEXT
)
''')

# Create 'orders' table with a foreign key referencing 'customers'
cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    order_date TEXT,
    customer_id INTEGER,
    amount REAL,
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
)
''')

# Commit changes
conn.commit()
```

### Step 5: Insert Data into Tables

```python
# Insert data into 'customers' table
customers_df.to_sql('customers', conn, if_exists='append', index=False)

# Insert data into 'orders' table
orders_df.to_sql('orders', conn, if_exists='append', index=False)

# Commit changes and close the connection
conn.commit()
conn.close()
```

### Verification: Ensure Foreign Key Relationships

```python
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Query to check if all customer_id in orders table exist in customers table
cursor.execute('''
SELECT order_id
FROM orders
WHERE customer_id NOT IN (SELECT customer_id FROM customers)
''')

invalid_orders = cursor.fetchall()
conn.close()

if invalid_orders:
    print("Invalid foreign key references found:", invalid_orders)
else:
    print("All foreign key references are valid.")
```

