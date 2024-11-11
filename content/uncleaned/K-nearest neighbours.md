---
title: 
tags:
  - classifier
aliases:
  - KNN
category:
---
K-nearest Neighbors is a non-parametric method used for both [[classification]] and [[regression]] tasks. It classifies a sample by a majority vote of its neighbors, assigning the sample to the class most common among its \(k\) nearest neighbors, where \(k\) is a small positive integer.

### How It Works

- **Classification:** When a new data point needs classification, KNN identifies its \(k\) nearest neighbors in the training data based on feature similarity. The class label most common among these neighbors is assigned to the new data point.
- **Regression:** For regression tasks, KNN predicts the average value of the \(k\) nearest neighbors.

### Applications

  - [[Recommender systems]]
  - Pattern recognition

### Key Points

- **Non-parametric:** KNN does not make any assumptions about the underlying data distribution.
- **Supervised Learning:** Despite the note's mention of unsupervised learning, KNN is actually a supervised learning algorithm because it requires labeled training data.

### Use Cases

- KNN is useful for tasks where the decision boundary is irregular and not easily captured by parametric models ([[parametric vs non-parametric models]]). It is simple to implement and understand but can be computationally expensive with large datasets.


### Understanding K-nearest Neighbors

KNN is a straightforward algorithm that relies on the proximity of data points to make predictions. It is particularly effective in scenarios where the relationship between features and the target variable is complex and non-linear.

- **Choice of \(k\):** The value of \(k\) is crucial. A small \(k\) can be sensitive to noise, while a large \(k\) can smooth out the decision boundary too much.

- **Distance Metric:** The choice of distance metric (e.g., Euclidean, Manhattan) affects how neighbors are determined and can impact the algorithm's performance.

KNN is best suited for smaller datasets due to its computational intensity, as it requires calculating the distance between the new data point and all existing data points.