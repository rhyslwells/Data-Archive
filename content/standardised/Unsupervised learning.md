---
title: 
tags:
  - "#clustering"
  - field
aliases:
  - unsupervised
category:
---
Unsupervised learning is a type of machine learning where the algorithm is trained on data without explicit labels or predefined outputs. 

Unsupervised learning involves discovering hidden patterns in data without predefined labels. It is valuable for exploratory data analysis, [[Clustering]], and [[Isolated Forests]].

The goal is to find hidden patterns, relationships, or structures in the data. Unlike supervised learning, which uses labeled input-output pairs, unsupervised learning relies solely on input data, allowing the algorithm to uncover insights independently.

### Key Concepts

1. No Labeled Data: There is no ground truth or correct output associated with the input data.
2. Data Patterns: The algorithm identifies inherent structures, clusters, or associations within the dataset.
3. Objective: The primary objective is to explore the data and organize it to reveal underlying patterns.

### Common Types of Unsupervised Learning

#### [[Clustering]]

Description: The algorithm groups similar data points together based on their features.

Example: Customer segmentation in marketing, where a clustering algorithm divides customers into groups based on purchasing behavior, demographics, or browsing history.

Popular Algorithms:
  - [[K-means]]: Divides the data into \( k \) clusters, where each data point belongs to the nearest cluster.
  - Hierarchical Clustering
  - [[DBScan]]
  - [[Support Vector Machines]]
  - [[K-nearest neighbours]]

#### [[Dimensionality Reduction]]

Description: Reduces the number of input variables (features) while preserving as much information as possible. This is helpful for high-dimensional data, where visualization and analysis become challenging.

Popular Algorithms:
  - [[Principal Component Analysis]] 

#### [[Isolated Forests]]

Description: Identifies [[Outliers]] or unusual data points that don’t conform to the expected pattern in the dataset.

Example: Detecting fraudulent credit card transactions by identifying transactions that deviate significantly from typical spending patterns.

Mechanism: Works by randomly partitioning the data and identifying [[Outliers|anomalies]] as points that can be isolated quickly.
