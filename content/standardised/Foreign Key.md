---
aliases: []
category:
date modified: 27-07-2025
tags: []
---
A foreign key is a field in one table that uniquely identifies a row in another table, linking to the primary key of that table.

For example, `DepartmentID` in the ==Employees== table links to `DepartmentID` in the Departments table. 

Foreign keys establish relationships between tables and maintain referential integrity by ensuring valid connections between records.

**Departments Table**

| DepartmentID | DepartmentName      |
|--------------|----------------------|
| 1            | Human Resources       |
| 2            | IT                   |
| 3            | Marketing            |

**Employees Table**

| EmployeeID | EmployeeName | DepartmentID |
|------------|--------------|---------------|
| 101        | Alice        | 1             |
| 102        | Bob          | 2             |
| 103        | Charlie      | 1             |
| 104        | Dana         | 3             |