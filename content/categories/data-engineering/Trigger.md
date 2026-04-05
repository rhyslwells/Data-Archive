---
aliases: []
category: DE
date modified: 7-01-2026
tags:
  - database
---
In SQLite, a **trigger** is a database-level mechanism that **executes SQL logic automatically when a specific data event occurs** on a table.

A trigger **automates enforcement or side effects tied to data changes**. 
## What a trigger does

A trigger defines:

* **When** it fires
  `BEFORE` or `AFTER` an event

* **What event**
  `INSERT`, `UPDATE`, or `DELETE`

* **Which table**
  The table the event applies to

When the event occurs, SQLite runs the trigger’s SQL body as part of the same transaction.

## Typical purposes

### 1. Enforcing data rules

Ensure invariants that SQLite does not enforce natively.

Example: prevent empty names

```sql
CREATE TRIGGER validate_artist_name
BEFORE INSERT ON artists
FOR EACH ROW
WHEN NEW.name IS NULL OR NEW.name = ''
BEGIN
  SELECT RAISE(ABORT, 'Artist name is required');
END;
```

### 2. Maintaining derived data

Keep denormalised or computed fields consistent.

Example: maintain a count table

```sql
CREATE TRIGGER artist_insert_count
AFTER INSERT ON artists
BEGIN
  UPDATE stats
  SET artist_count = artist_count + 1;
END;
```

### 3. Auditing and history

Record changes automatically.

Example:

```sql
CREATE TRIGGER log_artist_update
AFTER UPDATE ON artists
BEGIN
  INSERT INTO artist_log(artist_id, changed_at)
  VALUES (NEW.id, CURRENT_TIMESTAMP);
END;
```

### 4. Cascading changes

Apply side effects across tables.

Example:

```sql
CREATE TRIGGER delete_artist_cleanup
AFTER DELETE ON artists
BEGIN
  DELETE FROM albums WHERE artist_id = OLD.id;
END;
```
## Key properties (important in your context)

* Triggers are **implicit**: application code does not call them.
* They execute **inside the same transaction** as the triggering statement.
* If a trigger fails, the original operation fails.
* Multiple triggers can fire for the same event, in creation order.

## How this differs from application logic

Triggers are appropriate when:

* The rule must hold regardless of which client modifies the database
* You want the database to protect its own consistency

They become problematic when:

* Logic is complex or opaque
* Side effects are surprising to users or tools
* Debugging needs to happen outside the database