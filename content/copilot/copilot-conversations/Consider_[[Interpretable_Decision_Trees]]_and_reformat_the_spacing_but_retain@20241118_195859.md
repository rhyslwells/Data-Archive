---
epoch: 1731959939373
modelKey: gpt-4o|openai
tags:
  - copilot/copilot-conversation
---

**user**: Consider [[Interpretable Decision Trees]] and reformat the spacing but retain the content
[Timestamp: 2024/11/18 19:58:59]

**ai**: Here's the reformatted content with improved spacing while retaining the original content:

---

[[Interpretable Decision Trees]]:

# **Building Interpretable Decision Trees**

In this post, we explore how to build [Decision Trees](https://rhyslwells.github.io/Data-Archive/standardised/Decision-Tree) using a systematic and [interpretable](https://rhyslwells.github.io/Data-Archive/standardised/interpretability) approach. While we use the Titanic dataset for its simplicity and structure, the method and workflow we outline can be applied to many other datasets. You can also find the complete script for this walkthrough [here](https://github.com/rhyslwells/ML_Tools/blob/main/Classifiers/Decision_Tree/Interpretable_Decision_Tree/Decision_Tree_Interpretable.py).

## **1. The Dataset**

The Titanic dataset is a classic binary classification problem where the goal is to predict passenger survival (1 for survived, 0 for not survived). Before diving into the modeling process, we preprocess the data by:

- Encoding categorical variables (e.g., converting "Sex" into numeric values).
- Imputing missing values (e.g., filling missing "Age" values with the mean).

Here is a preview of the cleaned dataset after preprocessing:

| Row ID | Pclass | Age  | Fare    | Sex_male | SibSp | Parch | Survived |
| ------ | ------ | ---- | ------- | -------- | ----- | ----- | -------- |
| 0      | 3      | 22.0 | 7.2500  | 1        | 1     | 0     | 0        |
| 1      | 1      | 38.0 | 71.2833 | 0        | 1     | 0     | 1        |
| 2      | 3      | 26.0 | 7.9250  | 0        | 0     | 0     | 1        |
| 3      | 1      | 35.0 | 53.1000 | 0        | 1     | 0     | 1        |
| 4      | 3      | 35.0 | 8.0500  | 1        | 0     | 0     | 0        |

## **2. Hyperparameter Tuning with Grid Search**

To identify the best Decision Tree configuration, we use **GridSearchCV** ([link to reference](link)) to systematically tune key hyperparameters such as:

- `max_depth`: Controls the maximum depth of the tree.
- `min_samples_split`: The minimum number of samples required to split a node.
- `criterion` ([Gini](https://rhyslwells.github.io/Data-Archive/standardised/Gini-Impurity), [Entropy](https://rhyslwells.github.io/Data-Archive/standardised/Cross-Entropy)): The function to measure the quality of a split.

**Code Snippet: Performing Grid Search**

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

# Extract best parameters
best_params = grid_search.best_params_
print("Best Parameters:", best_params)
```

### Results of the Best Hyperparameters

| Parameter                | Value   |
|--------------------------|---------|
| `ccp_alpha`              | 0.0     |
| `class_weight`           | None    |
| `criterion`              | gini    |
| `max_depth`              | 3       |
| `max_features`           | None    |
| `max_leaf_nodes`         | None    |
| `min_impurity_decrease`  | 0.0     |
| `min_samples_leaf`       | 2       |
| `min_samples_split`      | 2       |
| `min_weight_fraction_leaf` | 0.0   |
| `random_state`           | 42      |
| `splitter`               | best    |

This ensures that the model is neither underfitting nor overfitting. Below is a visualization of the tuned Decision Tree model:

![[best_model.png]]

## **3. When and How to Perform Feature Selection**

Feature selection is crucial for simplifying the model and improving its interpretability. Depending on the workflow,
[Timestamp: 2024/11/18 19:59:18]