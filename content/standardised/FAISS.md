---
tags:
  - NLP
  - ml_process
aliases: 
category: 
phase: 
topic: 
filename:
---
FAISS (Facebook AI [[Similarity Search]]) is a library developed by Facebook AI Research that enables efficient [[similarity search]] and [[clustering]] of dense vectors. It is especially well-suited for applications involving high-dimensional vector data, such as [[NLP]]
### Core Concept

At its core, FAISS takes a large number of high-dimensional vectors (e.g., sentence or document embeddings), and enables fast [[similarity search]] to retrieve the most similar vectors to a given [[Querying|query]].

For example, in an NLP [[LLM Memory]]:
- Documents or notes are embedded into vector space using a model like SBERT.
- These embeddings are stored in a FAISS index.
- Given a query, its embedding is computed, and FAISS returns the nearest neighbors (i.e., most semantically similar notes).
### Index Types

FAISS offers different types of indices depending on use case:
- `IndexFlatL2`: exact search using L2 (Euclidean) distance.
- `IndexIVFFlat`: approximate search using inverted files.
- `IndexHNSW`: Hierarchical Navigable Small World graph-based index (good for high recall).
- `IndexPQ`: product quantization for memory-efficient indexing.

FAISS is optimized for:
- Fast retrieval from large collections of vectors (millions or more).
- Approximate nearest neighbor (ANN) search, which trades off accuracy for speed.
- Exact search, depending on the chosen index type.
- GPU acceleration for very large-scale search tasks.
### Use Cases

- Embedding search (e.g., text, image, or audio embeddings)
- Recommendation systems
- [[Semantic search]]
- Clustering of high-dimensional data
- [[Vector Embedding]]