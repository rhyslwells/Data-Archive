---
aliases: []
category:
date modified: 27-07-2025
tags: [evaluation, ml_process, model_explainability]
title: 
---
Feature importance refers to ==techniques that assign scores to input features== (predictors) in a machine learning model to ==indicate their relative impact on the model's predictions.==

Feature importance is typically assessed ==after== [[Model Building]]. It involves analyzing the trained model to determine the impact of each feature on the predictions.

Feature importance helps in:
- improving model [[interpretability]], 
- identifying key predictors, 
- and possibly performing [[Feature Selection]] to reduce dimensionality, and refining performance

The ==outcome== is a ranking or scoring of features based on their importance.

By understanding which features contribute the most to the predictions, you can focus on the most relevant information in your data and potentially reduce model complexity without sacrificing performance.
### Types of Feature Importance Methods

Model-Specific Methods:
- Tree-based models: Models like Random Forests, Gradient Boosted Trees, and Decision Trees have built-in mechanisms for calculating feature importance. They do so based on the decrease in impurity (e.g., [[Gini Impurity]] in classification tasks or variance in regression tasks) or based on the reduction in error when the feature is used for splitting. Tree-based algorithms like [[Random Forests]] or [[XGBoost]] automatically calculate feature importance. 
- Linear models: In models like linear regression or logistic regression, feature importance can be derived from the absolute values of the model coefficients, assuming features are standardized ([[Why standardise features]]).
   
Model-Agnostic Methods:
- Permutation importance: This method measures the importance of a feature by randomly shuffling its values and observing the impact on the model's performance. The larger the decrease in performance, the more important the feature is.
- [[SHapley Additive exPlanations]]
- [[Local Interpretable Model-agnostic Explanations]]