[LINK](https://www.youtube.com/watch?v=NGf0voTMlcs)

In L1 regularization, a penalty term proportional to the absolute value of the weights is added to the loss function. This encourages sparsity in the model by driving some weights to exactly zero, effectively performing feature selection.

- Adds a penalty term proportional to the ==absolute value of the model's coefficients.==
- Encourages sparsity by ==driving some coefficients to exactly zero.==
- Useful for [[Feature Selection]] , as it tends to eliminate less important features by setting their corresponding coefficients to zero.
- Can result in a sparse model with fewer features retained.
-  Lasso regression adds a penalty term to the loss function proportional to the absolute value of the coefficients of the features. This encourages sparsity in the coefficient vector, effectively setting some coefficients to zero and performing feature selection.