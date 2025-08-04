---
aliases: 
category: 
date modified: 27-07-2025
tags:
  - querying
  - NLP
---
Text2Cypher is a concept that allows users to convert natural language queries into Cypher queries, which are used to interact with [[GraphRAG|graph database]] like [[Neo4j]]. This functionality enables users to ask questions in a more intuitive/[[interpretability|interpretable]], conversational manner, rather than needing to know the specific syntax of [[Cypher]].

Allows the user to ask vague questions.
Allows for multihop queries on the graph

Overall, Text2Cypher aims to simplify the interaction with graph databases, making it accessible to users who may not be familiar with query languages.
### Key Features of Text2Cypher:

1. **Natural Language Processing**: It utilizes natural language processing (NLP) techniques to understand user queries and translate them into structured Cypher queries.

2. **Flexibility**: Users can ask vague or complex questions that may not directly relate to the underlying data structure, making it easier to retrieve information from a graph database.

3. **Traversal Queries**: Text2Cypher can generate traversal queries that navigate through the graph, allowing for multi-hop queries that explore relationships between entities.

4. **Explainability**: By converting natural language into Cypher, it helps provide a clearer understanding of how the data is structured and how the queries are executed, enhancing interpretability.

