---
aliases: []
category: DEVOPS
date modified: 27-09-2025
tags:
- code_snippet
---
This method combines both L1 ([[L1 Regularisation]]) and L2 ([[Ridge]]) regularization by adding both absolute and squared penalties to the loss function. It strikes a balance between Ridge and Lasso.

It is particularly useful when you have high-dimensional datasets with highly correlated features.

The Elastic Net loss function is:

    $$\text{Loss} = \text{MSE} + \lambda_1 \sum_{i=1}^{n} |w_i| + \lambda_2 \sum_{i=1}^{n} w_i^2$$
    
where $\lambda_1$ controls the L1 regularization and $\lambda_2$ controls the L2 regularization.

#### Code

```python
from sklearn.linear_model import ElasticNet

# Initialize an Elastic Net model
model = ElasticNet(alpha=0.1, l1_ratio=0.5)  # l1_ratio controls the L1/L2 mix
model.fit(X_train, y_train)
```