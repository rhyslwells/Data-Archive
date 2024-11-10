---
tags:
  - ml_process
  - drafting
---
Purpose: The primary goal of feature selection is to identify and retain the most relevant features for model training while ==removing irrelevant or redundant ones==. This helps in simplifying the model, reducing overfitting, and improving computational efficiency.

Process: Feature selection is typically performed before model training. It involves evaluating features based on certain criteria or algorithms to decide which features to keep or discard.

Through an iterative process, feature selection experiments with different methods, adjusts parameters, and evaluates model performance until an optimal set of features is found.

See [[Feature Selection vs Feature Importance]]
### Methods

The choice of feature selection method depends on factors like the size of your dataset, the number of features, and the complexity of your model. It's often a balance between computational cost and performance improvement.

- [[Filter Methods]]: Select features based on statistical properties, independent of any machine learning algorithm. (Separate stage to training)
- [[Wrapper Methods]]: Involve training multiple models with different subsets of features and selecting the subset that yields the best performance. (Separate stage to training)
- [[Embedded Methods]]: Perform feature selection as part of the model training process. (Part of training)

After selecting features, it's essential to evaluate your model's performance ([[Model Evaluation]]) with the chosen subset. Sometimes, feature selection can inadvertently remove important information.

### Detecting Noisy or Redundant Features

- [[Correlation]] Analysis: Use a [[Heatmap]] or [[Clustering]]. Features with low correlation to the target or high correlation with other features may be candidates for removal.

- [[Dimensionality Reduction]] Techniques: Techniques like [[Principal Component Analysis]] or Singular Value Decomposition ([[SVD]]) can transform the features into a lower-dimensional space while preserving as much variance as possible. Features with low contribution to the principal components can be considered for removal.

- Visualizations: Plotting pairwise scatter plots or [[Heatmap]] of feature [[Correlation]] can provide visual insights into redundant features. Clusters of highly correlated features or scatter plots showing no discernible pattern with the target variable can indicate noisy or redundant features.
### Investigating Features

1. Variance Thresholding: Check the [[variance]] & [[Distributions]] of each feature. Features with very low variance (close to zero) contribute little information and may be considered noisy. Removing such features can help simplify the model without sacrificing much predictive power.

1. Univariate Feature Selection: Use statistical tests like chi-square for categorical variables or [[ANOVA]] for numerical variables to assess the relationship between each feature and the target variable. Features with low test scores or high p-values may be less relevant and can be pruned.