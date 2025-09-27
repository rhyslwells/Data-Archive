---
aliases: []
category: DE
date modified: 27-09-2025
tags:
- data
- null
- SQL
---
\#database\_storage

**MariaDB** is an **open-source relational database management system (RDBMS)**. It was originally created as a fork of **MySQL** in 2009, after concerns arose that Oracle Corporation’s acquisition of [[MySql]] might limit its open-source future.

### Key Points:

* **Origin**: Developed by the original creators of MySQL, led by Michael "Monty" Widenius.
* **Compatibility**: Designed to remain highly compatible with MySQL (same commands, APIs, and table definitions), so applications built for MySQL often work with MariaDB without modification.
* **Storage Engines**: Supports MySQL storage engines but also introduces its own, such as **Aria** and **ColumnStore** (for analytical workloads).
* **Performance**: Generally optimized for speed, scalability, and stability, with features like thread pooling and query optimizations.
* **License**: Released under the **GPL (General Public License)**, ensuring it remains open-source.
* **Use Cases**:
  * Web applications (often used as a backend in LAMP/LEMP stacks).
  * Data warehousing (with MariaDB ColumnStore).
  * Enterprise systems that need high availability and replication.

### Example:

```sql
-- Creating a database in MariaDB
CREATE DATABASE company;

-- Creating a table
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    department VARCHAR(50),
    salary DECIMAL(10,2)
);

-- Inserting data
INSERT INTO employees (name, department, salary)
VALUES ('Alice', 'Engineering', 60000.00);
```

Related:
- [[MariaDB vs MySQL]]