---
tags: 
category: 
aliases:
  - GQL
---

GQL is an emerging ISO standard for querying graph databases.

Not yet fully finalized, but intended to unify concepts from:
  - [[Neo4j]] [[Cypher]]
  - SQL/PGQL

==Think of GQL as a future "standard [[SQL]]" for graphs.==

Tutorial Lesson 1: [GraphQL Crash Course #1 - What is GraphQL?](https://www.youtube.com/watch?v=xMCnDesBggM)

Alternative to using a [[REST API]].

[[REST API]]
- GET or POST to endpoints, many endpoints
- Server interacts with a database using CRUD
- drawbacks at scale and complexity
	- Overfetching of data: GraphQL get specific
	- Underfetching, need to go to many different places.

GraphQL:
- request goes to a single endpoint
- There is a querying format for this request.
- Dont need many queries.
- Mutations similar to CRUD.