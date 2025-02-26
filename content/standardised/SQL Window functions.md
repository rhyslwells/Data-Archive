SQL Window Functions are a feature in SQL that allow you to perform calculations across a set of table rows that are somehow related to the current row. 

Unlike regular aggregate functions, which return a single value for a group of rows, window functions return a value for each row in the result set while still allowing access to the individual row data.

### Key Characteristics of Window Functions

1. Non-Aggregating: Window functions do not collapse rows into a single output row. Instead, they perform calculations across a defined "window" of rows related to the current row.

2. OVER Clause: Window functions are defined using the `OVER` clause, which specifies the window of rows to be considered for the function.

3. Partitioning: You can partition the result set into groups using the `PARTITION BY` clause within the `OVER` clause. Each partition is processed independently.

4. Ordering: You can specify the order of rows within each partition using the `ORDER BY` clause within the `OVER` clause.
### Example Use Case

Suppose you have a table `sales` with columns `salesperson`, `region`, and `amount`. You can use window functions to calculate the total sales for each salesperson while still displaying individual sales records:

Initial Table: `employees`

| id | name    | department | salary |
|----|---------|------------|--------|
| 1  | Alice   | Sales      | 50000  |
| 2  | Bob     | Sales      | 60000  |
| 3  | Charlie | HR         | 55000  |
| 4  | David   | HR         | 70000  |
| 5  | Eve     | IT         | 80000  |
| 6  | Frank   | IT         | 75000  |

### Example [[Querying|Queries]] Using SQL Window Functions

#### 1. Using `ROW_NUMBER()`

The `ROW_NUMBER()` function assigns a unique rank to each employee within their department based on their salary.

```sql
SELECT 
    id, 
    name, 
    department, 
    salary, 
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rank
FROM employees;
```

Resulting Table:

| id | name    | department | salary | rank |
|----|---------|------------|--------|------|
| 2  | Bob     | Sales      | 60000  | 1    |
| 1  | Alice   | Sales      | 50000  | 2    |
| 4  | David   | HR         | 70000  | 1    |
| 3  | Charlie | HR         | 55000  | 2    |
| 5  | Eve     | IT         | 80000  | 1    |
| 6  | Frank   | IT         | 75000  | 2    |

#### 2. Using `SUM()` similar AVG

The `SUM()` function calculates the total salary for each department, showing the same total for each employee in that department.

```sql
SELECT 
    id, 
    name, 
    department, 
    salary, 
    SUM(salary) OVER (PARTITION BY department) AS total_department_salary
FROM employees;
```

Resulting Table:

| id | name    | department | salary | total_department_salary |
|----|---------|------------|--------|-------------------------|
| 1  | Alice   | Sales      | 50000  | 110000                  |
| 2  | Bob     | Sales      | 60000  | 110000                  |
| 3  | Charlie | HR         | 55000  | 125000                  |
| 4  | David   | HR         | 70000  | 125000                  |
| 5  | Eve     | IT         | 80000  | 155000                  |
| 6  | Frank   | IT         | 75000  | 155000                  |









[[SQL Window functions]]
   **Tags**: #data_analysis, #querying