---
aliases:
- null
category: DE
date modified: 27-09-2025
tags:
- database
---
A foreign key is a field in one table that uniquely identifies a row in another table, linking to the primary key of that table.

For example, `DepartmentID` in the ==Employees== table links to `DepartmentID` in the ==Departments== table.  

Foreign keys establish relationships between tables and ==maintain **referential integrity** by ensuring valid connections between records.==  
This means:
- You cannot insert a `DepartmentID` in the Employees table unless it already exists in the Departments table.  
- You cannot delete a department from the Departments table if employees are still assigned to it (unless cascading rules are defined).  
- This ==prevents orphaned records== and enforces consistency across related tables.  
### Example

**Departments Table**

| DepartmentID | DepartmentName   |
|--------------|------------------|
| 1            | Human Resources  |
| 2            | IT               |
| 3            | Marketing        |

**Employees Table**

| EmployeeID | EmployeeName | DepartmentID |
|------------|--------------|--------------|
| 101        | Alice        | 1            |
| 102        | Bob          | 2            |
| 103        | Charlie      | 1            |
| 104        | Dana         | 3            |
