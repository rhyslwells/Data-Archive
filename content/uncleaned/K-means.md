---
tags:
  - ml
  - clustering
---
# Description

: Kmeans [[clustering]] partitions data into k clusters, with each data point assigned to the cluster with the nearest centroid.

- [[K-means]] is an {{[[Unsupervised learning]]}} that organises unlabelled data into meaningful groups.
- Initially have to pick a [[Hyperparameter]] $k$ of the number of clusters. To choose the correct number of clusters in [[K-means]] we use a {{[[WCSS and elbow method]]}} diagram.
- [[K-means]] works by ;; Randomly choosing k points (centroids), grouping the remaining data to closest centroid, redefining the centroid, then repeating. Where each sample will get the label of the cluster it was assigned to.
- You would want to use scatterplot, to plot clusters with centroids.
- Has the ability to be updated with new information and compare difference in centroids.
###### Resources

[Statquest](https://www.youtube.com/watch?v=4b5d3muPQmA)





[[K-means]]
Limitations
sensitive to the initialisation of cluster centroids and requires specifying the number of clusters beforehand.



[[K-means]]
- **How does the [[K-means]] algorithm work?**: It partitions a dataset into K clusters, assigning data points to the closest cluster mean. The means are updated iteratively until convergence.