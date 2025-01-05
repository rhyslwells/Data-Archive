Optuna is a [[Hyperparameter]] optimization framework used to automatically tune hyperparameters for machine learning models. 

## Steps to Use Optuna
1. **Define Objective Functions**: 
   - For each model (LightGBM, XGBoost, CatBoost), define an objective function.
   - The objective function takes trial parameters as input and returns a score to optimize.
   - Specify hyperparameters to tune within each function, such as learning rate, number of leaves (for LightGBM), eta, max depth (for [[XGBoost]]), and learning rate, depth (for [[CatBoost]]).

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

# [[Optuna]]

### In summary:
- Optuna automates the process of tuning the hyperparameters of a machine learning model. It does this by defining an objective function where different combinations of hyperparameters are tested, training the model, and evaluating its performance.
- The best set of hyperparameters is chosen based on the performance metric (test accuracy in this case) returned by the objective function.
### Benefits of Using Optuna:

1. Efficient Search: Optuna uses algorithms like TPE (Tree-structured Parzen Estimator) to search the hyperparameter space more efficiently than grid search.
2. Dynamic Search Space: Optuna can search across continuous, categorical, and discrete spaces.
3. Automatic Pruning: Optuna supports pruning of unpromising trials during training, improving computational efficiency.
4. Visualization: Optuna provides built-in tools for visualizing the optimization process, making it easier to understand the impact of hyperparameters.

Optuna is an automatic hyperparameter optimization library that helps you find the best hyperparameters for your machine learning model. Here's a simplified breakdown of what Optuna is doing in the provided code:

### 1. Creating an Optimization Study:
```python
study = optuna.create_study(direction='maximize')
```
- Optuna begins by creating a study. The study is essentially the container for tracking and managing the optimization process. 
- The `direction='maximize'` tells Optuna to maximize the output of the objective function. In this case, the objective is to maximize the model's test accuracy.

### 2. Defining the Objective Function:
```python
def objective(trial):
```
- Objective function: This is the function that Optuna will optimize. It defines the model, how it's trained, and how its performance is evaluated.
- The goal of the objective function is to return a score (test accuracy in this case), which Optuna will use to decide if the current trial is successful.

### 3. Suggesting Hyperparameters:
Inside the objective function, Optuna suggests values for the model's hyperparameters by using different `trial.suggest_*` methods:
```python
learning_rate = trial.suggest_loguniform('learning_rate', 1e-5, 1e-2)
batch_size = trial.suggest_categorical('batch_size', [32, 64, 128])
dropout = trial.suggest_uniform('dropout', 0.2, 0.5)
units_1 = trial.suggest_int('units_1', 64, 128)
```
- Hyperparameters: These are the settings for the model that you want Optuna to optimize, such as the learning rate, batch size, and dropout rate.
- `trial.suggest_*` methods: These methods tell Optuna what types of values to explore for each hyperparameter (e.g., log-uniform for learning rate, categorical for batch size, etc.).
  
### 4. Training the Model:
```python
model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=config['epochs'], batch_size=config['batch_size'], callbacks=[...])
```
- Optuna uses the suggested hyperparameters to build and train a Keras model. The model is trained using the `fit()` function with the hyperparameters defined earlier.
- The goal is to evaluate the model's test accuracy to decide whether this set of hyperparameters is good.

### 5. Returning the Result:
```python
return test_accuracy
```
- After training, the model's test accuracy is returned as the result of the trial.
- Optuna uses this score to evaluate how well this set of hyperparameters performed.

### 6. Optimization:
```python
study.optimize(objective, n_trials=15)
```
- This line starts the optimization process.
- Optuna runs the `objective` function multiple times (in this case, 15 times). Each time, it tries different hyperparameter combinations.
- It uses the result (test accuracy) to decide which hyperparameters are performing best.

### 7. Best Trial:
```python
best_trial = study.best_trial
```
- After all trials, Optuna identifies the best trial, which is the trial with the highest test accuracy.
- The hyperparameters that led to this best performance are stored in `best_trial.params`.