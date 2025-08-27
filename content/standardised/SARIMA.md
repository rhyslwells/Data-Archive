---
aliases: []
category:
date modified: 26-08-2025
tags: [explainability, ml, statistics]
---
SARIMA extends ARIMA by adding seasonal components. It is written as: $$\text{SARIMA}(p, d, q)(P, D, Q)_s$$

### Non-Seasonal ARIMA Part $(p, d, q)$

These are the standard ARIMA components:

* $p$ – autoregressive (AR) order:
  The number of lagged observations included in the model. ==AR terms capture how past values influence current values.==
  Example: If $p=2$, the model uses the previous 2 time points to predict the current one.

* $d$ – differencing order:
  Number of times the data is differenced to make it stationary (remove trends).
  Example: $d=1$ means we model the difference: $y_t - y_{t-1}$.

* $q$ – moving average (MA) order:
  Number of lagged forecast errors in the prediction equation. MA terms capture short-term shocks or noise in the series.
  Example: $q=1$ means the model uses the previous time step’s error to adjust the prediction.

### Seasonal Part $(P, D, Q)_s$

These extend ARIMA to handle repeating seasonal patterns. Here, $s$ is the seasonal period (how often the pattern repeats, e.g., 12 for monthly yearly seasonality).

* $P$ – seasonal autoregressive order:
  Similar to $p$, but at the seasonal lag.
  Example: If $P=1$ and $s=12$, the model uses $y_{t-12}$ (value from one year ago) to predict $y_t$.

* $D$ – seasonal differencing order:
  Number of times seasonal differencing is applied. Removes seasonal trends.
  Example: $D=1$ with $s=12$: $y_t - y_{t-12}$.

* $Q$ – seasonal moving average order:
  Similar to $q$, but considers past seasonal forecast errors.
  Example: $Q=1$ and $s=12$ uses the error from 12 months ago.

### How SARIMA Works (Step by Step)

1. Seasonal differencing first (if $D>0$):
   Remove repeating seasonal trends to stabilize the mean.
   $y'_t = y_t - y_{t-s}$

2. Non-seasonal differencing (if $d>0$):
   Remove overall trend to make the series stationary.

3. Apply ARMA on transformed series:

   * Non-seasonal AR ($p$) and MA ($q$) model short-term dependencies.
   * Seasonal AR ($P$) and MA ($Q$) model dependencies at seasonal lags.

2. Combine predictions:
   The model combines seasonal and non-seasonal components to forecast the next time step.
### Example

$\text{SARIMA}(1,1,1)(1,1,1)_{12}$

* $p=1$: depends on previous value
* $d=1$: difference once to remove trend
* $q=1$: uses previous forecast error
* $P=1$: depends on value 12 months ago
* $D=1$: seasonal difference to remove annual seasonality
* $Q=1$: adjusts using error from 12 months ago
* $s=12$: yearly seasonality

This model is good for monthly data with annual seasonal cycles.

### Related:
- [[AIC in Model Evaluation]]