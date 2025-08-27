---
aliases: []
category:
date modified: 23-08-2025
tags: [classifier, explainability]
---
In decision trees, each leaf node typically contains the outcome for all training examples that fall into that leaf. This outcome can be represented in two ways:

#### 1. Single Predicted Value

* Classification: The leaf predicts the majority class (e.g., if 60% of samples are class A, predict A).
* Regression: The leaf predicts the mean of the target values in that leaf.

#### 2. Distribution of Target Values

Instead of storing just a single prediction, the leaf can store the distribution of the target variable:

* Classification: Store class probabilities.
  Example: If a leaf has 100 samples -> 60 class 1, 40 class 2 -> Distribution = {class 1: 0.6, class 2: 0.4}.
* Regression: Store a histogram or density estimate of the continuous values rather than just their mean.

#### Why use distributions?

* Enables probabilistic predictions (e.g., predict class probabilities, not just hard labels).
* Provides uncertainty estimates, useful for Bayesian methods and risk-sensitive decisions.
* Improves interpretability by showing the variability in outcomes for samples reaching the same leaf.

This method is commonly applied in:

* Random Forests and Gradient Boosted Trees (which use class probabilities for classification).
* Probabilistic decision tree models for uncertainty-aware predictions.
