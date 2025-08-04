---
aliases: []
category:
date modified: 1-08-2025
tags: [database]
---
Views are virtual tables defined by SQL [[Querying|Query]] that ==simplify complex data representation.== They can remove unnecessary columns, aggregate results, partition data, and secure sensitive information.

In [[DE_Tools]] see:
https://github.com/rhyslwells/DE_Tools/blob/main/Explorations/SQLite/Viewing/Viewing.ipynb

Basic Usage:
- Simplification
- Aggregation (using GROUP)
- [[Common Table Expression]]
- Securing data: can give all values in a field the same value.

Advanced Usage
- Temporary Views: Exist only for the ==duration of the database connection.==
- [[Common Table Expression]]: Serve as temporary views for a single query.
- [[Soft Deletion]]: Use views and triggers to mark records as deleted without physically removing them from the table.

Related topics:
- [[View Use Case]]

## Why Use Views?

1. **Simplification and Abstraction**:
   - Views encapsulate complex queries, allowing users to interact with data without needing to understand the underlying structure. This simplifies data retrieval by hiding complexity.

2. **Security**:
   - Views restrict access to specific data by granting users access to views instead of underlying tables, which can help protect sensitive information. Note: Access controls may vary by database system (e.g., not available in [[SQLite]]).

3. **Reusability and [[Maintainability]]**:
   - Define complex queries once in a view and reuse them across multiple applications, simplifying maintenance when logic changes.

4. **Data Consistency and Integrity**:
   - Ensure consistent data presentation across applications and users by encapsulating business logic for uniform calculations.

5. **Performance Optimization**:
   - While regular views do not inherently improve performance, materialized views can enhance performance by storing precomputed results.

6. **Logical Data Independence**:
   - Provide a layer of abstraction between physical data storage and access methods, allowing [[Database Schema|schema]] changes without affecting view users.

7. **Aggregation and Partitioning**:
   - Views can be used to calculate and store aggregated results (e.g., average ratings) and organize data by specific criteria (e.g., years or categories).