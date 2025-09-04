---
aliases: []
category:
date modified: 3-09-2025
tags:
  - probability
  - statistics
  - time_series
---
A **stationary time series** is one whose **statistical properties do not change over time**.

Formally, a time series ${y_t}$ is *stationary* if:

* The **mean** is constant: $E[y_t] = \mu$ for all $t$.
* The **variance** is constant: $\text{Var}(y_t) = \sigma^2$ for all $t$.
* The **autocovariance** depends only on the lag $k$, not on the specific time $t$:
  $\text{Cov}(y_t, y_{t+k}) = \gamma_k$

This means the process has the same behavior regardless of when you observe it.

### Types of stationarity

1. **Strict stationarity**: The entire distribution of the process is invariant to shifts in time (all moments remain constant).
2. **Weak (or covariance) stationarity**: Only the first two moments (mean, variance, covariance) are invariant. This weaker definition is often sufficient for models like [[ARIMA]].

### Examples

Stationary: White noise (mean = 0, variance constant).

Non-stationary:
  * Series with a **trend** (e.g., increasing sales over time).
  * Series with **changing variance** (e.g., volatility clustering in finance).
  * Series with **seasonality** (patterns repeating over time).

### Why it matters

Many classical time series models (e.g., [[ARIMA]], [[SARIMA]]) assume stationarity. Non-stationary data can lead to misleading results. Common [[Data Transformation]] to achieve stationarity include:

* **Differencing**: $y_t - y_{t-1}$
* [[Log transformation]] (to stabilize variance)
* **Detrending or deseasonalising**
