---
aliases: []
category: 
date modified: 1-08-2025
tags: [graph, querying]
---
Cypher is a graph query language designed to be:

- Declarative: you say *what* you want, not *how* to get it.
- Pattern-based: you express queries as graph patterns.
- Human-readable

Related to:
- [[neo4j]]
- [[Querying]]
- [[APOC Procedures]]
- [[Indexing in cypher]]

## Core Components

| Concept         | Syntax                  | Example                          |
|-----------------|--------------------------|----------------------------------|
| Node        | `(n)`                    | `(n:Person)`                     |
| Relationship| `-[r:TYPE]->`             | `-[:FRIENDS_WITH]->(friend)`      |
| Property    | `{key: value}`            | `{name: 'Alice'}`                |
| Labels      | `:Label`                  | `:Person`                        |
| Alias       | `variable` names          | `alice`, `friend`, etc.           |

## Common Keywords

| Keyword   | Purpose                      | Example                               |
|-----------|-------------------------------|---------------------------------------|
| `MATCH`   | Find pattern                  | `MATCH (n:Person)`                    |
| `WHERE`   | Add condition                 | `WHERE n.age > 30`                    |
| `RETURN`  | Output results                | `RETURN n.name`                       |
| `CREATE`  | Insert nodes/relationships    | `CREATE (n:Person {name: 'Bob'})`      |
| `MERGE`   | Create if not exists           | `MERGE (n:Person {name: 'Charlie'})`   |
| `SET`     | Update properties             | `SET n.age = 40`                      |
| `DELETE`  | Remove nodes/relationships    | `DELETE n`                            |

## Example 1: Find Alice’s Friends

```cypher
MATCH (alice:Person {name: 'Alice'})-[:FRIENDS_WITH]->(friend)
RETURN friend.name
```

- `MATCH`: pattern starts with `alice` node.
- `-[:FRIENDS_WITH]->(friend)`: outgoing relationship to `friend`.
- `RETURN`: names of friends.

## Example 2: Create a New Person Node

```cypher
CREATE (p:Person {name: 'David', age: 29})
```

- `CREATE`: create node `p`.
- `:Person`: label.
- Properties: `name`, `age`.

## Example 3: Connect Two People

```cypher
MATCH (alice:Person {name: 'Alice'}), (bob:Person {name: 'Bob'})
CREATE (alice)-[:FRIENDS_WITH]->(bob)
```

- Find both `alice` and `bob`.
- Create a `FRIENDS_WITH` relationship from Alice to Bob.

## Example 4: Conditional Query

```cypher
MATCH (p:Person)
WHERE p.age > 30
RETURN p.name, p.age
```

- Find all `Person` nodes with `age > 30`.
- Return their `name` and `age`.

## Example 5: Shortest Path

```cypher
MATCH path = shortestPath((a:Person {name: 'Alice'})-[:FRIENDS_WITH*]-(b:Person {name: 'Charlie'}))
RETURN path
```

- Find the shortest path between Alice and Charlie.
- `*` means any number of `FRIENDS_WITH` hops (edges).

# Tips for Writing Cypher

- Use Aliases: `(a:Person)` makes later referencing (`a.name`) easier.
- Direction Matters: `-[:TYPE]->` vs `<-[:TYPE]-`.
- Wildcard Relationships: `-[:TYPE*1..3]->` allows 1 to 3 hops.
- Optional Matches: `OPTIONAL MATCH` to avoid dropping records if some parts are missing.


Excellent — let's go through these topics carefully and systematically, with simple examples and clear breakdowns.  

---

# 1. Aggregations in Cypher (#cypher)

In Cypher, you can aggregate data much like SQL — examples include `COUNT()`, `AVG()`, `SUM()`, `MIN()`, `MAX()`.

## Basic Syntax

| Function | Purpose                      | Example                        |
|----------|-------------------------------|--------------------------------|
| `COUNT()`| Count records                 | `COUNT(p)`                     |
| `AVG()`  | Average a numeric field       | `AVG(p.age)`                   |
| `SUM()`  | Sum numeric fields            | `SUM(p.age)`                   |
| `MIN()`  | Find minimum                  | `MIN(p.age)`                   |
| `MAX()`  | Find maximum                  | `MAX(p.age)`                   |

---

## Example: Count number of people

```cypher
MATCH (p:Person)
RETURN COUNT(p) AS number_of_people
```

- `MATCH` all nodes with label `Person`.
- `COUNT(p)` counts how many nodes.

---

## Example: Average age of friends

```cypher
MATCH (:Person {name: 'Alice'})-[:FRIENDS_WITH]->(friend)
RETURN AVG(friend.age) AS avg_friend_age
```

- Find Alice’s friends.
- Compute their average age.

---

# 2. Returning Paths and Subgraphs (#cypher)

In Neo4j, you can return not only *nodes* but entire *paths*.

## Path Syntax

```cypher
MATCH path = (a:Person {name: 'Alice'})-[:FRIENDS_WITH*]->(b:Person)
RETURN path
```

- `path = (...)` captures the whole path (nodes + relationships).

## Visualizing

In Neo4j Browser or Bloom, returning a `path` shows an actual graph visualization, not just rows.

---

## Example: Return all paths of up to 2 hops

```cypher
MATCH path = (a:Person)-[:FRIENDS_WITH*1..2]->(b:Person)
RETURN path
```

- `*1..2` means 1 to 2 relationships deep.

---

# 3. `CREATE` vs `MERGE` (#cypher)

This is very important to understand:

| Action | Meaning | Key Behavior |
|--------|---------|--------------|
| `CREATE` | Always create a new node or relationship. | No checking if it already exists. |
| `MERGE`  | Search first, create only if not found.   | Like SQL `INSERT OR IGNORE`. |

---

## Example: CREATE

```cypher
CREATE (p:Person {name: 'Alice'})
```
- Every time you run it, a new node will be created.

If you run it 5 times, you get 5 nodes!

---

## Example: MERGE

```cypher
MERGE (p:Person {name: 'Alice'})
```
- If a `Person` with `name: 'Alice'` already exists, no new node is created.
- If none exists, a new node is created.

---

## Important Note

- `MERGE` matches the entire pattern: both labels and properties.
- If only partial matching is done, it may create *extra* unwanted nodes.

Tip: Be careful when using `MERGE` with relationships — you often have to `MATCH` the nodes first, then `MERGE` the relationship separately.

Example:

```cypher
MATCH (a:Person {name: 'Alice'}), (b:Person {name: 'Bob'})
MERGE (a)-[:FRIENDS_WITH]->(b)
```

---



