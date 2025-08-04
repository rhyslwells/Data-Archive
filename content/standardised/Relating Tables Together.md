---
aliases: []
category:
date modified: 1-08-2025
tags: [database]
---
Implementing these concepts, database tables can be effectively related, ensuring [[Data Integrity]], efficient retrieval, and easy maintenance.

Resources:
- [LINK](https://cs50.harvard.edu/sql/2024/weeks/1/)
### Notes on Relating Database Tables

[[Primary Key]]

[[Foreign Key]]

One-to-One Relationships:
   - Each record in Table A relates to one record in Table B and vice versa.
   - Example: Each employee has one unique profile.

One-to-Many Relationships:
   - A single record in Table A can relate to multiple records in Table B.
   - Example: One department has many employees.

[[Many-to-Many Relationships]]

[[Junction Tables]]
   - Used to manage many-to-many relationships.
   - Contains foreign keys from both tables it connects.
   - Example: Enrollments table with StudentID and CourseID as foreign keys.

Referential Integrity
   - Ensures that relationships between tables remain consistent.
   - Example: If an employee is assigned a department, the DepartmentID must exist in the Departments table.

Cascading Actions:
   - Cascade Update: Updates related records automatically when a primary key is updated.
   - Cascade Delete: Deletes related records automatically when a primary key is deleted.

[[ER Diagrams]]
