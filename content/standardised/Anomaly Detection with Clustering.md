---
aliases: []
category:
date modified: 27-07-2025
tags: [anomaly_detection, clustering]
---
Outliers can often be detected using [[clustering]] methods because they either form small, distinct groups or are isolated from major clusters without strict statistical assumptions.

| Method                         | Key Assumption                                                         | Strengths                                                                                                              | Weaknesses                                                                                           | Typical Use Case                                            |
| :----------------------------- | :--------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------- | :---------------------------------------------------------- |
| **[[DBSCAN]]**                 | Clusters are areas of high density separated by low-density regions    | - No need to specify number of clusters- Can find arbitrarily shaped clusters- Explicitly identifies noise (anomalies) | - Struggles with varying densities- Sensitive to parameter choice (epsilon, minPoints)               | Spatial data clustering and density-based anomaly detection |
| **[[Isolation Forest]]**       | Anomalies are easier to isolate via random splits                      | - Efficient on large, high-dimensional datasets- Requires fewer assumptions- Scales well with data size                | - Not suited for small datasets- Less [[interpretability\|interpretable]] than density-based methods | High-dimensional tabular data anomaly detection             |
| **Local Outlier Factor (LOF)** | Anomalies have significantly lower local density compared to neighbors | - Good for local anomaly detection- Adapts to density variations                                                       | - Sensitive to choice of k (number of neighbors)- Poor performance on high-dimensional data          | Detecting subtle anomalies in medium-sized tabular datasets |

## [[DBSCAN]]

Purpose:  
  - Detects anomalies based on density rather than explicit statistical models.

Key Idea:  
  - Points in low-density regions are identified as anomalies.

Steps:
  1. Cluster data points based on neighborhood density.
  2. Identify points that do not belong to any dense cluster (noise) as anomalies.

## Local Outlier Factor (LOF)

Purpose:  
  - A density-based method that identifies anomalies by comparing a point's local density to its neighbors.

Key Idea:  
  - Points with substantially lower local density than their neighbors are considered outliers.

Steps:
  1. For each point, compute local density based on its k-nearest neighbors.
  2. Calculate the LOF score: a value higher than 1 suggests potential anomaly.
  3. Points with high LOF scores are flagged as anomalies.

## [[Isolated Forest]]



