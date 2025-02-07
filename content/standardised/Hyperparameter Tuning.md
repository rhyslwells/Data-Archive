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
- [[standardised/Optuna]]
- [[Regularisation]]: Often part of the hyperparameter tuning process, especially in models prone to overfitting.

Key Considerations
- Balance Between Exploration and Exploitation: Ensure a good balance between exploring the hyperparameter space and exploiting known good configurations.
- [[Cross Validation]]: Use cross-validation to ensure that the hyperparameter tuning process is robust and not overfitting to a particular train-test split.

Order matters: See [[Interpretable Decision Trees]]. Example when tuning hyperparameters for [[Random Forests]] try the following:

1. High Train Accuracy, Low Test Accuracy (Overfitting)
- Objective: Reduce model complexity to prevent overfitting.
- Parameters to Adjust:
	- `max_depth`: Limit the depth of each tree.
	- `min_samples_split`: Increase the minimum number of samples required to split a node.
	- `max_features`: Reduce the number of features considered for splitting.
	- `n_estimators`: Decrease the number of trees in the forest.

2. Low Train Accuracy, Low Test Accuracy (Underfitting)
- Objective: Increase model complexity to improve learning capacity.
- Parameters to Adjust:
	- `n_estimators`: Increase the number of trees.
	- `max_depth`: Allow deeper trees.
	- `min_samples_split`: Decrease the minimum number of samples required to split a node.

3. Moderate Train Accuracy, Moderate Test Accuracy (Balanced but Low Performance)
- Objective: Fine-tune the model for better performance.
- Parameters to Adjust:
	- `max_features`: Experiment with different numbers of features.
	- `max_depth`: Adjust the depth of trees.
	- `n_estimators`: Fine-tune the number of trees.
	- `min_samples_split`: Adjust the minimum samples for splitting.

4. High Train Accuracy, High Test Accuracy (Optimal)
- Objective: Make minor adjustments for incremental improvements.
- Parameters to Adjust:
	- `n_estimators`: Slightly adjust the number of trees.
	- `max_features`: Fine-tune the number of features.
	- `min_samples_split`: Make small adjustments to the minimum samples for splitting.

### Links

See [[ML_Tools]]: [[Hyperparameter_tuning_GridSearchCV.py]]

Hyperparameter_tuning_RF.py
Video link: https://youtu.be/jUxhUgkKAjE?list=PLtqF5YXg7GLltQSLKSTnwCcHqTZASedbO&t=765
