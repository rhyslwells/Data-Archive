---
tags: 
aliases:
  - Transactions
category: 
phase: 
topic: 
filename:
---
Transactions are used for maintaining [[Data Integrity]] and should adhere to the [[ACID Transaction]].

## Transaction Operations

- Commit: Saves all changes made during the transaction.
- Rollback: Reverts the database to its previous state if an error occurs during the transaction.

## Concurrency and Transactions

- Concurrency: Allows multiple [[Querying]] to run simultaneously, essential for high-traffic applications.
- Race Conditions: Occur when concurrent transactions access and modify shared data, potentially causing inconsistencies.

## Transaction Locks

To prevent ==race conditions,== transactions and locking mechanisms are employed to ensure that operations occur sequentially. Locks manage access to the database during [[Transaction|Transactions]]:

- UNLOCK: Allows anyone to read or add data.
- SHARED: Permits reading while allowing others to access the data.
- LOCKED: Grants exclusive write access to ensure that no other transactions can interfere.

### Types of Locks
- Shared Locks: Used for read operations.
- Exclusive Locks: Used for write operations.

### [[Granularity]] of Locks

[[SQLite]] locks the entire database during exclusive transactions. While finer granularity (e.g., row-level locks) is possible in other database management systems ([[Database Management System (DBMS)|DBMS]]), SQLite's approach is simpler but can lead to contention in high-concurrency scenarios.

### Timestamping
Using timestamping can help manage access to exclusive locks, allowing for more efficient handling of concurrent transactions ([[Concurrency]]).
