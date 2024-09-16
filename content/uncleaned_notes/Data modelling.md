---
tags:
  - design
---


Includes [[ER Diagrams]]

Defining structure of a database.

Google data modleing tools

Workflow of data modeling:
1. conceptual: [[ER Diagrams]], definitions, relationships (ER STUDIO,DbSchema)
2. Logical modeling, attributes of data
3. physical model: tech requirements, 

Types of modeling:
Relational
Object Oriented : state changes of objects: Robots of car factory robot
Entity: [[ER Diagrams]]
Network: Extension of hierarchical
Hierarchical: 


Data modeling is the process of creating a visual representation of a system's data and the relationships between different data elements. This helps in organizing and structuring the data so it can be efficiently managed and utilized.

Here's a simple breakdown:

1. **Conceptual Model**: This is the high-level overview that outlines what data is important and the relationships between different data entities (e.g., customer, order, product). It focuses on the business perspective without going into technical details.

2. **Logical Model**: This defines how the data should be organized, detailing the attributes of each data entity and the relationships between them. It does not depend on a specific database management system.

3. **Physical Model**: This is the implementation of the logical model in a specific database management system. It includes detailed specifications like table structures, columns, data types, and constraints.

### Example

Let's say you are modeling data for an online bookstore. Here’s how you might approach it:

1. **Conceptual Model**:
   - Entities: Customer, Order, Book
   - Relationships: Customers place Orders, Orders include Books

2. **Logical Model**:
   - Customer: CustomerID, Name, Email
   - Order: OrderID, OrderDate, CustomerID
   - Book: BookID, Title, Author
   - Order-Book Relationship: OrderID, BookID (indicating which books are in each order)

3. **Physical Model** (for a SQL database):
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

By following these steps, data modeling ensures that data is logically structured and organized, making it easier to store, retrieve, and manipulate in a database.