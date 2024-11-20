# Building Interpretable Decision Trees

In this post, we explore how to build [Decision Trees](https://rhyslwells.github.io/Data-Archive/standardised/Decision-Tree) using an [interpretable](https://rhyslwells.github.io/Data-Archive/standardised/interpretability) approach. While we use the Titanic dataset for its simplicity and structure, the method and workflow we outline can be applied to many other datasets. You can also find the complete script for this walkthrough [here](https://github.com/rhyslwells/ML_Tools/blob/main/Classifiers/Decision_Tree/Interpretable_Decision_Tree/Decision_Tree_Interpretable.py).
## The Dataset

The Titanic dataset is a classic binary classification problem where the goal is to predict passenger survival (1 for survived, 0 for not survived). Before diving into the modeling process, we preprocess the data by:

- Encoding categorical variables (e.g., converting "Sex" into numeric values).
- Imputing missing values (e.g., filling missing "Age" values with the mean).

After [preprocessing](https://rhyslwells.github.io/Data-Archive/standardised/Data-Preprocessing), the dataset looks like this:

| Pclass | Age | Fare | Sex_male | SibSp | Parch | Survived |
| ------ | --- | ---- | -------- | ----- | ----- | -------- |
| 3      | 22  | 7    | 1        | 1     | 0     | 0        |
| 1      | 38  | 71   | 0        | 1     | 0     | 1        |
| 3      | 26  | 8    | 0        | 0     | 0     | 1        |
| 1      | 35  | 53   | 0        | 1     | 0     | 1        |
| 3      | 35  | 8    | 1        | 0     | 0     | 0        |
| ...    | ... | ...  | ...      | ...   | ...   | ...      |

## Hyperparameter Tuning with Grid Search

To identify the `Best` Decision Tree configuration, we use [GridSearchCV](https://rhyslwells.github.io/Data-Archive/standardised/GridSeachCv) to systematically tune key [hyperparameters](https://rhyslwells.github.io/Data-Archive/standardised/Hyperparameter) such as:

- `max_depth`: Controls the maximum depth of the tree.
- `min_samples_split`: The minimum number of samples required to split a node.
- `criterion` ([Gini](https://rhyslwells.github.io/Data-Archive/standardised/Gini-Impurity), [Entropy](https://rhyslwells.github.io/Data-Archive/standardised/Cross-Entropy)): The function to measure the quality of a split.

Here’s how we set up and run the grid search:
```python
# Define the parameter grid
param_grid = {
    'max_depth': [2, 3, 5, 7, 10, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'criterion': ['gini', 'entropy']
}

# Perform grid search
grid_search = GridSearchCV(DecisionTreeClassifier(random_state=42), param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)
```

The `Best` model from the grid search uses the following hyperparameters:

| Hyperparameter      | Value |
| ------------------- | ----- |
| `criterion`         | Gini  |
| `max_depth`         | 3     |
| `min_samples_leaf`  | 2     |
| `min_samples_split` | 2     |
| `random_state`      | 42    |

When evaluated using 5 fold [cross-validation](https://rhyslwells.github.io/Data-Archive/standardised/Cross-validation) - which we will do in every case when determining  [Classification Metrics](https://rhyslwells.github.io/Data-Archive/standardised/Classification-Metrics) - give an evaluation matrix of the form:

| Metric    | Mean   | Std    |
| --------- | ------ | ------ |
| Accuracy  | 0.8103 | 0.0121 |
| Precision | 0.7966 | 0.0185 |
| Recall    | 0.6812 | 0.0559 |
| F1 Score  | 0.7325 | 0.0302 |
| ROC AUC   | 0.8499 | 0.0273 |

Below is a visualization of the `Best` Decision Tree model:

![[best_model.png]]

One could argue that such a tree is to large to be understandable. So we will try reduce its complexity while retaining its predictive power.
## When and How to Perform Feature Selection

Feature selection improves interpretability by reducing the number of variables in the model. It also helps avoid overfitting. In this case, we’ll use **Recursive Feature Elimination (RFE)** to identify the most important features.

Depending on the workflow, it can be performed:

Before Pruning:
   - Reduces the input space early.
   - Leverages the full complexity of the model to determine feature importance.
   - Helps mitigate overfitting.
After Pruning:
   - Aligns with a simplified model.
   - Focuses on interpretability by prioritizing simplicity over raw performance.

Since the Titanic dataset is relatively small, and we aim to maintain predictive power, we perform feature selection before pruning.

### Using Recursive Feature Elimination (RFE) for Feature Selection

Recursive Feature Elimination (RFE) helps iteratively remove the least important features ([Feature Selection](https://rhyslwells.github.io/Data-Archive/standardised/Feature-Selection)). Here's how we applied RFE:

```python
from sklearn.feature_selection import RFE

# Apply RFE to the best model
rfe = RFE(estimator=best_model, n_features_to_select=3)
rfe.fit(X_train, y_train)

# Extract selected features
selected_features = [features[i] for i in range(len(features)) if rfe.support_[i]]
print("Selected Features:", selected_features)
```

The top three features are `Pclass, Age, Sex_male`. We will use this subset of the dataset for subsequent modelling steps. 

| Pclass | Age | Sex_male | Survived |
| ------ | --- | -------- | -------- |
| 3      | 22  | 1        | 0        |
| 1      | 38  | 0        | 1        |
| 3      | 26  | 0        | 1        |
| 1      | 35  | 0        | 1        |
| 3      | 35  | 1        | 0        |
| ...    | ... | ...      | ...      |
## Base Model

We can further simplify the model by increasing the size of the bins the values are partitioned into. Suppose we take this dataset with the following hyperparameters.

| Hyperparameter      | `Best` Value | `Base` Value |
| ------------------- | ------------ | ------------ |
| `criterion`         | Gini         | Gini         |
| `max_depth`         | 3            | 3            |
| `min_samples_leaf`  | 2            | 10           |
| `min_samples_split` | 2            | 4            |
| `random_state`      | 42           | 42           |

Recalculating the evaluation metrics we obtain arguable similar results, while simplifying the model complexity.

| Metric    | `Best` Mean | `Base` Mean | `Best` Std | `Base` Std |
| --------- | ----------- | ----------- | ---------- | ---------- |
| Accuracy  | 0.8103      | 0.7963      | 0.0121     | 0.0213     |
| Precision | 0.7966      | 0.7902      | 0.0185     | 0.0931     |
| Recall    | 0.6812      | 0.6493      | 0.0559     | 0.0837     |
| F1 Score  | 0.7325      | 0.7036      | 0.0302     | 0.0387     |
| ROC AUC   | 0.8499      | 0.8422      | 0.0273     | 0.0150     |

## Pruning the Decision Tree for Interpretability

Pruning trims unnecessary branches in the tree, simplifying its structure while maintaining performance. We used **cost-complexity pruning** to determine the optimal pruning threshold (`ccp_alpha`).

```python
# Get pruning path
ccp_path = base_interpretable_model.cost_complexity_pruning_path(X_train_rfe, y_train)
ccp_alphas = ccp_path.ccp_alphas
```

We evaluate the model for various `ccp_alpha` values using cross-validation on the feature-selected data. Below are the results:

| ID  | ccp_alpha | accuracy |
| --- | --------- | -------- |
| 1   | 0.000000  | 0.796297 |
| 2   | 0.000412  | 0.796297 |
| 3   | 0.003874  | 0.794888 |
| 4   | 0.004331  | 0.796297 |
| 5   | 0.009055  | 0.786467 |
| 6   | 0.015924  | 0.783650 |
| 7   | 0.038605  | 0.778046 |

We can be aggressive here (taking ccp_alpha = 0.015924) as pruning does not significantly reduce the accuracy in this case.  The result is the following pruned decision tree:

![[pruned.png]]

Finally let compare the evaluation metrics so far:

| Metric    | `Best` Mean | `Final` Mean | `Best` Std | `Final` Std |
| --------- | ----------- | ------------ | ---------- | ----------- |
| Accuracy  | 0.8103      | 0.7837       | 0.0121     | 0.0316      |
| Precision | 0.7966      | 0.8775       | 0.0185     | 0.1277      |
| Recall    | 0.6812      | 0.5338       | 0.0559     | 0.1077      |
| F1 Score  | 0.7325      | 0.6462       | 0.0302     | 0.0540      |
| ROC AUC   | 0.8499      | 0.8039       | 0.0273     | 0.0357      |

We can see that the pruned Decision Tree achieves a balance between interpretability and predictive performance. 
## Conclusion

We see that the pruned Base Model on a reduced dataset provides comparable performance with much more interpretable decision tree.

This workflow demonstrates that it’s possible to balance interpretability and prediction.
