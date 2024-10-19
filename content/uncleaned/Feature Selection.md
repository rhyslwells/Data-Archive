---
tags:
  - ml_process
  - drafting
---
# Description

- Understanding the features in your dataset is crucial for building effective machine learning models.
  
- Feature selection helps identify the most relevant features for model prediction, enhancing its accuracy and efficiency.
  
- Techniques such as [[Correlation]] analysis, feature importance scores, and dimensionality reduction are employed to sift through the data and extract the most informative features.
  
- Not all features are created equal; some may introduce noise or redundancy, while others hold valuable predictive power.
  
- Through an iterative process, feature selection experiments with different methods, adjusts parameters, and evaluates model performance until an optimal set of features is found.
  
- The goal of feature selection is to;; simplify the model, mitigate overfitting, and enhance its generalization to new data.
  
- By selecting the most pertinent features, we streamline the model's complexity, improve its ability to make accurate predictions, and ensure robust performance on unseen data.
## Methods

The choice of feature selection method depends on factors like the size of your dataset, the number of features, and the complexity of your model. It's often a balance between computational cost and performance improvement.

- [[filter methods]] by relevance based on statistical properties.(Separate stage to training)

- [[wrapper methods]] these involve training multiple models with different subsets of features and selecting the subset that yields the best performance. (Separate stage to training)

- [[embedded methods]]: These methods perform feature selection as part of the model training process. (Part of training)

After selecting features, it's essential to evaluate your model's performance with the chosen subset. Sometimes, feature selection can inadvertently remove important information.

## How do you detect if a feature is noisy or redundant.

- [[Correlation]] analysis: use a [[Heatmap]]/[[Clustering]]. Features with low correlation to the target or high correlation with other features may be candidates for removal.
  
- **Dimensionality Reduction Techniques**: Techniques like [[Principal Component Analysis]] or Singular Value Decomposition ([[SVD]]) can transform the features into a lower-dimensional space while preserving as much variance as possible. Features with low contribution to the principal components can be considered for removal.
  
- **Visualizations**: Plotting pairwise scatter plots or heatmaps of feature correlations can provide visual insights into redundant features. Clusters of highly correlated features or scatter plots showing no discernible pattern with the target variable can indicate noisy or redundant features.
  
- Analyse the feature importance's [LINK](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html) (using [[Decision Tree]] for example).

## To investigate 

1. **Variance Thresholding**: Check the [[variance]] of each feature. Features with very low variance (close to zero) contribute little information and may be considered noisy. Removing such features can help simplify the model without sacrificing much predictive power.
   
2. **Univariate Feature Selection**: Use statistical tests like chi-square for categorical variables or [[ANOVA]] for numerical variables to assess the relationship between each feature and the target variable. Features with low test scores or high p-values may be less relevant and can be pruned.

## Resources

Combine feature increases feature importance.
# notes

can be done per model you are training for.

What are the main purposes of feature selection?;;Reducing the number of features increases understandability, reducing the training times, reducing dimensionality, removing noise.

How can you use variance for ?;;Features with low variance can be dropped since (almost) constant features do not provide any information.

What are the main techniques of ?;; [[Filter method]], [[wrapper methods]] and [[embedded methods]]

[[Filter method]] in feature selection are?;; Statistical techniques are used to evaluate the relationship between individual features and the target features. 

[[wrapper methods]] in feature selection are?;; adding/removing features so you can evaluate their effect on the model based on a certain scoring.

 [[embedded methods]] in feature selection are?;;  The features are selected during the model training, and more important features are assigned a higher rank. Examples of such models are decision trees and lasso regression models.

How can you use [[correlation]] for ?;; Use the correlation of each feature with the target. Keep features with a significant correlation, i.e., a correlation value < -0.5 or > +0.5. Use pairwise correlation between features. If two features are highly correlated, one can be dropped since they provide the same information.