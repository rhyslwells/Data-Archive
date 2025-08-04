---
aliases: []
category: 
date modified: 1-08-2025
tags: [clustering, graph]
---
In graph theory, a community (also known as a cluster or module) is a group of nodes that are more densely connected to each other than to the rest of the network.
 

https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.louvain.louvain_communities.html

### Intuition
Communities often represent:
- Functional units in biological networks (e.g., protein complexes)
- Groups of friends or followers in social networks
- Topical clusters in knowledge graphs or citation networks

They capture meso-scale structure—between the local (node/edge) and global (graph-level) scale.

### Formal Definition
There is no single universal definition, but communities typically exhibit:

- High intra-community density: lots of edges within the group
- Low inter-community density: few edges connecting to other groups

Mathematically, a common goal is to maximize modularity, a measure that quantifies the density of links inside communities compared to links between them.

### Community Detection Algorithms
Some widely used algorithms:

| Algorithm | Description |
|-|-|
| Louvain | Fast and widely used; optimizes modularity |
| Girvan–Newman | Based on removing high-betweenness edges |
| Label Propagation | Propagates labels through the network |
| Leiden | Improved version of Louvain for better quality and performance |
