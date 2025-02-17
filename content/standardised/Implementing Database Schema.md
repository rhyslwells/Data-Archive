To manage and create a database schema in SQLite, you can use the following commands:

- To view all commands used to create a database, execute:
  ```
  .schema
  ```
- To view the schema for a specific table, use:
  ```
  .schema table
  ```
- To run a schema from a file, use:
  ```
  .read schema.sql
  ```

## Creating a Database Schema

When creating a database schema, follow these steps:

1. **Identify the Tables**: Determine which tables are necessary for your data.
2. **Define Columns**: Specify the columns for each table.
3. **Choose Data Types**: Select appropriate data types for each column.
4. **Establish Keys**: Define primary and foreign keys to maintain data integrity.
5. **Set Column Constraints**: Ensure that values adhere to specified conditions.

Note that constraints do not need to apply to primary and foreign keys. Common constraints include:

- `CHECK`: Ensures values meet certain criteria (e.g., amount must be greater than 0).
- `DEFAULT`: Sets a default value for a column.
- `NOT NULL`: Ensures a column cannot have a NULL value.
- `UNIQUE`: Ensures all values in a column are distinct.

### Example Schema Creation

Here’s an example of how to create tables for a database:

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

## Modifying the Schema

To change an existing schema, you can use commands such as `RENAME`, `ADD COLUMN`, and `DROP COLUMN`. 

```sql
ALTER TABLE visits
RENAME TO swipes;

ALTER TABLE swipes
ADD COLUMN "swipetype" TEXT;

DROP TABLE "riders"; 
```

## Relating Entities

Done using foreign keys.

```sql
CREATE TABLE visits (
    "rider_id" INTEGER,
    "station_id" INTEGER,
    FOREIGN KEY("rider_id") REFERENCES "riders"("id"),
    FOREIGN KEY("station_id") REFERENCES "stations"("id")
);
```

Also See:
- [[Many-to-Many Relationships]]
- [[ER Diagrams]]