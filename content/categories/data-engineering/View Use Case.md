---
aliases: []
category: DE
date modified: 27-09-2025
tags:
- cleaning
- explainability
- transformation
---
## View Use Case

### Scenario

A company wants to generate monthly performance reports for its employees. The performance data is spread across multiple tables, including `employees`, `departments`, and `performance_reviews`. ==Instead of writing complex queries== every time a report is needed, the company can create a view that simplifies data retrieval.

### Step 1: Define the Tables

Assume we have the following tables:

- **employees**: Contains employee details.
  - `employee_id`
  - `name`
  - `department_id`

- **departments**: Contains department details.
  - `department_id`
  - `department_name`

- **performance_reviews**: Contains performance review data.
  - `review_id`
  - `employee_id`
  - `review_score`
  - `review_date`

### Step 2: Create a View

To simplify the reporting process, we create a view that joins these tables and aggregates the performance scores:

```sql
CREATE VIEW employee_performance AS
SELECT 
    e.employee_id,
    e.name,
    d.department_name,
    AVG(pr.review_score) AS average_score
FROM 
    employees e
JOIN 
    departments d ON e.department_id = d.department_id
JOIN 
    performance_reviews pr ON e.employee_id = pr.employee_id
GROUP BY 
    e.employee_id, e.name, d.department_name;
```

### Step 3: Query the View

Now, whenever the HR department needs to generate a performance report, they can simply query the `employee_performance` view:

```sql
SELECT * FROM employee_performance WHERE average_score >= 4.0;
```

This query retrieves all employees with an average performance score of 4.0 or higher, making it easy to identify top performers.

### Benefits of Using Views in This Use Case

1. **Simplification**: The view encapsulates complex joins and aggregations, allowing HR to retrieve performance data without needing to understand the underlying table structure.

2. **Reusability**: The view can be reused for different reports, such as quarterly reviews or department-specific performance assessments.

3. **[[Maintainability]]**: If the logic for calculating performance scores changes, the HR team only needs to update the view definition, not every individual query.

4. **Data Consistency**: All reports generated from the view will be consistent, as they rely on the same underlying logic for calculating average scores.

5. **[[Data Security]]**: If sensitive employee data needs to be protected, the view can be designed to exclude certain columns, ensuring that only necessary information is accessible.