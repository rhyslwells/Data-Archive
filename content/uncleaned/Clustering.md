---
title: 
tags:
  - clustering
aliases: 
category:
---
- Clustering involves grouping a set of data points into subsets or clusters based on inherent patterns or similarities. It is an unsupervised learning technique used for tasks like customer segmentation and anomaly detection.

What is the goal of clustering;; to group items in a way that similar items such as grouping documents by topic.

Clustering

Customer segmentation: Clustering can be used to group customers with similar purchasing behaviour or demographics for targeted marketing.
Image segmentation: Clustering algorithms can group pixels in an image based on their colour or texture to identify objects or regions.
Anomaly detection: By identifying clusters of normal behaviour, anomalies that deviate significantly from these clusters can be detected.

It involves grouping a set of data points into subsets or clusters based on the inherent patterns or similarities within the data. 

The goal is to organize the data to cluster similar items.

Clustering is an [[Unsupervised learning]] learning technique.

Type: [[Classification]] [[Unsupervised learning]]

## Methods

[[K-means]]
[[DBScan]]
[[Clustering]]
## [[Hyperparameter]]:

[[WCSS and elbow method]]
## [[interpretability]]

[[Feature Scaling]] is usefull to bring features to the same scale, as clusters look crappy if you dont [[Feature Scaling]].
```python
from sklearn.preprocessing import scale
from sklearn.preprocessing import MinMaxScaler
```


## Notes

Not to be confused with [[Clustering]] in [[Feature Preprocessing]].

## Description

The use case of getting a [[Correlation]] between features to build clusters.

In [[Clustering]] use a [[dendrogram]] to see relation of features.

![[Pasted image 20240405173403.png|500]]



## Description clustermap

Can tell which ==features are the most similar== with [[Dendrograms]]

Regions of colour show [[Clustering]], similar to [[Heatmap]]

Clustermaps performs [[Clustering]] [[Clustering]] on both rows and columns.

![[Pasted image 20240119170302 1.png|300]]

## Resources

[Explanation](https://youtu.be/crQkHHhY7aY?t=149)

https://seaborn.pydata.org/generated/seaborn.clustermap.html
## Implementation

Input should be numerical.
Need to scale data
`sns.clustermap(df,standard_scale=0)` for rows 1 for cols
```
import seaborn as sns
sns.clustermap(x_scaled, cmap='mako')
```



Hierarchical Clustering
: Hierarchical clustering builds a treelike structure of clusters, with similar clusters merged together at higher levels.

