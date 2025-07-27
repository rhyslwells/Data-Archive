---
aliases: [KNN]
category:
date modified: 27-07-2025
tags: [classifier, ml]
title: 
---
K-Nearest Neighbors is a [[non-parametric]], [[supervised learning]] algorithm used for both classification and regression tasks. It predicts the label of a new data point based on the labels of its $k$ nearest neighbors in the training data, where $k$ is a user-defined positive integer.

### How It Works

* Classification: Assigns the class most common among the $k$ nearest neighbors.
* Regression: Predicts the average of the target values of the $k$ nearest neighbors.
* Distance Metric: Common choices include Euclidean and Manhattan distance; the choice affects neighbor selection and model performance.
* Choice of $k$: Small $k$: sensitive to noise, Large $k$ : smoother but may blur decision boundaries
### Characteristics

* Non-parametric: Makes no assumptions about the underlying data distribution.
* Instance-based: Stores training data and delays computation until prediction.
* Simple and [[interpretability|interpretable]]: Easy to understand and implement.
* Computationally expensive: Requires distance computation to all training points at prediction time.

### Use Cases

* Works well when the decision boundary is irregular or non-linear.
* Most effective on smaller datasets due to computational cost.

### Applications

* [[Recommender systems]]
* Pattern recognition