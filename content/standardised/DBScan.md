---
title: 
tags:
  - clustering
aliases: 
category:
---
**DBSCAN** (Density-Based Spatial Clustering of Applications with Noise) is a [[clustering]] algorithm that groups together data points ==based on density==. It is particularly useful when K-means doesn't work well, such as in datasets with complex shapes or when there are outliers.

- **Used when [[K-means]] doesn't work**: DBSCAN handles datasets with ==irregular cluster shapes== and is not sensitive to outliers like K-means.
- **When you have nesting of clusters**: It can identify clusters of varying shapes and sizes without needing to predefine the number of clusters, unlike K-means.
- **Groups core points to make clusters**: DBSCAN identifies core points, which have many nearby points, and groups them together.
- **Can identify [[Outliers]]**: It detects noise points (outliers) that don't belong to any cluster.

### Python Example:

```python
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Create sample data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Apply DBSCAN
dbscan = DBSCAN(eps=0.3, min_samples=5)
clusters = dbscan.fit_predict(X)

# Plot results
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='plasma')
plt.show()
```

This will cluster the data and visualize it, highlighting core points and marking outliers as separate clusters.

## 🌐 Sources
1. [hex.tech - When and Why To Choose Density-Based Methods](https://hex.tech/blog/comparing-density-based-methods/#:~:text=DBSCAN%20is%20a%20density%2Dbased)
2. [newhorizons.com - DBSCAN vs. K-Means: A Guide in Python](https://www.newhorizons.com/resources/blog/dbscan-vs-kmeans-a-guide-in-python)