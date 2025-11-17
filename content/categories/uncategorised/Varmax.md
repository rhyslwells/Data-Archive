---
aliases: []
category: DS
date modified: 9-11-2025
tags:
  - analysis
  - statistics
  - time_series
---
A **VARMAX** model (Vector Autoregressive Moving Average with [[Exogenous Regressors]]) is a multivariate time-series model extending two classical ideas:

1. **VAR($p$)**: Models interactions among multiple endogenous series using autoregressive lags.
2. **VMA($q$)**: Captures correlations in multivariate residuals using moving-average terms.
3. **X**: Allows the inclusion of exogenous predictors.

Formally, a $k$-dimensional VARMAX($p$, $q$) for endogenous vector $y_t$ and exogenous predictors $x_t$ can be written as:

$y_t = c + \sum_{i=1}^{p} A_i y_{t-i} + \sum_{j=1}^{q} M_j \varepsilon_{t-j} + B x_t + \varepsilon_t$

Where:

* $y_t$: vector of endogenous variables
* $A_i$: autoregressive coefficient matrices
* $M_j$: moving-average coefficient matrices
* $B$: matrix of coefficients for exogenous variables
* $\varepsilon_t$: error terms (possibly correlated across series)

[[Statsmodels]] implements this within the statespace framework, giving access to [[Kalman filtering]], smoothing, and forecast intervals.

[[Multivariate Analysis]]

## How VARMAX is used

### 1. **Multivariate forecasting**

Useful when several time-dependent variables influence each other.
Examples:

* Forecasting $[ \text{demand}, \text{price} ]$ together
* Forecasting multiple KPIs: $[\text{revenue}, \text{users},\text{conversion}]$

Because the model estimates cross-lag impacts, you obtain richer dynamics than running separate univariate models.

### 2. **Understanding cross-relationships**

You can quantify how a change in one variable affects others over future periods.
Common analyses include:

* Impulse-response functions
* Forecast error variance decomposition

### 3. **Including external drivers**

Exogenous regressors allow structured drivers to influence all series.

Examples:

* $x_t$: temperature affecting energy demand and cost
* $x_t$: marketing spend affecting multiple product KPIs

### 4. **Scenario analysis**

Once fitted, you can simulate future paths under different exogenous scenarios.

## Example usage in Statsmodels

```python
import pandas as pd
from statsmodels.tsa.statespace.varmax import VARMAX

# Assume df contains:
#   'revenue', 'customers', plus exogenous column 'marketing_spend'
endog = df[['revenue', 'customers']]
exog = df[['marketing_spend']]

model = VARMAX(endog, exog=exog, order=(2, 1))
fit = model.fit(disp=False)

# Forecast 12 periods ahead
forecast = fit.get_forecast(steps=12, exog=future_exog)
forecast_df = forecast.predicted_mean
```

## When to consider VARMAX

Choose VARMAX when:

* Your variables interact across time.
* Residuals show multivariate [[autocorrelation]].
* You need forecasts that account for cross-effects.
* You need to incorporate exogenous drivers.

Avoid it when:

* You want a purely univariate model (consider ARIMA/ETS).
* You have very short [[time series]] (many parameters).
* You need nonlinear or regime-switching dynamics (consider deep learning or structural models).
