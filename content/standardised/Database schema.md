---
title: 
tags:
  - drafting
  - database
aliases:
  - schema
category:
---
### Overview
#### Resources
[link](https://www.youtube.com/watch?v=3BZz8R7mqu0)

#### Summary
Database schema are used in [[Data Management]]. Here are the main takeaways:

1. **Definition and Components**: A database schema represents the ==structure== around the data, including tables, views, fields, relationships, and various other elements like indexes and triggers. It provides a framework for organizing and understanding data.

2. **Importance of ==Structure==**: Without a schema, data can be chaotic and difficult to ==interpret==. A well-defined schema organizes data, making it ==manageable and meaningful.==

3. **Schema on Read vs. Schema on Write**: 
   - **Schema on Read**: Structure is applied when the data is read, useful for unstructured data stores.
   - **Schema on Write**: Structure is enforced when data is written, typical of traditional databases.

4. **Design Influences**: The design of a schema impacts database behavior. For example, schemas designed with tables connected by primary keys are optimized for transactional applications, while star schemas are designed for efficient read operations in data warehouses.

5. **Performance Impact**: A good schema can significantly ==improve query performance==, reducing processing ==time== and ==cost==, and simplifying query complexity.

6. [[Data Modelling]]Despite being considered an old concept, data modeling remains crucial for creating effective schemas, particularly in the context of big data and analytics.

7. **Iterative Process**: Developing a data warehouse schema involves iterative refinement, starting with interviews to create a conceptual data model, which is then tested and refined through multiple iterations before being implemented.

8. **Strategic Importance**: The strategic design and deployment of a database schema are vital for efficient data warehousing and analytics. Intricity specializes in this process, helping organizations define and execute their data strategies.

[[SQL]]

Definition: Schema, tables with relations between 

### Introduction to Database Schema
- **Purpose**: Learn to design database schemas.
- **Example**: Database of books longlisted for the International Booker Prize.

To find commands used to create a database use 
```.schema```

or
.schema table

to run a schema use: in sqlite
.read schema.sql

---

### Creating a Database Schema
- **Steps**:
  1. Decide the tables for the Boston Subway system.
  2. Define columns for each table.
  3. Choose data types for each column.
- **Example**:
  ```sql
  CREATE TABLE stations (
      "id" INTEGER,
      "name" TEXT,
      "line" TEXT
  );
  ```

many to many relationships. What tables needed
one for each entity. To implement the relationship have another table.
I.e. People, incidents. Then crew_on_board (person_id,incident_id)

### [[Normalisation of data]] (first,second,.. normal forms)
- **Purpose**: Reduce data ==redundancy== by separating entities into different tables.
![[Pasted image 20240524193844.png|500]]
- **Example**:
  ```sql
  CREATE TABLE riders (
      "id" INTEGER,
      "name" TEXT
  );
  ```
- To make it easier to write queries about.

---

### Relating ==Entities==
- **Purpose**: Define ==relationships== between entities using foreign keys.
- **Example**:
  ```sql
  CREATE TABLE visits (
      "rider_id" INTEGER,
      "station_id" INTEGER,
      FOREIGN KEY("rider_id") REFERENCES "riders"("id"),
      FOREIGN KEY("station_id") REFERENCES "stations"("id")
  );
  ```

---

### Data Types and Storage Classes
- **Types**:
  - Null
  - Integer
  - Real
  - Text
  - Blob
- **Example**:
  ```sql
  CREATE TABLE fares (
      "id" INTEGER,
      "amount" REAL
  );
  ```

---

### Type Affinities
- **Definition**: ==Columns== try to convert values to their affinity type (convert to text,int,ect).
- **Example**:
  ```sql
  CREATE TABLE example (
      "value" INTEGER
  );
  -- Inserting text "25" converts to integer 25
  ```

---

### Table Constraints
- **Constraints**:
  - PRIMARY KEY
  - FOREIGN KEY
- **Example**:
  ```sql
  CREATE TABLE stations (
      "id" INTEGER PRIMARY KEY,
      "name" TEXT UNIQUE NOT NULL
  );
  ```

---

### Column ==Constraints==

values have to be a given way. 

dont need to apply to primary and foreign keys

Primary and foreign keys
- **Constraints**:
  - CHECK (amount is greater than 0)
  - DEFAULT
  - NOT NULL
  - UNIQUE
- **Example**:
  ```sql
  CREATE TABLE swipes (
      "id" INTEGER,
      "type" TEXT NOT NULL CHECK("type" IN ('enter', 'exit', 'deposit')),
      "datetime" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP
  );
  ```

```sql
CREATE TABLE "riders"(
"id" INTEGER,
"name" TEXT,
PRIMARY KEY("id")
);
```

```sql
CREATE TABLE "visits"(
"rider_id" INTEGER,
"station_id" TEXT,
FOREIGN KEY("rider_id") REFERENCES "riders"("id")
);
```

Joint primary key constraint
row id is always created primary keys

---
### Altering Tables
- **Operations**:
  - RENAME
  - ADD COLUMN
  - DROP COLUMN
- **Example**:
  ```sql
  ALTER TABLE visits
  RENAME TO swipes;

  ALTER TABLE swipes
  ADD COLUMN "swipetype" TEXT;

  DROP TABLE "riders"; 
  ```


---

### Final Schema Example
- **Updated Schema**:
  ```sql
  CREATE TABLE cards (
      "id" INTEGER PRIMARY KEY
  );

  CREATE TABLE stations (
      "id" INTEGER PRIMARY KEY,
      "name" TEXT UNIQUE NOT NULL,
      "line" TEXT NOT NULL
  );

  CREATE TABLE swipes (
      "id" INTEGER PRIMARY KEY,
      "card_id" INTEGER,
      "station_id" INTEGER,
      "type" TEXT NOT NULL CHECK("type" IN ('enter', 'exit', 'deposit')),
      "datetime" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
      "amount" NUMERIC NOT NULL CHECK("amount" != 0),
      FOREIGN KEY("card_id") REFERENCES "cards"("id"),
      FOREIGN KEY("station_id") REFERENCES "stations"("id")
  );
  ```

A **[[database schema|schema]]** is the structure that defines how data is organized in a database. It specifies the tables, columns, relationships, and constraints within the database. The schema is crucial for ensuring data is stored consistently and can be queried efficiently.