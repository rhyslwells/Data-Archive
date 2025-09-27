---
aliases: []
category: DS
date modified: 27-09-2025
tags:
- time_series
---
A **lag value** is simply the value of a series at a previous time step, used as a feature for the current prediction. For example, at time $t$, the feature $y_{t-1}$ is the lagged value from the previous step.

Lags capture short-term dependencies in a series and are especially useful for models such as [[Random Forest for Time Series]].

### Why use lags?

* They help the model learn relationships from recent history.
* Useful when modeling [[Seasonality in Time Series]], since repeating patterns often depend on past values.
* Performance can be compared by looking at [[Evaluation Metrics]] with and without lag features.

### Limitations of Lags

While lags can boost short-horizon forecasts, they can cause problems in **longer-term forecasting**:

* At some point, the model no longer has real lag values to use as inputs—it must rely on its own **predicted values**.
* This creates **error propagation**: each prediction carries uncertainty, which compounds with each additional step.

Example:
* At time $t$, $y_{t-1}=5$, model predicts $y_t=6$.
* At $t+1$, the model must use **6 (a prediction)** as input, leading to more uncertainty.
* If it predicts $8$ at $t+1$, the forecast for $t+2$ is based on $8$ (itself dependent on $6$), compounding the error.

This recursive process means performance usually **degrades with horizon length**.

### Beyond Lags

To reduce over-reliance on lagged features, it’s often useful to add **other numerical or categorical predictors**, such as:

* Calendar features (holiday flags, weekday vs weekend, month/season indicators).
* External variables (e.g., temperature, promotions, economic indicators).

These features can help the model generalize better and reduce error accumulation over time.

Resources:
* [How to Forecast Time Series Using Lags](https://towardsdatascience.com/how-to-forecast-time-series-using-lags-5876e3f7f473/)
