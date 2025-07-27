---
aliases: []
category:
date modified: 27-07-2025
tags: [optimisation]
---
On large graphs, performance becomes critical. Neo4j supports [[Database Index|Index]] and tuning.

## When to Use Indexes

- You often `MATCH` nodes by a property (e.g., `name`, `id`).
- These searches benefit greatly from an index.
## How to Create an Index

```cypher
CREATE INDEX person_name_index IF NOT EXISTS
FOR (p:Person)
ON (p.name)
```

- Creates an index on the `name` property for `Person` nodes.
- `IF NOT EXISTS` avoids errors if the index already exists.
## Types of Indexes

| Type | Use Case | Example |
|------|----------|---------|
| Property Index | Speed up lookups by property | `CREATE INDEX FOR (p:Person) ON (p.name)` |
| Composite Index | Search by multiple properties | `CREATE INDEX FOR (p:Person) ON (p.name, p.age)` |
| Full-text Index | Search unstructured text fields | More advanced setup |

## Performance Tips

- Always MATCH on indexed properties for faster queries.
- Avoid Cartesian Products: if you forget to connect nodes in `MATCH`, Neo4j will combine everything (`n * m`) — extremely slow!
- Limit the depth when matching variable-length paths (`*1..3`) to avoid exploring the entire graph.

Example of a bad Cartesian product:

```cypher
MATCH (a:Person), (b:Person) 
RETURN a, b
```

(no relationship specified between `a` and `b`!)