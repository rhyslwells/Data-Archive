---
tags:
  - database
aliases:
  - Queries
---
Querying is the process of asking questions of data. Querying makes use of keys primary and foreign within tables.

Useful Links
- [CS50 SQL Course](https://cs50.harvard.edu/sql/2024/weeks/0/)
### SQL Commands and Examples

**Basic SELECT Statement**:
  ```sql
    SELECT * FROM longlist; -- Retrieves all data
    ```
  
  ```sql
    SELECT title FROM longlist; -- Retrieves book titles
    ```

 ```sql
    SELECT title, author FROM longlist; -- Retrieves titles and authors
    ```

**Using LIMIT**:
 ```sql
    SELECT title FROM longlist LIMIT 10; -- Retrieves the first 10 rows
```
  
 ```sql
    SELECT title FROM longlist LIMIT 5; -- Retrieves the first 5 rows
    ```

**Filtering with WHERE**:
 ```sql
    SELECT title, author FROM longlist WHERE year = 2023; -- Retrieves books from 2023
    ```
  
 **Not Equals**:
   ```sql
      SELECT title, format FROM longlist WHERE format != 'hardcover';
      ```
      
   ```sql
      SELECT title, format FROM longlist WHERE format <> 'hardcover';
      ```
 **NOT Keyword**:
   ```sql
      SELECT title, format FROM longlist WHERE NOT format = 'hardcover';
      ```

**Combining Conditions**:
  - Future lessons will cover more complex conditions, such as filtering by multiple years.

### Good Practices
**Capitalization**: 
  - Use uppercase for SQL keywords for better readability.
  - Use lowercase for table and column names.
  
**Quotes**:
  - Use double quotes for SQL identifiers (table and column names).
  - Use single quotes for string values.
### Example of LIKE with Wildcards
```sql
SELECT "title" 
FROM "longlist" 
WHERE "title" LIKE 'P_re';
```