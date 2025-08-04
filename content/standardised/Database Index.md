---
aliases: [Index, Indexing]
category: DE
date modified: 1-08-2025
tags: [database, optimisation]
---
In [[DE_Tools]] see: 
- https://github.com/rhyslwells/DE_Tools/blob/main/Explorations/SQLite/Indexing/Indexing.ipynb

Related terms:
- [[Covering Index]]
- Partial Index (Index with where clause)

Indexing is a technique used to ==speed up data retrieval== in [[database]]. It achieves this by creating a separate structure, known as an index, that organizes specific columns of data for faster access. Better than scanning.

Commonly created on ==primary keys== (unique for item) and foreign keys.

Indexes can also be created across multiple tables to enhance the performance of complex queries, especially those that involve joins. A special type of index, called a ==covering index==, includes all the necessary data within the index itself, further improving efficiency.

Example:  
For instance, creating an index on the "title" column in the "movies" table can significantly reduce the time it takes to execute [[Querying|queries]] that search for movie titles.

## Using Indexes

Keep in mind that indexes consume additional storage space.

Creating Indexes: To improve search performance, create indexes on relevant columns. For example:
  ```sql
  CREATE INDEX idx_title ON movies(title);
  ```

Analyzing Queries: Use the `EXPLAIN QUERY PLAN` command to check if a query is utilizing an index effectively.

Dropping Indexes: If an index is no longer needed, it can be removed using:
  ```sql
  DROP INDEX idx_title;
  ```

## Space and Time Trade-offs

Space: Indexes require extra storage because they are built using B-Trees, which are hierarchical data structures.
Time: While indexes speed up data retrieval, creating and updating them can slow down data insertion and modification processes.

## How Indexes Work

- Data Structure: Indexes typically use a [[B-tree]] data structure, which allows for efficient searching.
- Node Structure: A B-tree organizes data into nodes, where each node contains links to the corresponding rows in the table. The data is sorted, enabling quick access.
- Search Mechanism: When searching, a binary search method is employed. This involves checking the middle of the data and deciding which side to search next, taking advantage of the ordered nature of B-trees for efficiency.
