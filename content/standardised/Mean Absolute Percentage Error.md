---
aliases:
  - MAPE
category:
date modified: 12-09-2025
tags: []
---
MAPE is a metric for evaluating forecasting or regression models. It measures the **average absolute error between predicted and actual values**, expressed as a **percentage of the actual values**. This makes it intuitive for communicating model accuracy to stakeholders or management. Lower values indicate better model performance.

**Formula:**

$MAPE = \frac{100}{n}\sum\limits_{i=1}^{n} \frac{|y_i - \hat{y}_i|}{y_i}$

**Notes:**

* Useful for comparing errors across different scales.
* Sensitive to very small actual values, which can inflate the percentage error.

Related:
- [[Regression Metrics]]
- [[Mean Absolute Error]]

### MAPE vs RMSE

For an initial forecast model, use MAPE over RMSE because it provides a relative measure of error that's easy to interpret. By expressing errors as a percentage of actual values, MAPE is scale-independent and gives a intuitive sense of how far off forecasts are.

MAPE also treats all periods more evenly, while [[Root Mean Squared Error]] gives extra weight to large errors, which can skew evaluation if outliers or volatile periods exist.

MAPE provides a simple, easy-to-read overview of forecast accuracy on test data and helps guide improvements before moving on to more sensitive metrics like RMSE or MAE.