---
tags:
  - regressor
aliases: 
category:
---


https://scikit-learn.org/1.5/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor

[[Boosting]]

The `GradientBoostingRegressor` from the `sklearn.ensemble` module is a model used for regression tasks. It builds an [[Model Ensemble]] of [[Decision Tree]] in a sequential manner, where each tree tries to correct the errors made ==by the previous ones==. Here’s a breakdown of the key parameters:

1. **loss**: Specifies the loss function to optimize. Default is `'squared_error'`, which is the least-squares loss function. Other options like `'absolute_error'` can be used for robustness against outliers.

2. **learning_rate**: Controls the contribution of each tree to the final prediction. A smaller value (e.g., 0.01) makes the model learn more slowly, but it can lead to better generalization. Default is 0.1.

3. **n_estimators**: The number of boosting stages (i.e., trees). More trees can improve performance but also increase the risk of overfitting. Default is 100.

4. **subsample**: The fraction of samples to be used for fitting each tree. Setting this to a value less than 1.0 can help reduce overfitting, at the cost of a slight increase in bias. Default is 1.0 (use all samples).

5. **criterion**: The function used to measure the quality of a split. `'friedman_mse'` is the default, which is an improved version of mean squared error for decision trees. Other options include `'mse'` and `'mae'`.

6. **max_depth**: The maximum depth of the individual trees. This parameter controls the complexity of each tree. Default is 3, which typically works well for most tasks.

7. **min_samples_split**: The minimum number of samples required to split an internal node. Default is 2, meaning any node can be split as long as there are at least 2 samples.

8. **min_samples_leaf**: The minimum number of samples required to be at a leaf node. This helps control overfitting by requiring more data points at each leaf. Default is 1.

9. **alpha**: The quantile used for the loss function in cases of robust regression. This is useful when dealing with data that includes outliers. Default is 0.9.

10. **validation_fraction**: The fraction of training data to set aside for validation to monitor performance during training. Default is 0.1.

11. **n_iter_no_change**: The number of iterations with no improvement on the validation score to wait before stopping the training early. Default is `None`, meaning no early stopping.

12. **ccp_alpha**: Complexity parameter used for pruning the trees. A larger value leads to more pruning (simplifying the model), which can help prevent overfitting.
