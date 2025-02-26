---
tags:
  - database
---
Views are virtual tables defined by SQL [[queries]] that simplify complex data representation. They can remove unnecessary columns, aggregate results, partition data, and secure sensitive information.

Example
```sql
CREATE VIEW longlist AS
SELECT name, title FROM authors
JOIN authored ON authors.id = authored.author_id
JOIN books ON books.id = authored.book_id;
```

## Advanced Usage

- Temporary Views: Exist only for the ==duration of the database connection.==
- [[Common Table Expression]]: Serve as temporary views for a single query.
- [[Soft Deletion]]: Use views and triggers to mark records as deleted without physically removing them from the table.

Related topics:
- [[View Use Case]]
- [[Why Use Views]]



