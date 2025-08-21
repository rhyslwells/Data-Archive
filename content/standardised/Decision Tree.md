---
aliases: []
category:
date modified: 1-08-2025
tags: [classifier, regressor]
---
A Decision Tree is a type of [[Supervised Learning]] algorithm used to predict a target variable based on input features. It involves splitting data into subsets to create a tree-like model.

Decision Tree Structure are a flowchart-like model where each internal node represents a decision based on a feature, branches represent outcomes, and leaf nodes represent final predictions.

Splits data recursively based on feature importance, forming a tree-like structure.

The decision tree algorithm calculates the i.e the [[Gini impurity]] for each possible split and selects the one with the lowest impurity. Use to make predictions on new data, the algorithm traverses the decision tree from the root node to a leaf node, following decision rules based on input features. Once it reaches a leaf node, it assigns the corresponding class label or prediction.

Also see: [[CART]]

![[Pasted image 20240404154526.png|500]]
### Key Concepts

1. Objective: Predict a target variable using input features.
2. Splitting: Identify the best feature to split the data into subsets, aiming for homogeneous groups.
3. Impurity Calculation: Use metrics like [[Gini Impurity]] or [[Cross Entropy]] ([[Gini Impurity vs Cross Entropy]]) to evaluate splits. Choose the split that minimizes impurity.
4. Purity: A node is pure if it perfectly classifies the data, requiring no further splits.
5. Leaf Node Output: Assigns the most common class label or average value in the node.
6. [[Overfitting]]: Can occur if the tree is too complex. Mitigate with [[pruning]] and limiting tree depth.
7. [[Cross Validation]]: Refine the model to better generalize to new data.
### Splitting Process

The splitting process in a Decision Tree involves dividing the dataset into subsets to create a tree-like structure. This process is crucial for building an effective model that can predict target variables accurately.

Splitting Criteria:
- The algorithm evaluates various features to determine the best split at each node.
- It selects the feature and split point that minimize impurity in the resulting child nodes.
- The split that most effectively reduces impurity is chosen, ensuring that each subset is as homogeneous as possible.

#### Building Process

1. **Initial Splitting**:
   - Begin at the root node and select the best feature to split the data. This selection is based on impurity measures such as Gini impurity or entropy for [[Classification]] tasks, and variance reduction for regression tasks.
   - The goal is to create subsets that are as homogeneous as possible with respect to the target variable.

2. **Recursive Partitioning**:
   - After the initial split, each subset becomes a child node.
   - The algorithm recursively applies the splitting process to each child node.
   - Continue splitting until stopping criteria are met, such as reaching a maximum tree depth, having a minimum number of samples per node, or achieving insufficient improvement in purity.

3. **Leaf Nodes**:
   - The process continues until reaching leaf nodes, which have no further splits.
   - At each leaf node, assign a class label (for classification) or predict a continuous value (for regression) based on the majority class or average value of the samples in that node.

### Refinement

Pruning:
  - Pre-pruning: Stop tree growth early based on criteria like maximum depth or minimum impurity improvement.
  - Post-pruning: Allow the tree to grow fully, then prune back based on performance metrics.

### [[Hyperparameter]]

Can use [[GridSeachCv]] to pick the best paramaters.

| **Parameter**       | **Purpose**                      | **Effect**                  | **Example**                                      |
|---------------------|----------------------------------|-----------------------------|--------------------------------------------------|
| `criterion`         | Splitting criteria               | Impacts decision logic.     | `criterion='gini'` or `criterion='entropy'`      |
| `max_depth`         | Maximum tree depth               | Prevents overfitting.       | `max_depth=5` limits the tree depth to 5.        |
| `min_samples_split` | Min samples to split a node      | Limits tree growth.         | `min_samples_split=10` requires at least 10 samples to split a node. |
| `min_samples_leaf`  | Min samples at leaf node         | Reduces overfitting.        | `min_samples_leaf=5` ensures every leaf has at least 5 samples. |
| `max_features`      | Features considered for splitting| Adds randomness.            | `max_features='sqrt'` or `max_features=3`.       |
| `max_leaf_nodes`    | Max leaf nodes allowed           | Reduces overfitting.        | `max_leaf_nodes=20` caps the tree at 20 leaves.  |
| `class_weight`      | Adjusts for imbalanced data      | Improves fairness.          | `class_weight='balanced'` or `class_weight={0:1, 1:2}`. |
| `ccp_alpha`         | Pruning parameter                | Simplifies tree.            | `ccp_alpha=0.01` prunes weak splits based on complexity. |

### Advantages and Disadvantages of Decision Trees

Advantages:
- Simple and [[interpretability|interpretable]] model.
- Minimal data preparation required.
- Transparent decision-making process.

Disadvantages:
- Prone to overfitting, especially with complex datasets.
- Sensitive to small changes in data.
- Can become complex with many features.

