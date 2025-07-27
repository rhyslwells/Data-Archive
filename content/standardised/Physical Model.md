---
aliases: []
category:
date modified: 27-07-2025
tags: []
---
Physical Model

(for a SQL database):
   ```sql
   CREATE TABLE Customer (
       CustomerID INT PRIMARY KEY,
       Name VARCHAR(100),
       Email VARCHAR(100)
   );

   CREATE TABLE Order (
       OrderID INT PRIMARY KEY,
       OrderDate DATE,
       CustomerID INT,
       FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
   );

   CREATE TABLE Book (
       BookID INT PRIMARY KEY,
       Title VARCHAR(100),
       Author VARCHAR(100)
   );

   CREATE TABLE OrderBook (
       OrderID INT,
       BookID INT,
       PRIMARY KEY (OrderID, BookID),
       FOREIGN KEY (OrderID) REFERENCES Order(OrderID),
       FOREIGN KEY (BookID) REFERENCES Book(BookID)
   );
   ```



Physical Model
   - Implements the logical model in a specific database system.
   - Includes table structures, columns, data types, and constraints.