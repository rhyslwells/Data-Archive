---
aliases: []
category: ML
date modified: 27-09-2025
tags:
- explainability
- statistics
---
`f_regression` is a statistical method provided by `sklearn.feature_selection` to evaluate the linear relationship between each independent variable in X and a continuous target variable y. It is a univariate [[Feature Selection]] method based on the [[F-statistic]] from simple linear regression.

Specifically:

* For each feature, `f_regression` fits a simple [[Linear Regression]] model (i.e. one feature at a time).
* It computes:
  * The F-statistic, which tests whether there is a linear relationship between the feature and the target.
  * The corresponding p-value, which helps assess the statistical significance of that relationship.

### Statistical Assumptions
* The relationship between each feature and the target is assumed to be linear.
* Errors are assumed to be normally distributed with constant variance.
* Features are assessed independently — mutual influence or [[Multicollinearity]] is ignored.

### Limitations

* `f_regression` does not account for feature interactions or joint effects.
* It cannot capture non-linear dependencies.
* It is not applicable to models outside the linear regression framework (e.g., tree-based models or SVMs).

## When to Use `f_regression`

Use `f_regression` when:

* You're performing linear regression and want to evaluate individual feature relevance.
* You want a fast, interpretable [[Filter Methods]] for selecting features before training.
* You assume no or limited multicollinearity between features.

Do not use `f_regression` when:

* Your model is non-linear or [[non-parametric]].
* Feature interactions are essential to the model’s behavior.
* You're working with [[Classification]] tasks — instead, use `f_classif`.

## Example: Computing P-values with `f_regression`

```python
from sklearn.feature_selection import f_regression

# Compute F-statistics and p-values
f_stats, p_values = f_regression(X, y)

print(p_values)
```

Example Output:

```python
(array([56.04804786, 0.17558437]), array([7.19951844e-11, 6.76291372e-01]))
```

* Feature 1 is statistically significant (very small p-value).
* Feature 2 is not statistically significant.

Documentation:
[scikit-learn f\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html)
