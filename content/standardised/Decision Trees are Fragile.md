---
aliases: []
category:
date modified: 23-08-2025
tags:
  - classifer
  - model
  - explainability
---
[[Decision Tree]]s are considered ==fragile== because small changes in the training data can lead to large changes in the tree structure and predictions.

### Why this happens

1. Greedy splitting

   * Trees build by making locally optimal splits at each node.
   * A slight change in data (e.g., one sample or a small noise) can change which split is chosen, altering the entire subtree downstream.

1. High variance [[Variance in ML]]

   * Decision trees have low bias but high variance.
   * They overfit easily to noise or outliers unless pruned or regularized.

1. Hierarchical structure

   * Early splits strongly influence the rest of the tree.
   * A different root split due to minor changes cascades into a completely different structure.

1. Sensitivity to outliers

   * Extreme values can dominate split selection, further increasing instability.

### Consequence

* Different training sets produce very different trees → poor generalization.
* This is why [[Model Ensemble|ensemble]] methods like [[Random Forest|Random Forest ]]and [[Gradient Boosted Trees]] are widely used; they reduce variance by combining multiple trees.
