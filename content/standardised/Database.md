---
title: 
tags:
  - database
aliases: 
category:
---
Databases are used for managing large amounts of data with **scalability**, **speed**, and **flexibility**. Through systems like
- [[MySql]], 
- [[PostgresSQL]], and 
- [[MongoDB]], 

databases enable efficient **[[CRUD]]** operations and handle **transactional processing** ([[OLTP]]). The **[[Database Schema|schema]]** provides the structural foundation that organizes data into tables and relationships, ensuring it can evolve with the system's needs.
### What is a Database?

A **database** is a [[structured data]]rganized to support operations such as **creation**, **reading**, **updating**, and **deleting** (commonly referred to as [[CRUD]] operations). It is designed to manage large volumes of data, often in a way that ensures efficient and reliable access.

### Relational Databases

Utilize structured query language ([[SQL]]) to manage data in tables, where relationships can be expressed through foreign keys and joins, often modelled using set theory. Relational databases are more efficient due to having less redundancy 
### Key Aspects of Databases:

**Definition**:  
   A database, especially a **relational database**, captures and stores data through **online transactional processing** (also referred to as ==[[OLTP]]==).

 **Structure**:  
   Databases organize data into **tables** (similar to spreadsheets), with each table having **columns** (fields) and **rows** (records). This structured format allows for efficient data storage, retrieval, and querying.

 **Flexibility**:  
   Databases come with a **flexible schema**, meaning the structure of the data (i.e., the layout of tables and columns) can be adjusted as the requirements evolve. This makes databases adaptable to changes, unlike static data storage solutions like spreadsheets.

**Use Case**:  
   Databases are primarily used for **transaction recording** and **managing live data** in applications. They are optimized for many small, quick transactions. However, databases can become slower when performing large or complex [[Querying]], especially on huge datasets, which may require other solutions like **data warehouses**.

Related Ideas:
- [[Spreadsheets to Databases]]
- [[Database Management System (DBMS)]]
- [[Components of the database]]
- [[Relating Tables Together]]
- [[Using SQLite to Process and Split Combined Data from Excel]]

Database Techniques:
- [[Soft Deletion]]