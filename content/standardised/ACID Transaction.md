---
aliases: []
category:
date modified: 1-08-2025
tags: [database, storage]
---
An ACID [[Transaction]] ensures that either all changes are successfully committed or rolled back, preventing the database from ending up in an inconsistent state. This guarantees the integrity of the data throughout the transaction process.

### Key Properties of ACID Transactions

1. Atomicity: This property ensures that transactions are treated as a single, indivisible unit. If any part of the transaction fails, the entire transaction is rolled back, and none of the changes are applied. Users do not see intermediate states of the transaction.

2. Consistency: Transactions must leave the database in a valid state, adhering to all defined constraints. If a transaction violates a constraint, it is rolled back to maintain the database's stable state.

3. Isolation: This property ensures that concurrent transactions do not interfere with each other. Each transaction operates independently, and the results of one transaction are not visible to others until it is committed.

4. Durability: Once a transaction has been committed, the changes are permanent, even in the event of a system failure. The data remains intact and recoverable.

