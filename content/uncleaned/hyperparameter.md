---
title: 
tags:
  - drafting
aliases: 
category:
---
**What are hyperparameters?**;; parameters in machine learning models that control the learning process. They are set before training, i.e. k-value in k-nearest neighbor or the number of nodes in a [[What is a neural network|neural network]].

Used [[GridSeachCv]] to search through the [[hyperparameter]] space

```python
rf_regressor = RandomForestRegressor(random_state=42)
grid_search = GridSearchCV(estimator=rf_regressor, param_grid=param_grid, cv=5, scoring='neg_mean_absolute_error')
grid_search.fit(X_train, y_train)
best_params = grid_search.best_params_

# Model Training with best hyperparameters
rf_regressor = RandomForestRegressor(**best_params, random_state=42)
rf_regressor.fit(X_train, y_train)
```

Given a parameter grid of [[hyperparameter]], a model, then you model it on the hypers, then gives you the best hypers, that gives the highest cross validation performance.

![[Pasted image 20240128194244.png|500]]

