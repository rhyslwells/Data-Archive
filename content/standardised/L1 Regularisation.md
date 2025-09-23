---
aliases:
  - L1
  - Lasso
category:
date modified: 27-07-2025
tags:
  - selection
  - regularization
  - optimisation
  - ml
---
L1 regularization adds a penalty proportional to the ==absolute values== of the model coefficients to the [[loss function]]. This penalty encourages ==sparsity==-some coefficients become exactly zero-making it useful for [[Feature Selection]].

Remember how L1 and L2 metrics work with regards to the unit ball.

Loss Function:

$$
\text{Loss} = \text{MSE} + \lambda \sum_{i=1}^{n} |w_i|
$$

where:

* $\text{MSE}$ = Mean Squared Error
* $\lambda$ = Regularization strength
* $w\_i$ = Model weights

Key Properties:

* Adds penalty based on absolute value of coefficients.
* Drives some coefficients to zero by removes less relevant features.
* Produces a sparse model (subset of important features retained).

Example (Lasso in scikit-learn):

```python
from sklearn.linear_model import Lasso

# Initialize and fit Lasso model
model = Lasso(alpha=0.1)  # alpha controls regularization strength
model.fit(X_train, y_train)
```

Use Case:

* Ideal for feature selection when dealing with many predictors.

[Video Explanation](https://www.youtube.com/watch?v=NGf0voTMlcs)
