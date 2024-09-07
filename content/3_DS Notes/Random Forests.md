---
tags:
  - ml
  - classifer
  - learning
  - focus
---

# Statquest notes:

[link](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ)  part 1



[[Decision Tree]] are not the best - need to make flexible for new data. THey work well with the data set they are defined on.

How to proceed with random forest: (build tree's randomly) i.e solve the issue with decision trees. Processis called [[Bagging]]
1) randomly select a dataset (bootstrap)
2) randomly select two (or multiple) features for each branch and proceed like in decision tree.

variety makes trees better.

To make a prediction , run data through trees in forest, and get prediction, conclude with majority prediciton.

How to know if random forest is good ?

Use data that was not in boot strap data set - measure the accuracy based on these classiifcations.

Refine the random forest by qweaking the [[hyperparameter]] of number of features used per step.

---
missing data

make initial guess for missing data and refine. Use [[Imputation]]. Remember where missing data was.


[link part 2](https://www.youtube.com/watch?v=sQ870aTKqiM)

[[Proximity matrix]] [[Finding missing data]]

![[Pasted image 20240411095614.png|500]]


# Description:
A random forest is an [[Ensemble model]] of [[Decision Tree]]s. Take many decision trees decisions to get better result.

![[Pasted image 20240128194716.png|500]]
![[Pasted image 20240118145117.png|500]]
# Applications

Apply the random forest regressor a dataset. Then evaluate the model performance with the R-squared metric [[R squared]]

```python
import numpy as np
    import pandas as pd
    from sklearn.datasets import fetch_california_housing
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import r2_score

    np.random.seed(1234)
    # load dataset
    ds = fetch_california_housing()
    df = pd.DataFrame(ds['data'], columns = ds['feature_names'])
    df['target'] = ds['target']
    # dependent variables
    X = df.drop('target', axis=1)
    # independent variable
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestRegressor( n_estimators=100 )
    model.fit(X_train, y_train)
    model.score(X_test, y_test)
    y_pred = model.predict(X_test)
    r2_score(y_test, y_pred)
    # you should get 0.8049
```

Train the RandomForestClassifier on a dataset and evaluate it with [[Cross validation]].

```python
    import numpy as np
    import pandas as pd
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import cross_val_score
    np.random.seed(12)
    ds = load_iris()
    df = pd.DataFrame(ds.data, columns=ds.feature_names)
    df['target'] = pd.Series(ds.target)
    X = df.drop('target', axis=1)
    y = df['target']
    model = RandomForestClassifier()
    cross_val_score(model, X, y)
    # As result you should get array([0.96666667, 0.96666667, 0.93333333, 0.96666667, 1.])
```
## Questions and answers:

What is the difference between RandomForestClassifier and RandomForestRegressor?;; One predicts a categorical and the other a continuous outcome.

What is the Random Forest method;; an ensemble learning method based on constructing multiple decision trees during training and combining their predictions through averaging. Random Forests are flexibility, robustness, and ability to handle high-dimensional data, as well as their resistance to overfitting.