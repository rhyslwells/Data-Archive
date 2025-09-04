---
aliases: []
category:
date modified: 1-08-2025
tags: [classifier, regressor]
---
A [[Decision Tree]] is a [[Supervised Learning]] algorithm that predicts a target variable from input features by recursively splitting data into subsets. The model takes a tree-like form where:

* Internal nodes represent decisions based on features.
* Branches represent outcomes of those decisions.
* Leaf nodes provide final predictions.

The algorithm evaluates possible splits using measures such as [[Gini Impurity]] or [[Cross Entropy]] ([[Gini Impurity vs Cross Entropy]]), choosing the one that produces the ==lowest impurity==. For classification, a leaf assigns the majority class; for regression, it outputs the mean value.

Also see: [[CART]]

### Key Concepts

1. Objective: Predict a target variable from input features.
2. Splitting: Select features that best divide the data into homogeneous subsets.
3. Impurity: Evaluate splits with metrics like [[Gini Impurity]] or entropy.
4. Purity: A node is pure if all samples belong to the same class.
5. Leaf Node Output: Provides a prediction from the samples in the node.
6. [[Overfitting]]: Deep trees may overfit; mitigate with [[pruning]] or depth limits.
7. [[Cross Validation]]: Ensures the model generalizes well to new data.

### Building Process

1. Root Node: Begin by choosing the best feature and split based on impurity (for [[Classification]]) or variance reduction (for regression).
2. Recursive Partitioning: Apply the same splitting process to each child node until stopping criteria are met (e.g., depth, minimum samples, no significant purity gain).
3. Leaf Nodes: When splitting stops, assign the prediction at the leaf. See [[Distributions in Decision Tree Leaves]].

### Refinement

Pruning reduces complexity and improves generalization:
* Pre-pruning: Stop growth early using constraints such as maximum depth or minimum impurity decrease.
* Post-pruning: Grow the full tree, then prune back based on performance metrics.

![[Pasted image 20240404154526.png|500]]

## Other Considerations

### [[Hyperparameter]] of Decision Trees

Can use [[GridSeachCv]] to pick the best paramaters.

| Parameter           | Purpose                           | Effect                  | Example                                                              |
| ------------------- | --------------------------------- | ----------------------- | -------------------------------------------------------------------- |
| `criterion`         | Splitting criteria                | Impacts decision logic. | `criterion='gini'` or `criterion='entropy'`                          |
| `max_depth`         | Maximum tree depth                | Prevents overfitting.   | `max_depth=5` limits the tree depth to 5.                            |
| `min_samples_split` | Min samples to split a node       | Limits tree growth.     | `min_samples_split=10` requires at least 10 samples to split a node. |
| `min_samples_leaf`  | Min samples at leaf node          | Reduces overfitting.    | `min_samples_leaf=5` ensures every leaf has at least 5 samples.      |
| `max_features`      | Features considered for splitting | Adds randomness.        | `max_features='sqrt'` or `max_features=3`.                           |
| `max_leaf_nodes`    | Max leaf nodes allowed            | Reduces overfitting.    | `max_leaf_nodes=20` caps the tree at 20 leaves.                      |
| `class_weight`      | Adjusts for imbalanced data       | Improves fairness.      | `class_weight='balanced'` or `class_weight={0:1, 1:2}`.              |
| `ccp_alpha`         | Pruning parameter                 | Simplifies tree.        | `ccp_alpha=0.01` prunes weak splits based on complexity.             |
### Advantages and Disadvantages of Decision Trees

Advantages:
- Simple and [[Interpretability|interpretable]] model.
- Minimal data preparation required.
- Transparent decision-making process.

Disadvantages:
- Prone to overfitting, especially with complex datasets.
- Sensitive to small changes in data.
- Can become complex with many features.
- [[Decision Trees are Fragile]]

