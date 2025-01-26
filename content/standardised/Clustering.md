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
- [[Anomaly Detection]]: Identify clusters of normal behavior to detect anomalies that deviate significantly from these clusters.
## Methods

- [[K-means]]
- [[DBScan]]
- [[Hierarchical Clustering]]
- [[Gaussian Mixture Models]]

## [[Interpretability]]

 [[Feature Scaling]]: Essential for bringing features to the same scale, as clusters may appear distorted without it.
  ```python
  from sklearn.preprocessing import scale
  from sklearn.preprocessing import MinMaxScaler
  ```

Use clustering to find [[Correlation]] between features. Utilize a [[Dendrograms]] to visualize the relationship between features.