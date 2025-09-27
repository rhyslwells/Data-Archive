---
aliases:
- L2
category: ML
date modified: 27-09-2025
tags: []
---
L2 Regularization, also known as Ridge Regularization, adds a penalty term proportional to the square of the weights to the [[Loss function]]. 

This technique enhances the robustness of linear regression models (and [[Logistic Regression]]) by penalizing large coefficients, encouraging smaller weights overall, and ==distributing weight values more evenly across all features.==

### Key Points

- **Overfitting Mitigation**: Ridge helps mitigate [[Overfitting]], especially in high-dimensional datasets, and is effective in managing [[Multicollinearity]] among predictors.
- **Coefficient Shrinkage**: Unlike Lasso regularization (L1), which can eliminate some features entirely by driving their coefficients to zero, Ridge reduces the magnitudes of coefficients but retains all features.
- **Multicollinearity Handling**: Particularly useful when predictors are highly correlated, as it stabilizes estimates by shrinking the coefficients of correlated features.
- **Feature Retention**: Ridge retains all features in the model, unlike Lasso, which can perform [[Feature Selection]]by setting some coefficients to zero.

### Understanding Ridge Regularization

#### 1. Purpose of Ridge Regularization

- **Penalty Addition**: Adds a penalty term to the loss function, proportional to the square of the coefficients (weights), discouraging overly complex models by shrinking the coefficients.

#### 2. Mathematical Formulation

- The loss function for Ridge regression can be expressed as:
  $$\text{Loss} = \text{SSE} + \lambda \sum_{j=1}^{p} b_j^2$$
  - Where:
    - SSE (Sum of Squared Errors) is the original loss function for [[Linear Regression]]
    - $\lambda$ is the regularization parameter (penalty term) that controls the strength of the penalty.
    - $b_j$ are the coefficients of the model.
    - $p$ is the number of predictors.

#### 3. Effect of the Regularization Parameter ($\lambda$)

- **Range**: $\lambda$ can take values from 0 to infinity.
- **Impact**:
  - A small $\lambda$ (close to 0) means the model behaves similarly to ordinary least squares (OLS) regression, with minimal regularization.
  - A large $\lambda$ increases the penalty, leading to smaller coefficients and a simpler model.

#### 4. Finding the Best $\lambda$

- Use techniques like cross-validation to determine the optimal value of $\lambda$. By testing various values and evaluating model performance, select the one that minimizes prediction error (or variance).

### Example Code

```python
from sklearn.linear_model import Ridge

# Initialize a Ridge model
model = Ridge(alpha=0.1)  # alpha is the regularization strength
model.fit(X_train, y_train)
```

### Resources

- [Understanding Ridge Regularization](https://www.youtube.com/watch?v=Q81RR3yKn30)

---

### Understanding the Content

- **L2 Regularization (Ridge)**: This technique is crucial for improving model generalization by penalizing large coefficients, which helps in reducing overfitting and handling multicollinearity. The regularization parameter $\lambda$ controls the trade-off between fitting the training data well and keeping the model coefficients small.

[[Ridge]]
### L2 Regularization (Ridge Regression): for [[Neural network]]



Adds a penalty term to the loss: \( L_{\text{regularized}} = L + \lambda \cdot ||W||^2 \). This discourages overly complex models by penalizing large weights.

Example:

```python
from tensorflow.keras.regularizers import l2
Dense(25, activation="relu", kernel_regularizer=l2(0.01))
```