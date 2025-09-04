---
aliases: []
category:
date modified: 3-09-2025
tags: [statistics, time_series]
---
**Autocorrelation** (also called serial [[Correlation]]) measures how a time series is related to a lagged version of itself.

Formally, for a time series ${y_t}$, the autocorrelation at lag $k$ is:

$$
\rho_k = \frac{\text{Cov}(y_t, y_{t-k})}{\sqrt{\text{Var}(y_t)\,\text{Var}(y_{t-k})}}
$$

It takes values between $-1$ and $1$:

* $\rho_k > 0$: Positive correlation → if $y_t$ is above its mean, $y_{t-k}$ tends to be above its mean too.
* $\rho_k < 0$: Negative correlation → if $y_t$ is above its mean, $y_{t-k}$ tends to be below its mean.
* $\rho_k \approx 0$: No linear relationship between $y_t$ and its past at lag $k$.

### Intuition

Autocorrelation tells you ==how predictable a series is from its past==:

* Stock returns: low/no autocorrelation (mostly random).
* Daily temperatures: high autocorrelation at lag 1 (yesterday’s temperature is a good predictor of today’s).
* Strong seasonal effects: autocorrelation spikes at seasonal lags (e.g., 7 days for weekly seasonality).

### Why it matters

* Used to **detect [[Seasonality and Trends in Time Series]]**.
* Helps decide AR and MA terms in [[ARIMA]].
* Checked via **Autocorrelation Function (ACF)** and **Partial Autocorrelation Function (PACF)** plots.
