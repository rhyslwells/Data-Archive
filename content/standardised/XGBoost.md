---
aliases: [XGM]
category:
date modified: 27-07-2025
tags: [optimisation]
---
XGBoost (eXtreme Gradient Boosting) is a highly efficient and flexible implementation of [[Gradient Boosting]] that is widely used for its accuracy and performance in machine learning tasks.

### How does XGBoost work

It works by building an [[Model Ensemble]] - ensemble of decision trees, where each tree is trained to correct the errors made by the previous ones. Here's a breakdown of how XGBoost works:
### Key Concepts

1. Gradient Boosting Framework:
   - XGBoost is based on the gradient boosting framework, which builds models sequentially. Each new model aims to reduce the errors (residuals) of the combined ensemble of previous models.

2. Decision Trees:
   - XGBoost typically uses decision trees as the base learners. These trees are added one at a time, and existing trees in the model are not changed.

3. Objective Function:
   - The objective function in XGBoost consists of two parts: the loss function and a regularization term.
   - [[Loss function]]: Measures how well the model fits the training data. For regression, this might be [[mean squared error]]; for classification, it could be logistic loss.
   - [[Regularisation]]: Helps prevent overfitting by penalizing complex models. XGBoost supports both L1 (Lasso) and L2 (Ridge) regularization.

4. Additive Training:
   - XGBoost adds trees to the model sequentially. Each tree is trained to minimize the loss function, taking into account the errors made by the previous trees.

5. [[Gradient Descent]]
   - The model uses gradient descent to minimize the loss function. It calculates the gradient of the loss function with respect to the model's predictions and uses this information to update the model.

6. [[Learning Rate]] ($\eta$):
   - A parameter that scales the contribution of each tree. A smaller learning rate requires more trees but can lead to better performance.

7. Tree Pruning:
   - XGBoost uses a technique called "max depth" to control the complexity of the trees. It also employs a "max delta step" to ensure that the updates are not too aggressive.

8. [[Handling Missing Data]]
   - XGBoost can handle missing data internally by learning the best direction to take when a value is missing.

9. Parallel and Distributed Computing:
   - XGBoost is designed to be highly efficient and can leverage parallel and distributed computing to speed up training.

Key Features:
- Tree Splitting: Builds [[Decision Tree]] in a level-wise manner, leading to balanced trees and efficient computation.
- Parameters: Key parameters include `eta` (learning rate) and `max_depth` (maximum depth of a tree), which control the model's complexity and learning process.

### Workflow

1. Initialization:
   - Start with an initial prediction, often the mean of the target values for regression or a uniform probability for classification.

2. Iterative Training:
   - For each iteration, compute the gradient of the loss function with respect to the current predictions.
   - Fit a new decision tree to the negative gradient (residuals).
   - Update the model by adding the new tree, scaled by the learning rate.

3. Model Output:
   - The final model is a weighted sum of all the trees, where each tree contributes to the final prediction.

Advantages:
- Accuracy: Known for its high accuracy and robustness across various machine learning tasks.
- [[Regularisation]]: Supports L1 (Lasso) and L2 (Ridge) regularization to prevent overfitting.
- Flexibility: Offers a wide range of hyperparameters for fine-tuning models.

Use Cases:
- Structured Data: Particularly effective for structured data and tabular datasets.
- [[Interpretability]]: Suitable when model interpretability is important.
- [[Hyperparameter Tuning]]: Ideal for scenarios where extensive hyperparameter tuning is feasible.
### Implementing XGBoost in Python

#### Step 2: Import Necessary Libraries

```python
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
```
#### Step 3: Prepare Your Data

Split your dataset into training and testing sets:

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

#### Step 4: Convert Data to DMatrix

Convert the data into DMatrix, the optimized data structure used by XGBoost:

```python
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)
```

#### Step 5: Set Parameters

Define the parameters for the XGBoost model:

```python
params = {
    'max_depth': 6,
    'eta': 0.1,
    'objective': 'binary:logistic',  # Use 'reg:squarederror' for regression tasks
    'eval_metric': 'logloss'
}
```

#### Step 6: Train the Model

Train the XGBoost model using the training data:
```python
num_rounds = 100
bst = xgb.train(params, dtrain, num_rounds)
```

#### Step 7: Make Predictions and Evaluate
Make predictions on the test set and evaluate the model's performance:

```python
y_pred = bst.predict(dtest)
y_pred_binary = [1 if y > 0.5 else 0 for y in y_pred]
accuracy = accuracy_score(y_test, y_pred_binary)
print(f"Accuracy: {accuracy:.2f}")
```

# Notes

Set up an example of XGBoost. Plot the paramater space slices "Min_Samples_split", "Max_Depth" vs accuracy.

```python
xgb_model = XGBClassifier(n_estimators = 500, learning_rate = 0.1,verbosity = 1, random_state = RANDOM_STATE)
xgb_model.fit(X_train_fit,y_train_fit, eval_set = [(X_train_eval,y_train_eval)], early_stopping_rounds = 10)
xgb_model.best_itersation
```