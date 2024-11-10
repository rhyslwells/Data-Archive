Optuna is a [[Hyperparameter]] optimization framework used to automatically tune hyperparameters for machine learning models. 

## Steps to Use Optuna
1. **Define Objective Functions**: 
   - For each model (LightGBM, XGBoost, CatBoost), define an objective function.
   - The objective function takes trial parameters as input and returns a score to optimize.
   - Specify hyperparameters to tune within each function, such as learning rate, number of leaves (for LightGBM), eta, max depth (for XGBoost), and learning rate, depth (for CatBoost).

2. **Running Hyperparameter Optimization**:
   - Create a study object for each model using `optuna.create_study()`.
   - Run the optimization process using `.optimize()` method, specifying the objective function and the number of trials.
   - Retrieve the best hyperparameters from each study object using `.best_params`.

3. **Comparison and Evaluation**:
   - Compare the best hyperparameters obtained for each model.
   - Evaluate the performance of the tuned models on a validation dataset.

## Differences between Models with Optuna

- **Hyperparameters**:
  - The specific hyperparameters to tune may vary between models.
  - For example, LightGBM may involve tuning parameters like learning rate and number of leaves, while XGBoost may involve parameters like eta and max depth.

- **Objective Function**:
  - The objective function for each model should be tailored to its respective API and requirements.
  - Ensure that the objective function properly trains and evaluates the model using the specified hyperparameters.

- **Optimization Strategy**:
  - Optuna provides different optimization algorithms (e.g., TPE, CMA-ES) that may behave differently depending on the model and hyperparameter space.
  - Experiment with different optimization strategies to find the most effective one for each model.