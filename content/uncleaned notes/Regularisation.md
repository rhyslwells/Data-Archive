---
tags:
  - ml
  - process
---
## Description

Used to prevent [[overfitting]] by penalising the [[loss function]] during training to reduce model complexity.

This penalty term ==imposes constraints== on the weights or parameters of the model, encouraging simpler or smoother models that are less prone to overfitting.

Types:
1. L1 [[Lasso]] (Absolute value)
2. L2: [[Ridge]] (Square)

Lasso tends to produce sparse models by ==eliminating less important features==, while Ridge tends to ==shrink the coefficients of all features== without eliminating any, making it more suitable for situations where retaining all features is desired but with reduced magnitudes to prevent overfitting.
## Questions and Answers

Explain what [[Regularisation]] is and why it is useful. ;; Regularization is the process of adding a tuning parameter to a model to ==induce smoothness in order to prevent overfitting.== It helps in controlling the complexity of the model and reduces the chance of fitting noise in the training data.

What is it [[Regularisation]]?;; A technique to prevent overfitting in a model by adding a penalty term to the cost function.