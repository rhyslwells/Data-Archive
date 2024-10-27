---
tags:
  - drafting
---
How do you make a model better?

- Optimize model parameters to improve performance.
- Use techniques like grid search or random search.
- Assess model performance on the testing set using relevant metrics (e.g., accuracy, precision, recall, F1-score).
- Evaluate generalization ability and potential biases.

### [[Regularisation]]
### Hyperparameter Tuning

[[Hyperparameter]]

- **Hyperparameters**:
  - Parameters set before training that control the learning process, such as the number of nodes in a neural network.
  - Techniques like GridSearchCV are used to explore the hyperparameter space and identify the best settings for model performance.

1. **Optimization**:
   - Involves adjusting model parameters to enhance performance.
   - Techniques like grid search or random search are used to find the best hyperparameters.

- Objective: Tune the model’s hyperparameters to improve performance. For regularized linear regression, the main hyperparameter to tune is the regularization strength (`alpha` in Ridge or Lasso). Use cross-validation to evaluate the model’s performance with different hyperparameters.
   - Method: Grid Search or Random Search with cross-validation.

Bayesian optimisation or evolutionary algorithms