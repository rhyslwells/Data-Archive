---
tags:
  - classifer
  - drafting
---

# Hyperparamaters tuning 

Max-features and n-estimaters, use Cv grid seearch . 

https://youtu.be/jUxhUgkKAjE?list=PLtqF5YXg7GLltQSLKSTnwCcHqTZASedbO&t=765


```python
# **4. Hyperparameter Tuning**

Now we will be performing the tuning of hyperparameters of Random forest model. The hyperparameters that we will tune includes **max_features** and the **n_estimators**.

Note: Some codes modified from [scikit-learn](http://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html)

Firstly, we will import the necessary modules.

The **GridSearchCV()** function from scikit-learn will be used to perform the hyperparameter tuning. Particularly, **GridSearchCV()** function can perform the typical functions of a classifier such as _**fit**_, _**score**_ and _**predict**_ as well as _**predict_proba**_, _**decision_function**_, _**transform**_ and _**inverse_transform**_.

Secondly, we define variables that are necessary input to the GridSearchCV() function.

In [0]:

from sklearn.model_selection import GridSearchCV
import numpy as np

max_features_range = np.arange(1,6,1)
n_estimators_range = np.arange(10,210,10)
param_grid = dict(max_features=max_features_range, n_estimators=n_estimators_range)

rf = RandomForestClassifier()

grid = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5)
```

Can them view the 2d hyper parameter space.


# Statquest notes:

[link](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ)  part 1

What is an issue with [[Random Forests]];; susceptible to overfitting, especially when dealing with noisy or high-dimensional data. Proper tuning of hyperparameters like the number of trees and maximum depth is crucial to mitigate this.

[[Decision Tree]] are not the best - need to make flexible for new data. THey work well with the data set they are defined on.

How to proceed with random forest: (build tree's randomly) i.e solve the issue with decision trees. Processis called [[Bagging]]
1) randomly select a dataset (bootstrap)
2) randomly select two (or multiple) features for each branch and proceed like in decision tree.

variety makes trees better.

To make a prediction , run data through trees in forest, and get prediction, conclude with majority prediciton.

How to know if random forest is good ?

Use data that was not in boot strap data set - measure the accuracy based on these classiifcations.

Refine the random forest by qweaking the [[Hyperparameter]] of number of features used per step.

---
missing data

make initial guess for missing data and refine. Use [[Data Cleansing]]. Remember where missing data was.


[link part 2](https://www.youtube.com/watch?v=sQ870aTKqiM)

[[Proximity matrix]] [[Data Cleansing]]

![[Pasted image 20240411095614.png|500]]


# Description:
A random forest is an [[Model Ensembling]] of [[Decision Tree]]s. Take many decision trees decisions to get better result.

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

Train the RandomForestClassifier on a dataset and evaluate it with [[Cross Validation]].

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

What is an issue with [[Random Forests]];; susceptible to overfitting, especially when dealing with noisy or high-dimensional data. Proper tuning of hyperparameters like the number of trees and maximum depth is crucial to mitigate this.

Random forests combine multiple decision trees to improve accuracy and generalisation.

**What is Random Forest, and how does it work?**;; Random Forest is an method that can perform regression, classification, dimensionality reduction, and handle missing values. It builds multiple decision trees and combines their outputs. Each tree is grown using a subset of the data and features, and the final output is determined by aggregating the predictions of individual trees.