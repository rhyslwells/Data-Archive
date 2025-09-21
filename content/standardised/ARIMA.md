---
aliases: []
category:
date modified: 1-08-2025
tags:
  - modeling
  - time_series
---
ARIMA (AutoRegressive Integrated Moving Average) is a widely used method for [[Time Series Forecasting]] that models the autocorrelations within the data. It is particularly effective for datasets with trends or patterns that are non-seasonal.

Requirement: [[Stationary Time Series]]
### ARIMA Explained

ARIMA consists of three components:

* AutoRegressive (AR): Uses past values to predict the current value.
* Integrated (I): Applies differencing to make the series stationary.
* Moving Average (MA): Uses past forecast errors to improve predictions.

The main ARIMA parameters are:
#### $p$ – Autoregressive (AR) Order

* Represents the number of lagged observations included in the model.
* Purpose: AR terms capture how past values influence the current value.
* Example: $p=2$ -> the model uses the previous 2 time points to predict the current one.
* How to pick $p$: Look at the Partial Autocorrelation Function ([[PACF Plots]]) plot:
  * The lag after which PACF cuts off (drops to near zero) suggests the `p` value.
  * Example: PACF is significant at lags 1 and 2, then drops -> `p = 2`.
#### $d$ – Differencing Order

* Represents the number of times the series is differenced ([[Differencing in Time Series]]) to achieve stationarity (removing trends).
* Example: $d=1$ -> model uses $y_t - y_{t-1}$.
* How to pick $d$:
  * Visual inspection: Check if the time series has a trend or changing mean.
  * [[ADF test]] (Augmented Dickey-Fuller): If p-value > 0.05 -> series is non-stationary -> increase $d$.
  * Rule of thumb: Usually $d ≤ 2$. Most series become stationary after 1–2 differences.
#### $q$ – Moving Average (MA) Order

* Represents the number of lagged forecast errors included in the model.
* Purpose: MA terms capture short-term shocks ([[Handling Time Series Shocks in the data]]) or noise.
* Example: $q=1$ -> model uses the previous time step’s error to adjust the prediction.
* How to pick $q$: Look at the [[Autocorrelation]] Function ([[ACF Plots|ACF]]) plot:
  * The lag after which ACF cuts off suggests the `q` value.
  * Example: ACF is significant at lag 1 -> `q = 1`.

### Fine-Tuning and Iterative Refinement

* Test several ARIMA models around initial `(p,d,q)` estimates.
* Evaluate using [[AIC in Model Evaluation]] BIC, or [[Cross Validation]] (lower values indicate a better model).
* Check residuals: They should resemble white noise (uncorrelated and zero mean).

### What ARIMA Does

1. Checks for stationarity and applies differencing ($d$ times) if needed.
2. Models the relationship between current values and:
   * Past values (AR component)
   * Past forecast errors (MA component)
3. Fits parameters by minimizing a loss function (typically log-likelihood).
4. Forecasts future values using the learned structure.
### Why ARIMA Isn’t Enough for Seasonal Data

ARIMA does not model repeating patterns (e.g., quarterly or monthly seasonality). For such cases, [[SARIMA]] is used.
### Related Resources

In [[ML_Tools]] see:
* [ARIMA Jupyter Notebook](https://github.com/rhyslwells/ML_Tools/blob/main/Explorations/Build/TimeSeries/ARIMA.ipynb)
* [[Forecasting_AutoArima.py]]
* [[pmdarima]]
* [[ARIMA vs Random Forest in Time Series]]
* [[SARIMA]]
