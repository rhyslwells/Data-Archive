---
type: term
tags:
  - "#evaluation"
  - ml
---
## Description 


**What it is:**

- A technique used in machine learning and statistics to evaluate the performance of a predictive model.
- ==It involves dividing the dataset into k equal-sized subsets (called "folds") and using each fold as a validation set once, while the remaining k-1 folds are used for training.==
- The model's performance is averaged across all k folds to provide a more robust estimate of its generalization performance.

**Advantages:**

- **Reduced bias:** More reliable performance estimate compared to using a single validation set.
- **More efficient use of data:** All data is used for both training and validation.
- **Helps prevent overfitting:** By evaluating on multiple folds, it can detect if the model is [[overfitting]] to the training data.
- **Aids in model selection and [[hyperparameter]] tuning:** Helps choose the best model and tune its parameters.

**Common variations:**

- **Stratified k-fold:** Ensures each fold has a similar proportion of class labels (important for imbalanced datasets).
- **Repeated k-fold:** Repeats the process multiple times with different random splits for more robust results.

**Choosing k:**

- Common values: 5 or 10
- Higher k leads to more accurate estimates but increases computation time.
- Consider dataset size and complexity when choosing k.

## Implementation:


```python
from sklearn.model_selection import cross_val_score
cross_val_score(model,X_train, y_train, cv=5)
```

 Implement k-fold cross-validation on a dataset and use it to train and evaluate a machine learning model. 
 ?
```python
  import pandas as pd
      from sklearn.model_selection import cross_val_score
      from sklearn.linear_model import LinearRegression
      # create a dataframe with sample data
      data = {'X1':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'X2':[11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
              'X3':[21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 'y':[31, 32, 33, 34, 35, 36, 37, 38, 39, 40]}
      df = pd.DataFrame(data) 
      # split the data into training and test sets
      X = df.drop('y', axis=1)
      y = df['y']
      # create a linear regression model
      model = LinearRegression()
      # perform k-fold cross-validation
      scores = cross_val_score(model, X, y, cv=5)
      # print the scores
      print(scores)
      # print the mean score
      print(scores.mean())
```
    
## [[Model Evaluation]] with cross-validation

If close to 1 (average 0.96) then, the model appears to perform consistently well across most folds, with an average accuracy of approximately 96%

```python
from sklearn.model_selection import cross_val_score
model_2 = RandomForestClassifier(n_estimators=10) #<-from random forest
# Perform cross-validation
cv_scores = cross_val_score(model_2, X, y, cv=5)  # Use 5-fold cross-validation

# Print cross-validation scores
print("Cross-Validation Scores:", cv_scores)
print("Mean CV Score:", cv_scores.mean())
```

## Questions and answers


What is [[Cross validation]];; a technique used to assess the performance of a model by splitting the data into multiple subsets for training and testing.