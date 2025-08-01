---
aliases: []
category: 
date modified: 27-07-2025
tags: []
---
**Definition:**  
Inertia is the sum of squared distances from each point to its assigned cluster center. Lower values indicate more compact clusters.

==Is this WCSS?==

**Use in [[K-means]]:**
- Used to determine optimal $k$ via the elbow method: [[WCSS and elbow method]]
- Sensitive to scale and number of features
    
**Exploratory Questions:**
- How does inertia correlate with cluster separation?
- Is it meaningful when clusters are non-spherical?
- What are its limitations in high-dimensional spaces?

Related:
- [[Cluster Density]]