---
tags:
  - database
---


- Views can remove unnecessary columns and simplify data representation.
- **Views**: Virtual tables defined by queries, useful for simplifying complex data, aggregating results, partitioning data, and securing sensitive information.

```sql
CREATE VIEW longlist AS
SELECT name, title FROM authors
JOIN authored ON authors.id = authored.author_id
JOIN books ON books.id = authored.book_id;
```
**Benefits**:

1. **==Simplification==**:
    - Simplifies complex queries by joining tables in a view.
2. **Aggregation**:
    - Example: Calculating average book ratings and storing results in a view.
3. **Partitioning**:
    - Creating views to store data for specific years or categories.
4. **Securing**:
    - Limiting access to sensitive data by creating views that omit or anonymize certain columns.

**Advanced Usage**:

- **Temporary Views**: Exist only for the duration of the database connection.
- **Common Table Expressions (CTEs)**: Temporary views for a single query.
- ==**Soft Deletions**==: Using views and triggers to mark data as deleted without removing it from the table.
- 
Question: why use views?

Using views in SQL offers several benefits:

1. **Simplification and Abstraction**:
   - Views allow you to simplify complex queries. Instead of writing a complex join or aggregation each time, you can encapsulate it in a view and select from the view.
   - They provide a level of abstraction. Users can interact with the data without needing to understand the underlying table structure or query logic.

2. **Security**:
   - Views can be used to restrict access to specific data. By granting users access to a view rather than the underlying tables, you can control what data they see and manipulate.
   - ==ACCESS controls== cant do in sqlite, can in others.

3. **Reusability and Maintainability**:
   - Views allow you to reuse SQL queries. You can define a complex query once in a view and use it in multiple places.
   - They can simplify maintenance. If the logic for a derived column changes, you only need to update the view definition rather than every place that uses the logic.

4. **Data Consistency and Integrity**:
   - Views ensure consistent presentation of the data. When multiple applications or users query the database, views ensure they get the same results based on the same underlying logic.
   - They can encapsulate business logic, ensuring that certain calculations or constraints are consistently applied.

5. **Performance Optimization**:
   - Although views themselves do not inherently improve performance, materialized views (a type of view that stores the result set) can improve performance for complex queries by storing the precomputed results.
   - Regular views can simplify query optimization by breaking down complex queries into simpler, manageable components.

6. **Logical Data Independence**:
   - Views provide a level of indirection between the physical storage of data and how it is accessed. Changes to the underlying schema can often be made without affecting the users of the view.


