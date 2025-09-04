---
aliases: []
category:
date modified: 1-08-2025
tags:
  - modeling
  - time_series
---
ARIMA (AutoRegressive Integrated Moving Average) is a popular method for [[Time Series Forecasting]] that models the autocorrelations within the data. It is particularly useful for datasets with trends and patterns that are not seasonal.

### ARIMA Explained

ARIMA stands for:
- AutoRegressive (AR): Uses past values to predict the current one.
- Integrated (I): Differencing to make the series stationary.
- MAving Average (MA): Uses past forecast errors for prediction.

A typical ARIMA(p,d,q) model has:

- $p$: Number of lagged values (AR terms)
- $d$: Number of differences needed to make the series stationary
- $q$: Number of lagged forecast errors (MA terms)

#### What ARIMA Does:

1. Checks for stationarity – if not, applies differencing ($d$ times).
2. Models relationships between current values and:
   - Past values (AR part)
   - Past errors (MA part)
1. Fits parameters by minimizing a loss (typically log-likelihood).
2. Forecasts future values using this learned structure.
### Why ARIMA Isn’t Enough for Seasonal Data

Data might show repeating patterns every 4 quarters (seasonality), and ARIMA has no built-in mechanism to model this periodic structure. This is where [[SARIMA]] comes in.

### Summary

| Model   | Handles Trend | Handles Seasonality | Use When...                                   |
|---------|---------------|---------------------|------------------------------------------------|
| ARIMA   | ✅            | ❌                  | Data has trend, but no regular cycles         |
| SARIMA  | ✅            | ✅                  | Data has both trend and seasonality           |

### Related terms

In [[ML_Tools]] see:
- https://github.com/rhyslwells/ML_Tools/blob/main/Explorations/Build/TimeSeries/ARIMA.ipynb
- [[Forecasting_AutoArima.py]]
- [[pmdarima]]
- [[ARIMA vs Random Forest in Time Series]]