---
tags:
  - database
---


[LINK](https://cs50.harvard.edu/sql/2024/weeks/1/)

Why have relational databases: efficiency less redundancy 


==keys== e.g  book_id these are vectors (unique) for identifying.

Use keys for querying 

### Notes on Relating Database Tables

**1. Primary Keys:** How to identify rows ISBN for books
   - Unique identifier for each record in a table.
   - Example: EmployeeID in an Employees table.

**2. Foreign Keys:**
   - Column in one table that links to the primary key in another table.
   - Example: DepartmentID in Employees table linking to DepartmentID in Departments table.

**3. One-to-One Relationships:**
   - Each record in Table A relates to one record in Table B and vice versa.
   - Example: Each employee has one unique profile.

**4. One-to-Many Relationships:**
   - A single record in Table A can relate to multiple records in Table B.
   - Example: One department has many employees.

**5. Many-to-Many Relationships:**
   - Records in Table A relate to multiple records in Table B, and vice versa.
   - ==Requires a junction table== to manage the relationships.
   - Example: Students and Courses tables with a junction table Enrollments.

**6. [[Junction Tables]]:**
   - Used to manage many-to-many relationships.
   - Contains foreign keys from both tables it connects.
   - Example: Enrollments table with StudentID and CourseID as foreign keys.

**7. Referential Integrity:**
   - Ensures that relationships between tables remain consistent.
   - Example: If an employee is assigned a department, the DepartmentID must exist in the Departments table.

**8. Cascading Actions:**
   - Cascade Update: Updates related records automatically when a primary key is updated.
   - Cascade Delete: Deletes related records automatically when a primary key is deleted.

**9. Indexing:**
   - Improves the speed of data retrieval operations on a database table.
   - Commonly created on ==primary keys== (unique for item) and foreign keys.

**10. Normalization:**
   - Process of structuring a database to reduce redundancy and improve data integrity.
   - Common forms include 1NF, 2NF, 3NF, and BCNF.

**11. [[ER Diagrams]]:**
   - Visual representation of the database structure.
   - Shows tables, fields, primary keys, foreign keys, and ==relationships==.
- ![[Pasted image 20240523192220.png]]

By understanding and implementing these concepts, database tables can be effectively related, ensuring data integrity, efficient retrieval, and easy maintenance.