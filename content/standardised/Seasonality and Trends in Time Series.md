---
aliases: []
category:
date modified: 3-09-2025
tags:
  - analysis
  - statistics
  - time_series
---
To handle seasonality and trends in time series, you usually need to ==make the data stationary== ([[Stationary Time Series]]) (constant mean and variance).

### Trends (long-term upward or downward movement)

* Differencing: Subtract the previous value from the current value:
  $$y'_t = y_t - y_{t-1}$$
  Removes linear trends. Can apply higher-order differencing if needed.
* Detrending with regression: Fit a line or curve to the data and use residuals.
* Transformation: [[Log transformation]] or square root to stabilize growth rates.

### Seasonality (repeating patterns over fixed periods)

* Seasonal differencing: Subtract the value from the same season in the past:
  $y'_t = y_t - y_{t-s}$
  where $s$ = seasonal period (e.g., 12 for monthly data with yearly seasonality).
* Decomposition methods:

  * Additive: $y_t = T_t + S_t + R_t$
  * Multiplicative: $y_t = T_t \times S_t \times R_t$
    Use STL (Seasonal-Trend decomposition) or classical decomposition to separate and model components.
* Seasonal dummy variables: Add month/quarter indicators as features (especially for machine learning models).

### Combined Trend + Seasonality

* Apply seasonal differencing + regular differencing if both are present (this is what [[SARIMA]] does).
* For machine learning approaches (e.g., [[Random Forest]], [[XGBoost]]), create lagged features, rolling averages, and seasonal indicators.

### Practical considerations

* Check stationarity: Use plots, ACF/PACF, or statistical tests (ADF test).
* Avoid over-differencing: Too many differences can destroy useful structure.
* Model choice:
  * Classical: [[SARIMA]], [[Exponential Smoothing Forecasting]]
  * Decomposition + ML: [[Random Forest for Time Series]], Gradient Boosting
