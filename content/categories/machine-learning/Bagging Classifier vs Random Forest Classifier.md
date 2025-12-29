---
aliases: []
category: ML
date modified: 21-11-2025
tags:
  - classifer
  - ml
---

**BaggingClassifier**

* Implements bootstrap aggregating.
* Builds multiple independent copies of a chosen base estimator using bootstrapped samples of the training data.
* Final predictions are obtained through averaging (regression) or majority voting (classification).
* When to use:
	* You want to ensemble models other than trees.
	* Example: ensembling multiple KNN classifiers or SVMs.

**RandomForestClassifier** (Sklearn)

* A specialised form of bagging that always uses decision trees as base estimators.
* Adds extra randomness by selecting a random subset of features at each split, controlled by $max_{features}$.
	* You need an ensemble of decision trees with feature-level randomness.
	* You want strong generalisation and minimal hyperparameter tuning.
### Key Differences

Random forests often outperform standard bagging with trees because the additional feature randomness decorrelates the trees, improving generalisation.

| Feature                 | BaggingClassifier              | RandomForestClassifier                                          |
| ----------------------- | ------------------------------ | --------------------------------------------------------------- |
| Base model              | Any estimator                  | Always a decision tree                                          |
| Feature randomness      | None by default                | Random subset of features at each split ($\text{max_features}$) |
| Correlation reduction   | From bootstrapped samples only | From bootstrapping and random feature selection                 |
| Bias–variance behaviour | Reduces variance               | Reduces variance more effectively                               |
| Out-of-bag scoring      | Supported                      | Supported                                                       |
| Speed and tuning        | Depends on base model          | Optimised for trees; typically faster and simpler to tune       |
| Interpretability        | Depends on estimator           | Tree-specific tools available (feature importance, etc.)        |
| API scope               | General-purpose                | Specialised and efficient for tree ensembles                    |
