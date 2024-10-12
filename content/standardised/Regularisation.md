---
tags:
  - ml
  - ml_process
---
>[!Summary]
Regularisation is a technique to prevent overfitting in a model by adding a penalty term to the cost function. Regularization is the process of adding a tuning parameter to a model to ==induce smoothness in order to prevent overfitting.== It helps in controlling the complexity of the model and reduces the chance of fitting noise in the training data.

Used to prevent [[overfitting]] by penalising the [[loss function]] during training to reduce model complexity.

This penalty term ==imposes constraints== on the weights or parameters of the model, encouraging simpler or smoother models that are less prone to overfitting.

Types:
1. L1 [[Lasso]] (Absolute value)
2. L2: [[Ridge]] (Square)

Lasso tends to produce sparse models by ==eliminating less important features==, while Ridge tends to ==shrink the coefficients of all features== without eliminating any, making it more suitable for situations where retaining all features is desired but with reduced magnitudes to prevent overfitting.

**What is regularization
used to prevent overfitting in machine learning models. It involves adding a penalty term to the loss function during training, discouraging the model from assigning too much importance to specific features. For example ==Lasso== and ==Ridge== regularization. By reducing the model's complexity, regularization promotes better generalization to new, unseen data.

[[Dropout]] is a regularization technique that ==randomly drops units== (along with their connections) from the neural network during training. This prevents units from co-adapting too much and forces the network to learn more robust features. By averaging the predictions of multiple dropout networks, the model generalizes better and reduces overfitting.**