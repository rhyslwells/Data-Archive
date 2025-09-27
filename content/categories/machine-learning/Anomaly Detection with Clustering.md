---
aliases: []
category: ML
date modified: 27-09-2025
tags:
- anomaly_detection
- clustering
---
Outliers can often be detected using [[Clustering]] methods because they either form small, distinct groups or are isolated from major clusters without strict statistical assumptions.

| Method                         | Key Assumption                                                         | Strengths                                                                                                              | Weaknesses                                                                                           | Typical Use Case                                            |
| :----------------------------- | :--------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------- | :---------------------------------------------------------- |
| [[DBSCAN]]                     | Clusters are areas of high density separated by low-density regions    | - No need to specify number of clusters- Can find arbitrarily shaped clusters- Explicitly identifies noise (anomalies) | - Struggles with varying densities- Sensitive to parameter choice (epsilon, minPoints)               | Spatial data clustering and density-based anomaly detection |
| [[Isolated Forest]]            | Anomalies are easier to isolate via random splits                      | - Efficient on large, high-dimensional datasets- Requires fewer assumptions- Scales well with data size                | - Not suited for small datasets- Less [[Interpretability\|interpretable]] than density-based methods | High-dimensional tabular data anomaly detection             |
| [[Local Outlier Factor (LOF)]] | Anomalies have significantly lower local density compared to neighbors | - Good for local anomaly detection- Adapts to density variations                                                       | - Sensitive to choice of k (number of neighbors)- Poor performance on high-dimensional data          | Detecting subtle anomalies in medium-sized tabular datasets |





