---
aliases: []
category:
date modified: 1-08-2025
tags: [graph, visualization]
---
PageRank is an algorithm originally developed by Larry Page and Sergey Brin (founders of Google) to rank web pages in [[search]] engine results. It measures the relative importance of each node (e.g., webpage) in a directed graph based on the structure of incoming links.
### Intuition

The core idea is:
> A node is important if many other important nodes link to it.

PageRank simulates a “random surfer” who clicks on links at random:
- With probability $d$ (typically 0.85), the surfer follows a link from the current page.
- With probability $1 - d$, the surfer jumps to a random page.

### Mathematical Formulation

Given a graph with $N$ nodes, the PageRank of node $i$ is defined recursively as:

$$
PR(i) = \frac{1 - d}{N} + d \sum_{j \in \text{In}(i)} \frac{PR(j)}{L(j)}
$$

Where:
- $d$ is the damping factor (usually 0.85),
- $\text{In}(i)$ is the set of nodes linking to $i$,
- $L(j)$ is the number of outbound links from node $j$.



### Implementation (using NetworkX)

```python
import networkx as nx

G = nx.DiGraph()
G.add_edges_from([
    ('A', 'B'), ('B', 'C'), ('C', 'A'), ('A', 'D'), ('D', 'C')
])

pagerank_scores = nx.pagerank(G, alpha=0.85)
for node, score in pagerank_scores.items():
    print(f"{node}: {score:.4f}")
```



### 📊 Use Cases
- Graph-based NLP: Keyword extraction (e.g., TextRank).
