---
aliases: 
category: 
date modified: 1-08-2025
tags:
  - database
  - management
  - SQL
---
Think of PostgreSQL as the “brains” — it does the actual work of managing data.

- Type: Database management system (DBMS).
- Role: The actual database engine that stores, processes, and manages your data.
- Nature: Runs as a server process and is accessed via SQL queries (e.g., through `psql`, scripts, or applications).
- Usage:
    - Define schemas, tables, indexes, and relationships.
    - Insert, query, update, and delete data.
    - Handle transactions, concurrency, and security.
- Interface: Can be used purely via command line or programmatically through APIs/drivers (Python `psycopg2`, JDBC, etc.).

Related:
- [[pgAdmin]]