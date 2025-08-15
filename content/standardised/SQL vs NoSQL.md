---
aliases: 
category: DEVOPS
date modified: 1-08-2025
tags:
  - modeling
  - storage
  - SQL
---
SQL and NoSQL are two broad classes of database technologies, distinguished by how they structure, query, and store data.

* Use SQL when data integrity, relational logic, and transactional consistency are key.
* Use NoSQL when scalability, performance, and schema flexibility are priorities.

| Feature        | SQL                              | NoSQL                                |
| -------------- | -------------------------------- | ------------------------------------ |
| Data model     | Relational (tables, rows)        | Varies (documents, key-value, graph) |
| Schema         | Fixed / predefined               | Flexible / dynamic                   |
| Query Language | SQL                              | Varies (JSON queries, APIs, etc.)    |
| Transactions   | ACID                             | Often BASE (eventual consistency)    |
| Scalability    | Vertical (scale-up)              | Horizontal (scale-out)               |
| Best for       | Structured data, complex queries | Unstructured data, high throughput   |

Related:
- [[SQL]]
- [[NoSQL]]
