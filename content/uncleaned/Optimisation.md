---
tags:
  - SQL
---


**Introduction:**
This lecture covers [[SQL]] query [[Querying]] optimization for ==time== (of queries) 
and ==space efficiency==, and how to run concurrent queries.

**Timing Queries:**

- Use `.timer on` to measure query execution time and identify slow queries.

**Search Strategies:**

- Linear [[Search]]: Scans one row at a time. Inefficient for unsorted data.
- Index Search: Uses an index to quickly locate data. Creating an index on specific columns can speed up searches.

**Using Indexes:**

- Create indexes on relevant columns to improve search performance. For example, `CREATE INDEX idx_title ON movies(title);`.
- Use the `EXPLAIN QUERY PLAN` command to determine if a query uses an index.
- Drop indexes with `DROP INDEX` if no longer needed, but be aware that indexes consume space.

**Covering Indexes:**

- A covering index includes all the columns required by a query, eliminating the need to access the table data.

**Trade-offs:**

- Indexes improve query speed but consume additional space and can slow down data insertion and updates.
- Use partial indexes to index only a subset of rows, saving space. For instance, indexing only recent movies.

[[B-tree]]
- Indexes use a B-tree data structure, which allows for efficient searching.
- A B-tree breaks copied data into nodes, using the ordering of column data to structure the tree.
- Nodes contain row data and linkages to the table location.
- The index copies column data, sorts it, and uses linkages to efficiently retrieve the original table data.

**[[Binary Search]]:**
- Binary search looks in the middle of the data and then chooses which side to search next. This method is effective due to the ordered nature of B-trees.

optimising the space used: partial index: includes only a subset of the data used: i.e more likely to search movies that are recent.

**[[Indexing]]:**
- **Concept:** Indexing speeds up data retrieval by creating a separate structure (index) that organizes selected columns.
- **Example:** Creating an index on the "title" column in the "movies" table significantly reduces query time.
- **Multiple Tables:** Indexes can be created on multiple tables to speed up complex queries involving joins. Covering indexes include all necessary data within the index itself.

**Space and Time Trade-offs:**
- **Space:** Indexes consume additional space as they are stored using B-Trees, which are hierarchical data structures.
- **Time:** Creating and updating indexes can increase the time required for data insertion and modification.

**Partial Index:**
- Partial indexes cover a subset of rows, saving space while maintaining query performance for frequently accessed data (e.g., recent movies).

**Vacuum:**
- SQLite's "VACUUM" command reclaims unused space after data deletion, reducing database size.

**Concurrency and ==Transactions==:**
- **Concurrency:** Allows multiple queries to run simultaneously, essential for high-traffic applications.
- **Transactions:** Ensure atomicity, consistency, isolation, and durability (==ACID== properties). Transactions can be committed to save changes or rolled back to revert to the previous state.
- **Race Conditions:** Occur when concurrent transactions access and modify shared data, potentially leading to inconsistencies. Transactions and locking mechanisms prevent these issues by ensuring sequential execution.

[[ACID Transaction]]
- Atomicity: can be broken down: dont see middle parts.
- Consistency: dones invalid a constraint: otherwise goes back to stable state.
- Isolation: muliple queries wont interfere with database
- Durability: data will still be there.

[[TRANSACTION]] call
Combines middles steps so others dont see it. its a bundle of calls.

ROLLBACK (previous statments if error) only when in transaction

RACE CONDITIONS due to ==concurrent== transactions occuring at different stages. To solve want to ISOLATE transactions - use LOCK.

**Locks:**
- UNLOCK (anyone can add/read), SHARED (can read/allow others in),LOCKED (to write/ get exclusive lock/ to ensure sequential privileges)
- **Types:** Shared locks for read operations, ==exclusive locks== for write operations.
- **Granularity:** SQLite locks the entire database during exclusive transactions, though finer ==granularity== (e.g., row-level locks) is possible in other DBMS (database management system).

Use ==timestamping== to allow access to exclusive locks.

**Conclusion:**
Optimizing SQL queries through indexing, managing trade-offs, using partial indexes, maintaining database health with vacuuming, and handling concurrency with transactions and locks ensures efficient and reliable database performance.