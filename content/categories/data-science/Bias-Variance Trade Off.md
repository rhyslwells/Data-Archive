---
aliases: []
category: DS
date modified: 27-09-2025
tags: []
---
The bias-variance trade-off describes the relationship between model complexity and performance. 
- High bias (underfitting) occurs when a model is too simple, leading to poor performance on both training and test data. 
- High variance (overfitting) happens when a model is overly complex, performing well on training data but poorly on unseen data.

Ways to Reduce Bias and Variance:
- [[Regularisation]]
- [[Boosting]]
- [[Bagging]]

Related to [[Overfitting]]
### [[Regularisation]]

Key Takeaway:
- Regularization trades variance for bias. The goal is to find the sweet spot that minimizes overall prediction error on unseen data.

Regularization directly affects the bias–variance trade-off in machine learning by controlling model complexity.
### Impact on Bias and Variance

| Regularization                                              | Model Complexity      | Variance           | Bias           | Typical Effect                                                        |
| ----------------------------------------------------------- | --------------------- | ------------------ | -------------- | --------------------------------------------------------------------- |
| Increase regularization (e.g., higher $\lambda$ in L1/L2) | Reduces flexibility   | Decreases variance | Increases bias | Model becomes simpler → less sensitive to training data, may underfit |
| Decrease regularization (smaller $\lambda$)               | Increases flexibility | Increases variance | Decreases bias | Model can fit training data better → may overfit                      |

### Intuition

* Variance: Measures sensitivity to small changes in the training data. High variance -> overfitting.
* Bias: Measures error from oversimplifying the model. High bias ->underfitting.
* Regularization: Adds a penalty for large weights-> discourages complex models -> reduces variance but increases bias.


