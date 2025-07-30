---
aliases: 
category: 
date modified: 27-07-2025
tags:
  - clustering
---
## Local Outlier Factor (LOF)

Purpose:  
  - A density-based method that identifies anomalies by comparing a point's local density to its neighbors.

Key Idea:  
  - Points with substantially lower local density than their neighbors are considered outliers.

Steps:
  1. For each point, compute local density based on its k-nearest neighbors.
  2. Calculate the LOF score: a value higher than 1 suggests potential anomaly.
  3. Points with high LOF scores are flagged as anomalies.