---
aliases: []
category:
date modified: 26-08-2025
tags: [explainability, ml, statistics]
---
SARIMA extends ARIMA by adding seasonal components. It is written as: $$\text{SARIMA}(p, d, q)(P, D, Q)_s$$

Non-Seasonal ARIMA Part $(p, d, q)$ see [[ARIMA]]

Seasonal Part $(P, D, Q)_s$

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
### Related:
- [[AIC in Model Evaluation]]
- [[Evolving Seasonality]]
- [[Differencing in Time Series]]

### Determining parameters

https://tsanggeorge.medium.com/a-semi-auto-way-to-determine-parameters-for-sarima-model-74cdee853080

### Notes

- Alternatively, **SARIMA** is conceptually similar to Holt-Winters but with more statistical rigor, so they can be compared side by side.