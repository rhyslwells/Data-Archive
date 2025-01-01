---
tags: 
aliases: 
category: 
phase: optimisation
topic: Hyperparameter_tuning
filename:
---
Objective:
- Tune the model’s hyperparameters to improve performance. For example, in regularized linear regression, the main hyperparameter to tune is the regularization strength (e.g., `alpha` in Ridge or Lasso).
- Use [[Cross Validation]] to evaluate the model’s performance with different hyperparameters.

Optimization Techniques:
- [[GridSeachCv]]: Exhaustively searches through a specified subset of hyperparameters.
- Random Search: Randomly samples from the hyperparameter space, often more efficient than grid search.
- [[Optuna]]
- [[Regularisation]]: Often part of the hyperparameter tuning process, especially in models prone to overfitting.

Key Considerations
- Balance Between Exploration and Exploitation: Ensure a good balance between exploring the hyperparameter space and exploiting known good configurations.
- [[Cross Validation]]: Use cross-validation to ensure that the hyperparameter tuning process is robust and not overfitting to a particular train-test split.
### Links

See [[ML_Tools]]:

Hyperparameter_tuning_GridSearchCV.py

Hyperparameter_tuning_RF.py
Video link: https://youtu.be/jUxhUgkKAjE?list=PLtqF5YXg7GLltQSLKSTnwCcHqTZASedbO&t=765
