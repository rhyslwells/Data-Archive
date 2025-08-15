---
aliases: 
category: 
date modified: 1-08-2025
tags:
  - transformation
  - SQL
---
The [[SQL]] `GROUP BY` clause is used to group rows that have the same values in specified columns into summary rows, like "total sales per region" or "average age per department." 

It is often used in conjunction with aggregate functions such as `COUNT()`, `SUM()`, `AVG()`, `MAX()`, and `MIN()` to perform calculations on each group.
### Basic Syntax

```sql
SELECT column1, aggregate_function(column2)
FROM table_name
WHERE condition
GROUP BY column1;
```

### Example Usage

Let's say you have a table called `sales` with the following columns:

- `id`: Unique identifier for each sale
- `product`: The name of the product sold
- `amount`: The sale amount
- `region`: The region where the sale occurred

#### 1. Count the Number of Sales per Product

To count how many sales were made for each product, you would use:

```sql
SELECT product, COUNT(*) AS total_sales
FROM sales
GROUP BY product;
```

#### 2. Calculate Total Sales Amount per Region

To calculate the total sales amount for each region, you would use:

```sql
SELECT region, SUM(amount) AS total_sales_amount
FROM sales
GROUP BY region;
```

### Using `HAVING` with `GROUP BY`

You can also filter the results of a `GROUP BY` [[Querying|query]] using the `HAVING` clause. This is useful when you want to filter groups based on aggregate values.

#### Example: Filter Groups

For example, to find products with total sales greater than $1000:

```sql
SELECT product, SUM(amount) AS total_sales_amount
FROM sales
GROUP BY product
HAVING SUM(amount) > 1000;
```

### Important Points

- **Columns in SELECT**: When using `GROUP BY`, all columns in the `SELECT` statement must either be included in the `GROUP BY` clause or be used in an aggregate function.
- **Order of Execution**: The `GROUP BY` clause is processed after the `WHERE` clause but before the `ORDER BY` clause in the SQL execution order.





[[SQL Groupby]]
   **Tags**: 