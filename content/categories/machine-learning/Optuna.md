---
aliases:
- null
category: ML
date modified: 27-09-2025
tags:
- optimisation
---
Optuna is a [[Hyperparameter]] optimization framework used to automatically tune hyperparameters for machine learning models.

Optuna automates the process of tuning hyperparameters by defining an objective function, testing different hyperparameter combinations, training the model, and evaluating its performance. The best set of hyperparameters is chosen based on the performance metric (e.g., test accuracy) returned by the objective function.

[[Hyperparameter Tuning]]
## Benefits of Using Optuna

1. Efficient Search: Utilizes algorithms like TPE (Tree-structured Parzen Estimator) to search the hyperparameter space more efficiently than grid search.
2. Dynamic Search Space: Can explore continuous, categorical, and discrete spaces.
3. Automatic Pruning: Supports pruning of unpromising trials during training, improving computational efficiency.
4. Visualization: Offers built-in tools for visualizing the optimization process, aiding in understanding the impact of hyperparameters.

## Steps to Use Optuna

1. Define Objective Functions:
   - For each model (e.g., [[LightGBM]], [[XGBoost]], [[CatBoost]]), define an objective function.
   - The objective function takes trial parameters as input and returns a score to optimize.
   - Specify hyperparameters to tune within each function, such as:
     - LightGBM: learning rate, number of leaves
     - XGBoost: eta, max depth
     - CatBoost: learning rate, depth

2. Running Hyperparameter Optimization:
   - Create a study object for each model using `optuna.create_study()`.
   - Run the optimization process using the `.optimize()` method, specifying the objective function and the number of trials.
   - Retrieve the best hyperparameters from each study object using `.best_params`.

3. Comparison and Evaluation:
   - Compare the best hyperparameters obtained for each model.
   - Evaluate the performance of the tuned models on a validation dataset.

## Differences between Models with Optuna

Hyperparameters:
  - The specific hyperparameters to tune may vary between models.
  - Example: LightGBM involves tuning parameters like learning rate and number of leaves, while XGBoost involves parameters like eta and max depth.

Objective Function:
  - Tailor the objective function for each model to its respective API and requirements.
  - Ensure the objective function properly trains and evaluates the model using the specified hyperparameters.

Optimization Strategy:
  - Optuna provides different optimization algorithms (e.g., TPE, CMA-ES) that may behave differently depending on the model and hyperparameter space.
### Implementation

```python
import optuna

# 1. Creating an Optimization Study
# Initialize a study to track and manage the optimization process.
# The 'direction' parameter specifies whether to maximize or minimize the objective function.
study = optuna.create_study(direction='maximize')

# 2. Defining the Objective Function
def objective(trial):
    # 3. Suggesting Hyperparameters
    # Use trial.suggest_* methods to specify the hyperparameters to optimize.
    # Each method defines the type and range of values to explore.
    learning_rate = trial.suggest_loguniform('learning_rate', 1e-5, 1e-2)
    batch_size = trial.suggest_categorical('batch_size', [32, 64, 128])
    dropout = trial.suggest_uniform('dropout', 0.2, 0.5)
    units_1 = trial.suggest_int('units_1', 64, 128)
    
    # 4. Training the Model
    # Train the model using the suggested hyperparameters.
    # Evaluate the model's performance on the validation dataset.
    model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=config['epochs'], batch_size=batch_size, callbacks=[...])
    
    # Returning the Result
    # Return the model's test accuracy as the result of the trial.
    return test_accuracy

# Optimization
# Run the optimization process, executing the objective function multiple times.
# The 'n_trials' parameter specifies the number of trials to run.
study.optimize(objective, n_trials=15)

# Best Trial
# After optimization, retrieve the best trial with the highest test accuracy.
# The best hyperparameters are stored in 'best_trial.params'.
best_trial = study.best_trial
```