---
aliases:
- null
category: CS
date modified: 27-09-2025
tags:
- graph
- python
---
**Neomodel** is a Python library that provides an Object-Graph Mapping (OGM) layer for [[neo4j]], a [[GraphRAG|graph database]]. It allows you to interact with a Neo4j graph database using Python objects, making it easier to work with the data stored in a graph structure without manually writing raw Cypher [[Querying]]. Neomodel simplifies the process of creating and manipulating nodes and relationships in a graph while providing an object-oriented approach.

### Key Features:
- **Object-Graph Mapping (OGM)**: Neomodel maps Python classes to Neo4j nodes and relationships, abstracting away the complexity of interacting directly with the database.
- **[[Database Schema|Schema]]-based**: You define your data models using Python classes, and Neomodel automatically generates the corresponding graph structure in Neo4j.
- **Easy to use**: Neomodel provides a simple and intuitive [[API]] for creating, querying, and updating graph data.
- **Integrates with Neo4j**: Neomodel works seamlessly with the Neo4j graph database, allowing you to leverage its full capabilities while using Python.

### Installation:
To install Neomodel, you can use `pip`:
```bash
pip install neomodel
```

### Basic Example:

Here’s an example of how you can define models, create nodes, and query the database using Neomodel:

1. **Define Node Models**:
   In Neomodel, you define models as Python classes. Each class represents a node in the graph.

   ```python
   from neomodel import StructuredNode, StringProperty, IntegerProperty, RelationshipTo

   class Person(StructuredNode):
       name = StringProperty()
       age = IntegerProperty()
       friends = RelationshipTo('Person', 'FRIEND')

   # Define another node class, e.g., for a Company
   class Company(StructuredNode):
       name = StringProperty()
       employees = RelationshipTo('Person', 'EMPLOYED_BY')
   ```

2. **Create and Save Nodes**:
   You can create instances of these classes and save them to the Neo4j database.

   ```python
   # Create and save a person
   john = Person(name="John", age=30).save()

   # Create another person and save
   jane = Person(name="Jane", age=25).save()

   # Create a relationship
   john.friends.connect(jane)
   ```

3. **Query the Graph**:
   You can query the graph using the model’s methods.

   ```python
   # Find people named 'John'
   johns = Person.nodes.filter(name='John')

   for john in johns:
       print(f"{john.name}, {john.age} years old")

   # Get all friends of 'John'
   for friend in john.friends:
       print(f"{friend.name} is a friend of John")
   ```

### Key Concepts:
- **StructuredNode**: This is the base class for defining nodes (entities) in your graph. You define properties using attributes (e.g., `StringProperty`, `IntegerProperty`).
- **Relationships**: You can define relationships between nodes using `RelationshipTo` or `RelationshipFrom`, specifying the type of relationship (e.g., "FRIEND", "EMPLOYED_BY").
- **Saving and Querying**: Nodes can be saved using the `.save()` method, and you can query nodes using `filter()`, `nodes`, or Cypher queries.

### Advantages:
- **Pythonic API**: The API is simple and follows Python conventions, making it easy to use for Python developers.
- **Automatic Schema Handling**: Neomodel handles the schema for you by automatically creating constraints and indexes for unique node properties (e.g., unique constraints for primary keys).
- **Integration with Neo4j**: It integrates tightly with Neo4j, making it easy to work with graph data without worrying about the underlying Cypher queries or database operations.

### Use Case:
Neomodel is especially useful when you need to interact with a Neo4j graph database while working within a Python application, providing a clean and simple interface to graph data without having to manually write raw Cypher queries. It’s ideal for applications that involve complex relationships, such as social networks, recommendation systems, fraud detection, and knowledge graphs.
