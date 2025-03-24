---
title: 
tags:
  - data_cleaning
  - data_visualization
aliases:
  - PCA
category:
---
PCA is a tool for [[Dimensionality Reduction]] in [[Unsupervised Learning]] to reduce the dimensionality of data. 

It transforms the original data into a new coordinate system defined by the principal components, which are ==orthogonal vectors== that capture the most [[Variance]] in the data.

It helps simplify models, enhances [[interpretability]], and improves computational efficiency by transforming data into a lower-dimensional space while ==retaining the most significant variance==, and reducing noise.


### How PCA Works

- ==Linear Technique==: PCA is a linear technique, meaning it assumes that the relationships between features are linear. This distinguishes it from methods like [[Manifold Learning]] which can capture non-linear relationships.

- Principal Components: PCA identifies principal components, which are linear combinations of the original features. These components are ordered by the amount of variance they capture from the data, with the first principal component capturing the most variance, the second capturing the second most, and so on.
### Comparison with Other Techniques

- [[t-SNE]]: Unlike PCA, t-SNE is a non-linear technique used for visualization, preserving local structures in high-dimensional data.
- [[Manifold Learning]]: Techniques like Isomap and Locally Linear Embedding (LLE) are designed to capture non-linear structures, which PCA might miss due to its linear nature
### Code Implementation

In [[ML_Tools]] see:
- [[PCA-Based Anomaly Detection]]
- [[PCA_Analysis.ipynb]]

### Related terms

- [[PCA Explained Variance Ratio]]
- [[PCA Principal Components]]