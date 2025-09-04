---
aliases: []
category:
date modified: 27-07-2025
tags:
  - classifier
---

A [[Random Forest]] is an [[Model Ensemble]] method that combines many [[Decision Tree]]s to improve accuracy and generalisation.

How does Random Forest work?

* Each tree is trained on a random bootstrap sample of the training data ([[bagging]]).
* At each split, the tree considers only a random subset of features (commonly $\sqrt{n}$ features if $n$ is the total number).
* The final prediction is obtained by majority vote (classification) or averaging (regression).

This randomness reduces correlation between trees, making the overall model more robust ([[Generalisation|generalize]]).

Key properties:
* Can handle regression, classification, dimensionality reduction, and missing values.
* Flexible, robust, and resistant to overfitting compared to a single [[Decision Tree]].
* Works well with high-dimensional data.

Hyperparameters to tune:

* `n_estimators`: number of trees.
* `max_depth`: maximum depth of each tree.
* `max_features`: number of features considered at each split (default $\sqrt{n}$ for classification).
* `n_jobs`: controls parallelism during training (more cores = faster training, but watch out for system slowdown).

Strengths:
* Reduces variance compared to a single tree.
* Handles large datasets and mixed feature types well.
* Provides feature importance estimates.

Weaknesses:
* Can still overfit with noisy or very high-dimensional data.
* Less interpretable than a single decision tree.

Evaluation:
* Out-of-bag (OOB) error can be used as an internal validation metric (data not included in bootstrap samples).
* Model performance can be refined by tuning [[Hyperparameter]]s.

Related:
- [[Random Forest Regression]]
- [[Random Forest for Time Series]]
- [[Time Series Forecasting]]


![[Pasted image 20240128194716.png]]
![[Pasted image 20240118145117.png]]
