---
aliases: []
category: ML
date modified: 27-09-2025
tags:
  - explainability
  - statistics
  - time_series
---
Seasonal ARIMA (SARIMA) extends the standard ARIMA model by incorporating seasonal components.
It is expressed as:

$$\text{SARIMA}(p, d, q)(P, D, Q)_s$$
### Components

#### Non-seasonal part $(p, d, q)$

(See [[ARIMA]] for details.)

#### Seasonal part $(P, D, Q)_s$

These terms allow ARIMA to model repeating seasonal patterns. 

The parameter $s$ denotes the seasonal period, how often the pattern repeats (e.g., $s=12$ for monthly data with yearly seasonality).

* $P$ - Seasonal Autoregressive Order
  Analogous to $p$, but applies to seasonal lags.
  Example: If $P=1$ and $s=12$, the model uses $y_{t-12}$ (the value from one year ago) to predict $y_t$.

* $D$ - Seasonal Differencing Order
  The number of times seasonal differencing is applied to remove seasonal trends.
  Example: $D=1$ with $s=12$ applies $y_t - y_{t-12}$.

* $Q$ - Seasonal Moving Average Order
  Analogous to $q$, but incorporates forecast errors from seasonal lags.
  Example: $Q=1$ and $s=12$ uses the forecast error from 12 months prior.

### How SARIMA Works

1. Seasonal differencing ($D > 0$)
   * Remove repeating seasonal patterns to stabilize the mean.
   $$y'_t = y_t - y_{t-s}$$

2. Non-seasonal differencing ($d > 0$)
   * Remove overall trends to make the series stationary.

3. Fit ARMA components

   * Non-seasonal AR ($p$) and MA ($q$) capture short-term dependencies.
   * Seasonal AR ($P$) and MA ($Q$) capture longer-term dependencies at seasonal lags.

2. Combine predictions
   The final forecast combines seasonal and non-seasonal components.

### Determining Parameters

Refer to:
[Tsang, G. (2020). *A semi-auto way to determine parameters for SARIMA models*](https://tsanggeorge.medium.com/a-semi-auto-way-to-determine-parameters-for-sarima-model-74cdee853080)

### Practical Notes

* SARIMA is conceptually similar to Holt–Winters exponential smoothing, but relies on more formal statistical assumptions.
* Before estimating $P$ and $Q$, ensure the series is seasonally stationary by applying seasonal [[Differencing in Time Series|Differencing]] if required ($D>0$).

### Identifying Seasonal Orders with [[ACF Plots|ACF]] and [[PACF Plots]]

To choose $Q$ (Seasonal MA order):
  * Examine the ACF plot for significant autocorrelations at seasonal lags (multiples of $s$).
  * A sharp cut-off at a seasonal lag suggests the appropriate $Q$.

To choose $P$ (Seasonal AR order):
  * Examine the PACF plot for significant spikes at seasonal lags.
  * A sharp cut-off indicates the seasonal AR order $P$.

### Related

* [[AIC in Model Evaluation]]
* [[Evolving Seasonality]]
* [[Differencing in Time Series]]
