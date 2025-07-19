---
title: Isolation Forest and Its Use in Anomaly Detection
tags:
  - anomaly_detection
  - data_quality
aliases:
  - iForest
  - anomaly isolation
category: ML
importance: 
engagement: 
recency_of_interest: 2024-09-26
---

 Isolation Forest (iForest) is an [[Model Ensemble]]-based method used for anomaly detection. It operates by isolating data points using a series of random binary splits.
 
The key idea is that [[standardised/Outliers|anomalies]], being rare and different, are easier to isolate and thus require fewer splits. 

Mathematically, the isolation of a point is captured by the path length in a decision tree, where shorter paths indicate anomalies. The algorithm constructs multiple isolation trees, and the ==anomaly score of a point== is determined by the average path length across all trees. 

Isolation Forest is highly efficient for large datasets and is particularly useful when the assumption is that anomalies are rare and distinct from normal instances.

**Steps:**
- Randomly select a feature and a split value between the maximum and minimum values of that feature.
- Repeat this process to create a tree structure.
- Anomalies are isolated faster than normal points, leading to shorter path lengths in the tree.
- The average path length across multiple trees is used to compute an anomaly score.


 Key Components:  
 - **Isolation Trees (iTrees)**: Binary trees where the goal is to isolate observations based on randomly chosen features and split values.  
 - **Anomaly Score**: Calculated based on the average path length across all isolation trees.  
 - **Path Length**: Anomalies tend to have shorter path lengths as they are easier to isolate.  
 - **Random Splitting**: Random feature selection and splitting result in the separation of instances, with fewer splits isolating anomalies.

Important
 - Anomalies are identified based on shorter average path lengths in the isolation forest, ==indicating that fewer splits are needed to isolate them.==  
 - The method scales well with large datasets because it relies on randomly generated trees, avoiding complex distance or density computations.
 - Isolation Forest assumes that anomalies are few and distinct; it may perform poorly when anomalies are not easily distinguishable.  
 - The method is sensitive to the [[Hyperparameter]] such as the number of trees and sample size.

Follow up questions
 - How does the isolation forest compare to density-based methods like [[DBSCAN]] in terms of detecting complex anomalies?  [[Anomaly Detection with Clustering]]
 - What impact does the choice of sample size have on the performance and accuracy of isolation forests in high-dimensional data?

Related Topics
 - [[Random Forests]] for classification and regression  
 - One-Class [[Support Vector Machines|SVM]] for anomaly detection
