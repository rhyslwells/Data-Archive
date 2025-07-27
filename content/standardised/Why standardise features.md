---
aliases: []
category:
date modified: 27-07-2025
tags: [ml, preprocessing]
---
Standardizing ([[Standardisation]]) features is a common preprocessing step in machine learning and statistical modeling. It transforms each feature to have mean $0$ and standard deviation $1$.

### 1. Equal Feature Contribution

When features are on different scales, models that rely on distance metrics or gradient-based optimization may be biased toward features with larger numeric ranges.

Example:
* `SAT`: 400–1600
* `Rand 1,2,3`: 1–5

Without standardization, `SAT` may dominate the model simply due to its larger scale.

Standardization ensures all features contribute proportionally.

### 2. Interpretability of Coefficients

In a linear model, standardized features allow coefficients to represent the change in the target (in standard deviations) per one standard deviation increase in the predictor.

This allows direct comparison of feature importance:
* Larger coefficients imply stronger influence on the prediction.

### 3. Improved Numerical Stability

Gradient-based optimizers (e.g. in neural networks, logistic regression) converge faster and more reliably when inputs are on comparable scales.

This prevents inefficient steps due to scale imbalance:

* Large features → overshooting
* Small features → slow progress

### 4. Required by Certain Algorithms

Some algorithms are scale-sensitive and may require standardization for proper functioning:

* Distance-based: k-NN, k-means, SVM
* Regularized models: Ridge, Lasso
* Projection methods: PCA, [[Latent Dirichlet Allocation|LDA]]

Without scaling, these models may behave unpredictably or suboptimally.
### 5. Consistent Treatment of Future Data

Standardization ensures that new observations are transformed using the same scaling parameters as the training data.

The same `StandardScaler` used during training must be applied to new inputs during inference to maintain model validity.

### When *Not* to Standardize

* When features are already on the same scale (e.g. proportions, dummy variables)
* With tree-based models like:
  * Decision Trees
  * Random Forests
  * XGBoost

These models are scale-invariant and do not benefit from standardization.
