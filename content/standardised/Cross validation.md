---
type: 
tags:
  - "#evaluation"
---
Cross-validation is a statistical technique used in machine learning to ==assess how well a model will generalize== to an independent dataset. It is a crucial step in the model-building process because it helps ensure that the model is not [[overfitting]] or underfitting the training data.

- Cross-validation is a technique used in machine learning and statistics to evaluate the performance ([[Model Optimisation]]) of a predictive model.
- It provides a robust evaluation by splitting the training data into smaller chunks and training the model multiple times.
- K-Fold Cross-Validation: Involves dividing the dataset into \( k \) equal-sized subsets (called "folds") and using each fold as a validation set once, while the remaining \( k-1 \) folds are used for training.
- The model's performance is averaged across all \( k \) folds to provide a more robust estimate of its generalization performance.
### Common Variations

- K-Fold Cross-Validation: The most common method, where the data is split into \( k \) folds and the model is trained \( k \) times, each time using a different fold as the validation set.
- Stratified K-Fold: Ensures each fold has a similar proportion of class labels, important for imbalanced datasets.
- Repeated K-Fold: Repeats the process multiple times with different random splits for more robust results.
- Leave-One-Out Cross-Validation (LOOCV): Each data point is used once as a test set while the rest serve as the training set.

### How Cross-Validation Fits into Building a Machine Learning Model

1. [[Model Evaluation]]: Used to evaluate the performance of different models or algorithms to choose the best one.
2. [[Hyperparameter]] Tuning: Provides a reliable performance metric for each set of hyperparameters.
3. [[Model Validation]]: Ensures consistent performance across different subsets of data.
4. [[Bias and variance]] tradeoff: Helps in understanding the tradeoff between bias and variance, guiding the choice of model complexity.

Advantages:

- Reduced Bias: Offers a more reliable performance estimate compared to using a single validation set.
- Efficient Data Use: All data is used for both training and validation.
- Prevents Overfitting: By evaluating on multiple folds, it can detect if the model is overfitting to the training data.
### Choosing \( k \)

- Common values: 5 or 10
- Higher \( k \) leads to more accurate estimates but increases computation time.
- Consider dataset size and complexity when choosing \( k \).

### Code Implementation

```python
from sklearn.model_selection import cross_val_score
cross_val_score(model, X_train, y_train, cv=5)
```

Implement k-fold cross-validation on a dataset and use it to train and evaluate a machine learning model:

```python
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

# Create a dataframe with sample data
data = {'X1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'X2': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        'X3': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        'y': [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]}
df = pd.DataFrame(data)

# Split the data into features and target
X = df.drop('y', axis=1)
y = df['y']

# Create a linear regression model
model = LinearRegression()

# Perform k-fold cross-validation
scores = cross_val_score(model, X, y, cv=5)

# Print the scores
print(scores)
print("Mean Score:", scores.mean())
```

If the mean score is close to 1 (e.g., 0.96), the model appears to perform consistently well across most folds, with an average accuracy of approximately 96%.

```python
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

model_2 = RandomForestClassifier(n_estimators=10)

# Perform cross-validation
cv_scores = cross_val_score(model_2, X, y, cv=5)

# Print cross-validation scores
print("Cross-Validation Scores:", cv_scores)
print("Mean CV Score:", cv_scores.mean())
```


## [[Cross Validation]]
#### Cross-Validation Strategy in [[TimeSeries]]

All notebooks use cross-validation based on `TimeSeriesSplit` to ensure proper evaluation of performance with no [[Data Leakage]]. This method ensures that training and test data are split while maintaining the chronological order of the data.