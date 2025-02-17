---
tags:
  - database
---
 [[Querying]] can be optimised for time, ==space efficiency==, and concurrency of queries.
 
Optimizing SQL [[Querying]]:
- Timing queries
- [[Database Index|Indexing]]
- Managing [[Transaction]]
- and vacuuming, and handling concurrency with transactions and locks ensures efficient and reliable database performance.

### Timing [[Queries]]:

- Use `.timer on` to measure query execution time and identify slow queries.

### [[Database Index|Index]] Search

Creating an index on specific columns can speed up searches:
- A covering index includes all the columns required by a query, eliminating the need to access the table data.
- Partial indexes cover a subset of rows, saving space while maintaining query performance for frequently accessed data i.e more likely to search movies that are recent.

Trade-offs when using indexes
- Indexes improve query speed but ==consume additional space== and can slow down data insertion and updates.

### To remove redundancy use [[Transaction|Transactions]]

### Vacuum

SQLite's "VACUUM" command reclaims unused space after data deletion, reducing database size.