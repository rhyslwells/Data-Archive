---
aliases:
  - L1
category: 
date modified: 27-07-2025
tags:
  - drafting
---

1. **L1 Regularization (Lasso Regression)**:
    - In L1 regularization, a penalty proportional to the absolute value of the coefficients is added to the loss function.
    - The L1 penalty tends to shrink some coefficients to exactly zero, effectively performing **feature selection** by eliminating irrelevant features.
    - **Lasso regression** (Least Absolute Shrinkage and Selection Operator) is an example of a model that uses L1 regularization.

    The L1-regularized loss function is:
    $\text{Loss} = \text{MSE} + \lambda \sum_{i=1}^{n} |w_i|$
    where $\lambda$ is the regularization parameter, $w_i$ are the model weights, and MSE is the mean squared error.


For **Lasso Regression (L1)**:

```python
from sklearn.linear_model import Lasso

# Initialize a Lasso model
model = Lasso(alpha=0.1)  # alpha is the regularization strength
model.fit(X_train, y_train)
```

[LINK](https://www.youtube.com/watch?v=NGf0voTMlcs)

In L1 regularization, a penalty term proportional to the absolute value of the weights is added to the loss function. This encourages sparsity in the model by driving some weights to exactly zero, effectively performing feature selection.

- Adds a penalty term proportional to the ==absolute value of the model's coefficients.==
- Encourages sparsity by ==driving some coefficients to exactly zero.==
- Useful for [[Feature Selection]] , as it tends to eliminate less important features by setting their corresponding coefficients to zero.
- Can result in a sparse model with fewer features retained.
- Lasso regression adds a penalty term to the loss function proportional to the absolute value of the coefficients of the features. This encourages sparsity in the coefficient vector, effectively setting some coefficients to zero and performing feature selection.