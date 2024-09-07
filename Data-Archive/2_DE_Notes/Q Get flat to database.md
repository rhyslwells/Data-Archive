---
tags:
  - SQL
aliases: 
type: 
created: 2024-06-21 16:04
---
To achieve this, you'll need to read the flat file into a pandas DataFrame, separate the data into two DataFrames for customers and orders, and then establish a foreign key relationship between them. Here’s how you can do this step-by-step:

1. **Read the flat file into a pandas DataFrame**.
2. **Separate the data into customers and orders DataFrames**.
3. **Assign a unique customer ID to each customer**.
4. **Use this customer ID as a foreign key in the orders DataFrame**.

Here's a detailed example assuming the flat file is a CSV file:

### Sample Data

Let's assume the flat file (e.g., `data.csv`) has the following structure:

```csv
customer_name,customer_email,order_id,order_date,order_amount
John Doe,johndoe@example.com,1001,2024-06-15,250
Jane Smith,janesmith@example.com,1002,2024-06-16,150
John Doe,johndoe@example.com,1003,2024-06-17,300
```

### Python Code

1. **Read the flat file into a pandas DataFrame**:

```python
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')
```

2. **Separate the data into customers and orders DataFrames**:

```python
# Create a customers DataFrame
customers = df[['customer_name', 'customer_email']].drop_duplicates().reset_index(drop=True)

# Add a unique customer_id to the customers DataFrame
customers['customer_id'] = customers.index + 1

# Create an orders DataFrame
orders = df[['customer_email', 'order_id', 'order_date', 'order_amount']]
```

3. **Assign a unique customer ID to each customer and establish a foreign key in the orders DataFrame**:

```python
# Merge the orders DataFrame with the customers DataFrame to get the customer_id
orders = orders.merge(customers[['customer_email', 'customer_id']], on='customer_email', how='left')

# Drop the customer_email column as it's no longer needed in the orders DataFrame
orders = orders.drop(columns=['customer_email'])
```

### Resulting DataFrames

**Customers DataFrame**:

```python
print(customers)
```

```
  customer_name     customer_email  customer_id
0      John Doe  johndoe@example.com            1
1    Jane Smith  janesmith@example.com            2
```

**Orders DataFrame**:

```python
print(orders)
```

```
   order_id   order_date  order_amount  customer_id
0      1001  2024-06-15          250            1
1      1002  2024-06-16          150            2
2      1003  2024-06-17          300            1
```

### Summary

- The `customers` DataFrame contains unique customer information with a new `customer_id`.
- The `orders` DataFrame contains order information with a `customer_id` as a foreign key, linking orders to customers.

You can now proceed to use these DataFrames for further analysis or save them to new CSV files, databases, etc. Here's how you can save them back to CSV files:

```python
customers.to_csv('customers.csv', index=False)
orders.to_csv('orders.csv', index=False)
```

This approach ensures that the orders are properly linked to the corresponding customers using a foreign key, facilitating more structured data management and analysis.