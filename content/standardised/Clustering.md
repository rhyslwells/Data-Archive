---
title: 
tags:
  - clustering
aliases: 
category:
---
Clustering involves grouping a set of data points into subsets or clusters based on inherent patterns or similarities. It is an [[Unsupervised Learning]]technique used for tasks like customer segmentation and [[Outliers|anomalies]] detection. The primary goal of clustering is to organize data by grouping similar items.

## Applications

- Customer Segmentation: Group customers with similar purchasing behavior or demographics for targeted marketing.
- Image Segmentation: Group pixels in an image based on color or texture to identify objects or regions.
- Anomaly Detection: Identify clusters of normal behavior to detect anomalies that deviate significantly from these clusters.
## Methods

- [[K-means]]
- [[DBScan]]
- [[Hierarchical Clustering]]

## [[Interpretability]]

 [[Feature Scaling]]: Essential for bringing features to the same scale, as clusters may appear distorted without it.
  ```python
  from sklearn.preprocessing import scale
  from sklearn.preprocessing import MinMaxScaler
  ```

Use clustering to find correlations between features. Utilize a [[Dendrograms]] to visualize the relationship between features.


## Clustermap
- Purpose: Identify which features are most similar using dendrograms.
- Visualization: Regions of color show clustering, similar to a heatmap.
- Functionality: Performs clustering on both rows and columns.

Requirements: Input should be numerical; data needs to be scaled.
  ```python
  import seaborn as sns
  sns.clustermap(x_scaled, cmap='mako', standard_scale=0)  # 0 for rows, 1 for columns
  ```
## Resources
- [Video Explanation](https://youtu.be/crQkHHhY7aY?t=149)
- [Seaborn Clustermap Documentation](https://seaborn.pydata.org/generated/seaborn.clustermap.html)
