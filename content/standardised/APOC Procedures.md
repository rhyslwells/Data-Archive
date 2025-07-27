---
aliases: []
category:
date modified: 27-07-2025
tags: [data_integration, graph]
---
APOC (Awesome Procedures On Cypher) is a collection of advanced utilities and procedures that extend Neo4j's functionality. APOC is a powerful library, with features that cover:

- Graph algorithms
- Data integration
- Query optimization
- Import/export functionality
- Advanced graph traversal

### How to Use APOC

APOC is often already installed in Neo4j (in the standard distribution). To use APOC procedures, you simply call them within your Cypher queries.

---

### Common APOC Procedures

| Procedure | Purpose | Example |
|-----------|---------|---------|
| `apoc.coll.flatten` | Flattens a nested collection | `RETURN apoc.coll.flatten([[1, 2], [3, 4]])` |
| `apoc.graph.fromGraphML` | Import data from GraphML format | `CALL apoc.graph.fromGraphML('file:///data.graphml')` |
| `apoc.load.json` | Load JSON data from a URL or file | `CALL apoc.load.json('https://api.example.com/data') YIELD value` |
| `apoc.create.node` | Create a node with properties | `CALL apoc.create.node(['Person'], {name: 'Alice', age: 25})` |
| `apoc.util.validate` | Validate conditions in queries | `CALL apoc.util.validate(p.age < 30, 'Age too high', [p]) YIELD value` |



### Example: Flatten a Collection

```cypher
RETURN apoc.coll.flatten([[1, 2, 3], [4, 5], [6]]) AS flattened
```

- This will flatten the list of lists into a single list: `[1, 2, 3, 4, 5, 6]`.



### Example: Load External JSON Data

```cypher
CALL apoc.load.json('https://api.example.com/users') YIELD value
RETURN value.name, value.email
```

- This loads JSON data from an external URL, and you can directly work with it in your Cypher query.



### Example: Create Nodes Dynamically

```cypher
CALL apoc.create.node(['Person'], {name: 'John', age: 30}) YIELD node
RETURN node
```

- This creates a node with a dynamic label and properties.



### Example: Graph Algorithm (Shortest Path)

APOC also includes many graph algorithms. For example, you can find the shortest path between two nodes using `apoc.algo.shortestPath`:

```cypher
MATCH (a:Person {name: 'Alice'}), (b:Person {name: 'Bob'})
CALL apoc.algo.shortestPath(a, b, 'FRIENDS_WITH') YIELD path
RETURN path
```

- This returns the shortest path between Alice and Bob through the `FRIENDS_WITH` relationship.



### Example: Convert Data to GraphML

```cypher
CALL apoc.graph.fromGraphML('file:///example.graphml') YIELD nodes, relationships
RETURN nodes, relationships
```

- This procedure imports a GraphML file and converts it to a graph format that Neo4j can use.



### Why APOC is Powerful

- Data Integration: Integrate data from external sources like JSON, CSV, or GraphML.
- Advanced Graph Algorithms: Run graph algorithms like centrality, community detection, and pathfinding.
- Utility Functions: Enhance queries with functions like flattening collections, validating conditions, or generating random data.
- Batch Operations: Many APOC procedures support batch processing of large datasets, improving performance.



### Getting Started with APOC

1. Check if APOC is installed:
   You can check if APOC is installed by running a simple query:

   ```cypher
   RETURN apoc.version()
   ```

   This will return the APOC version if it's available.

2. Install/enable APOC:
   If APOC isn't installed, it can typically be added by modifying the `conf` file (`neo4j.conf`), setting:
   ```plaintext
   dbms.security.procedures.unrestricted=apoc.*
   ```

3. Refer to the APOC documentation:
   For more information, the official [APOC documentation](https://neo4j.com/labs/apoc/4.0/) is extensive and lists all available procedures and functions.



# Summary of Key Concepts

| Topic | Key Idea | Example |
|-------|----------|---------|
| Query Tuning | Use `EXPLAIN` (estimates plan) and `PROFILE` (actual stats) | `EXPLAIN MATCH (a:Person)-[:FRIENDS_WITH]->(b:Person)` |
| APOC Procedures | Advanced utilities for Cypher queries | `CALL apoc.load.json('URL') YIELD value` |