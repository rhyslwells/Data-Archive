---
title: 
tags:
  - database
aliases: 
category:
---
# Summary

Databases are powerful tools for managing large amounts of data with **scalability**, **speed**, and **flexibility**. Through systems like [[MySql]], [[PostgresSQL]], and [[MongoDB]], databases enable efficient **[[CRUD]]** operations and handle **transactional processing** ([[OLTP]]). The **[[database schema|schema]]** provides the structural foundation that organizes data into tables and relationships, ensuring it can evolve with the system's needs.
### What is a Database?

A **database** is a [[structured data]]rganized to support operations such as **creation**, **reading**, **updating**, and **deleting** (commonly referred to as [[CRUD]] operations). It is designed to manage large volumes of data, often in a way that ensures efficient and reliable access.

### Key Aspects of Databases:

1. **Definition**:  
   A database, especially a **relational database**, captures and stores data through **online transactional processing** (also referred to as ==[[OLTP]]==). OLTP systems are designed to handle a large number of short online transactions (insert, update, delete).

2. **Structure**:  
   Databases organize data into **tables** (similar to spreadsheets), with each table having **columns** (fields) and **rows** (records). This structured format allows for efficient data storage, retrieval, and querying.

3. **Flexibility**:  
   Databases come with a **flexible schema**, meaning the structure of the data (i.e., the layout of tables and columns) can be adjusted as the requirements evolve. This makes databases adaptable to changes, unlike static data storage solutions like spreadsheets.

4. **Use Case**:  
   Databases are primarily used for **transaction recording** and **managing live data** in applications. They are optimized for many small, quick transactions. However, databases can become slower when performing large or complex [[Querying]], especially on huge datasets, which may require other solutions like **data warehouses**.

### Why Use Databases Instead of Spreadsheets?

- **Scale**: Databases can handle a vast amount of data more efficiently than spreadsheets.
- **Frequency**: Databases allow for real-time updates and continuous operations, unlike spreadsheets, which are more static.
- **Speed**: Databases are optimized for quick access, retrieval, and manipulation of data, especially with frequent and concurrent users.
### What is a Database Management System (DBMS)?

A **Database Management System** (DBMS) is software that allows you to interact with and manage databases. Popular DBMS platforms include:
- [[MySql]]
- [[PostgresSQL]]
- [[MongoDB]]

These systems enable users to perform [[CRUD]] operations while maintaining data integrity and providing tools for backup, security, and optimization.

[[Database]]
[[Fact table]] in main table that [[Dimension table]] connect to.

![[Obsidian_CSP0FnAVD1.png]]