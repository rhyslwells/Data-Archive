---
tags:
  - SQL
---


[LINK](https://cs50.harvard.edu/sql/2024/weeks/0/)

[[Database]]

SQL: the language used to interact with a database. Structured Query Language.

Querying: Asking questions of data.

end note: All of these actually exists. (transcript)

--- 


#### Transition from Spreadsheets to Databases
- **Limitations of Spreadsheets**:
  - Not suitable for large-scale data (millions/billions of records).
  - Limited update frequency and speed.
- **Advantages of Databases**:
  - Scalability.
  - Frequent updates.
  - Speed in querying data.

#### Database Concepts
- **Database Definition**:
  - Organizes data to create, read, update, and delete ([[CRUD]] operations).
- **Database Management System (DBMS)**:
  - Software to interact with databases (e.g., MySQL, Oracle, PostgreSQL, SQLite).
  - DBMS Types:
    - Proprietary (paid, with support).
    - Open source (free, self-supported).

#### SQL Overview
- **SQL Definition**: Structured Query Language.
  - Used to query, create, read, update, delete data.
- **Popular SQL-Based DBMS**:
  - MySQL, PostgreSQL, SQLite.
- **SQL Keywords**:
  - **SELECT**: Retrieve data.
  - **LIMIT**: Restrict number of rows returned.
  - **WHERE**: Filter rows based on conditions.

#### Tools and Environment
- **VS Code**: Integrated Development Environment (IDE).
- **[[SQLite]]**: Lightweight DBMS used in various applications (phone apps, desktop apps, websites).

To get in terminal enter: sqlite3 database.db

---


#### SQL Commands and Examples
- **Basic ==SELECT== Statement**:
  - `SELECT * FROM longlist;` retrieves all data.
  - `SELECT title FROM longlist;` retrieves book titles.
  - `SELECT title, author FROM longlist;` retrieves titles and authors.

- **Using LIMIT**:
  - `SELECT title FROM longlist LIMIT 10;` retrieves the first 10 rows.
  - `SELECT title FROM longlist LIMIT 5;` retrieves the first 5 rows.

- **Filtering with WHERE**:
  - `SELECT title, author FROM longlist WHERE year = 2023;` retrieves books from 2023.
  - **Not Equals**:
    - `SELECT title, format FROM longlist WHERE format != 'hardcover';`
    - `SELECT title, format FROM longlist WHERE format <> 'hardcover';`
  - **NOT Keyword**:
    - `SELECT title, format FROM longlist WHERE NOT format = 'hardcover';`

- **Combining Conditions**:
  - Future lessons will cover more complex conditions (e.g., filtering by multiple years).

#### Good Practices
- **Capitalization**:
  - SQL keywords in uppercase for readability.
  - Table and column names in lowercase.
- **Quotes**:
  - Double quotes for SQL identifiers (table and column names).
  - Single quotes for strings.

These notes provide a structured summary of the introductory lecture on databases and SQL, covering the key points and examples presented by Carter Zenke.


## LIKE  with % and _

```
SELECT "title" 
FROM "longlist" 
WHERE "title" LIKE 'P_re';
```


