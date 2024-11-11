---
title: 
tags:
  - classifier
  - regressor
aliases: 
category:
---
# Summary

1) What are we trying to predict?

2) What feature (categorical) best gives this classification i,e splits to leaves with TRUE or FALSE.
3) Calculate the total impurity for each branch, choose the one the gives the lowest number (ie best predictor).

![[Pasted image 20240411093348.png|700]]

A node is pure if it gives a correct classification to its term (i.e no further splitting) We stop when pure.

Output of leaf is the category with the most values.

Decision trees can be [[Overfitting]] if the leafs have a small number of values for a dataset, use [[pruning]]. 

Can put limit of tree depth.

Use cross validation to refine the model to better represent the data. (i.e may be more pruned).

---

A decision tree is a {{supervised}} learning algorithm used for both classification and regression tasks. 

Here's how a decision tree works:

**Splitting**: The algorithm starts at the root node (the topmost node) and selects the best feature to split the dataset into subsets. The feature and the split point are chosen based on certain criteria, such as ==Gini impurity== ==or entropy== for classification tasks, and variance reduction for regression tasks. The goal is to make the subsets as homogeneous as possible with respect to the target variable.

**Splitting Criteria**: When building a decision tree, the algorithm considers various features to split the data at each node==. It selects the feature and the split point that minimize the Gini impurity in the resulting child nodes==. The split that reduces impurity the most is chosen.

[[Gini Impurity]]

==**Recursive Partitioning**==: After the first split, each subset becomes a child node of the root node. The algorithm then recursively applies the splitting process to each child node, creating further splits until certain stopping criteria are met. ==Stopping criteria== may include reaching a maximum tree depth, having nodes with minimum samples, or not improving the purity measure significantly with further splits.

**Leaf Nodes**: Eventually, the splitting process continues until the algorithm reaches leaf nodes, which are nodes with no further splits. ==At each leaf node, the algorithm assigns a class label (for classification)== or predicts a continuous value (for regression) based on t==he majority class== or average value of the samples in that node, respectively.

 **Decision Making**: In practical terms, when deciding which feature to split on, the decision tree algorithm calculates the Gini impurity for each possible split and selects the one that results in the lowest impurity after the split.

**Tree Structure**: The decision tree structure resembles a flowchart, where each internal node represents a decision based on a feature, each branch represents the outcome of that decision, and each leaf node represents a class label or a prediction.

**Predictions**: To make predictions on new data, the algorithm traverses the decision tree from the root node down to a leaf node, following the decision rules based on the input features. Once it reaches a leaf node, it assigns the corresponding class label or prediction.


![[Pasted image 20240404154526.png]]

How can overfitting in a decision tree be reduced, and what are the two approaches to pruning?;;Overfitting in a decision tree can be reduced using pruning. 

How do use prune a decision tree?;; Two approaches to pruning are ==Pre-pruning==, which stops tree growth based on certain criteria, and ==Post-pruning==, which allows the tree to grow and then prunes based on tree size and performance.

**What is a decision tree?** ;;An algorithm that generates a flowchart from a dataset, representing a tree-like structure. It can also be seen as a series of if-else conditions where a feature is evaluated at each node.

**How are decision trees built?**;; Built in a decision tree is a recursive process. At each step, the algorithm searches for the best feature to split the dataset while minimizing ==entropy==.  The process continues until the tree is sufficiently homogenous or another stopping criterion is met.

What is Entropy in regards to Decision trees?;; Entropy describes dataset variety.

**What are the main advantages of decision trees?**;; output simplicity, minimal data preparation requirements, and human readability, making them suitable for transparent decision-making.

**What are some disadvantages of decision trees?**;;overfitting, instability to small changes in input data, and the potential for complex structures with datasets having many features.

Decision trees create a hierarchical structure of decisions based on the features of the data.

Limitations
Prone to overfitting if not properly pruned or regularised.