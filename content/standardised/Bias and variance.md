---
aliases: []
category:
date modified: 1-08-2025
tags: [architecture, explainability]
---
### Related to [[Overfitting]]

Ways to Reduce Bias and Variance:
- [[Regularisation]]
- [[Boosting]]
- [[Bagging]]

What is Bias in Machine Learning?  
Bias occurs when a model produces ==consistently unfair or inaccurate results==, usually caused during training due to design choices.

What Does High Bias Mean for a Machine Learning Model?  
High bias refers to a situation where a model has a strong and often ==simplistic assumption== about the underlying data, leading to underfitting.

It is biased to the data.

What is the Variance of a Machine Learning Model?  
Variance measures how much a ==model's predictions change when trained on different subsets== of the training data. It indicates how much the model overfits the training data.

What is the Difference Between Bias and Variance in Machine Learning?

- Bias: The error that occurs when the model cannot learn the true relationship between input and output variables.
- Variance: The error that arises when the model is ==too sensitive== to the training data and does not generalize well to new data.

Explain the Bias-Variance Trade-off in the Context of Model Complexity:

The bias-variance trade-off describes the relationship between model complexity and performance. 
- High bias (underfitting) occurs when a model is too simple, leading to poor performance on both training and test data. 
- High variance (overfitting) happens when a model is overly complex, performing well on training data but poorly on unseen data.