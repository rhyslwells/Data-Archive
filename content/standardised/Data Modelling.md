---
tags:
  - data_modeling
---
Data modelling is the process of creating a visual representation of a system's data and the relationships between different data elements. This helps in organizing and structuring the data so it can be efficiently managed and utilized.

Data modelling ensures that data is logically structured and organized, making it easier to store, retrieve, and manipulate in a database.

### Workflow of Data Modeling

1. **Conceptual Model**: 
   - Focuses on high-level business requirements.
   - Defines important data entities and their relationships.
   - Tools: [[ER Diagrams]], ER Studio, DbSchema.

2. **Logical Model**: 
   - Details the attributes of each data entity.
   - Specifies relationships without depending on a specific database management system.

3. **Physical Model**: 
   - Implements the logical model in a specific database system.
   - Includes table structures, columns, data types, and constraints.

### Types of Modeling

- **Relational**: Organizes data into tables.
- **Object-Oriented**: Focuses on objects and their state changes, e.g., robots in a car factory.
- **Entity**: Uses [[ER Diagrams]] to represent data entities and relationships.
- **Network**: An extension of hierarchical models.
- **Hierarchical**: Organizes data in a tree-like structure.

### Example: Online Bookstore

1. **Conceptual Model**:
   - **Entities**: Customer, Order, Book
   - **Relationships**: Customers place Orders, Orders include Books

2. **Logical Model**:
   - **Customer**: CustomerID, Name, Email
   - **Order**: OrderID, OrderDate, CustomerID
   - **Book**: BookID, Title, Author
   - **Order-Book Relationship**: OrderID, BookID

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

