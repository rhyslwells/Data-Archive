---
aliases:
  - L2
---
L2 Regularization (Ridge) adds a penalty term proportional to the square of the weights to the loss function. Ridge regularization is a powerful technique to enhance the robustness of linear regression models (and [[Logistic Regression]]) by adding a penalty for large coefficients. 

This encourages smaller weights overall and tends to distribute the weight values more evenly across all features.

It helps mitigate [[overfitting]], especially in high-dimensional datasets, and is effective in managing [[multicollinearity]] among predictors. 

By carefully selecting the regularization parameter $\lambda$, one can achieve a balance between model complexity and predictive accuracy.

==Coefficient Shrinkage==: Ridge does not set coefficients to zero but reduces their magnitudes, which helps retain all features in the model.

Multicollinearity Handling: It is particularly useful in situations where predictors are highly correlated (multicollinearity), as it stabilizes the estimates by shrinking the coefficients of correlated features.

 ==Feature Retention==: Unlike Lasso regularization (L1), which can eliminate some features entirely by driving their coefficients to zero, Ridge retains all features but with reduced impact.

### Understanding Ridge Regularization

Ridge Regularization, also known as L2 regularization, is a technique used to prevent overfitting in regression models, particularly in linear regression. Here’s a breakdown of its key concepts:

Resources:
[LINK](https://www.youtube.com/watch?v=Q81RR3yKn30)
#### 1. Purpose of Ridge Regularization

- Penalty Addition: Ridge regularization adds a penalty term to the loss function, which is proportional to the square of the coefficients (weights) of the model. This penalty discourages overly complex models by shrinking the coefficients.
  
#### 2. Mathematical Formulation
- The loss function for Ridge regression can be expressed as:
 $$\text{Loss} = \text{SSE} + \lambda \sum_{j=1}^{p} b_j^2$$
  - Where:
    - SSE (Sum of Squared Errors) is the original loss function for linear regression.
    - $\lambda$ is the regularization parameter (penalty term) that controls the strength of the penalty.
    - $b_j$ are the coefficients of the model.
    - $p$ is the number of predictors.

#### 3. Effect of the Regularization Parameter ($\lambda$)
- Range: $\lambda$ can take values from 0 to infinity.
- Impact:
  - A small $\lambda$ (close to 0) means the model behaves similarly to ordinary least squares (OLS) regression, with minimal regularization.
  - A large $\lambda$ increases the penalty, leading to smaller coefficients and a simpler model.
  
#### 4. Finding the Best $\lambda$

- To determine the optimal value of $\lambda$, techniques like cross-validation are used. By testing various values of $\lambda$ and evaluating model performance, the one that minimizes prediction error (or variance) can be selected.


