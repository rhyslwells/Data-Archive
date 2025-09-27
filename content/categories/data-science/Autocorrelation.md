---
aliases: []
category: DS
date modified: 27-09-2025
tags:
- statistics
- time_series
---
**Autocorrelation** (also called serial [[Correlation]]) measures how a time series is related to a lagged version of itself. Helps identify repeating patterns, seasonality, or persistence in data.

Formally, for a time series ${y_t}$, the autocorrelation at lag $k$ is:

$$
\rho_k = \frac{\text{Cov}(y_t, y_{t-k})}{\sqrt{\text{Var}(y_t)\,\text{Var}(y_{t-k})}}
$$

It takes values between $-1$ and $1$:

* $\rho_k > 0$: Positive correlation -> if $y_t$ is above its mean, $y_{t-k}$ tends to be above its mean too.
* $\rho_k < 0$: Negative correlation -> if $y_t$ is above its mean, $y_{t-k}$ tends to be below its mean.
* $\rho_k \approx 0$: No linear relationship between $y_t$ and its past at lag $k$.

### Intuition

Autocorrelation tells you ==how predictable a series is from its past==:
* Stock returns: low/no autocorrelation (mostly random).
* Daily temperatures: high autocorrelation at lag 1 (yesterday’s temperature is a good predictor of today’s).
* Strong seasonal effects: autocorrelation spikes at seasonal lags (e.g., 7 days for weekly seasonality).

### Why it matters
* Used to **detect [[Decomposition in Time Series]]** & [[Stationary Time Series]].
* Helps decide AR and MA terms in [[ARIMA]].
* Checked via **Autocorrelation Function (ACF)** and **Partial Autocorrelation Function (PACF)** plots ([[ACF Plots|ACF]], [[PACF Plots]]) to select lagged values.

### Hurst exponents
- The Hurst exponent ($H$) is a measure used to characterize the long-term memory of time series. 
- It helps to determine the presence of autocorrelation or persistence in the data. 
- The goal of the Hurst exponent is to provide us with a scalar value that will help us to identify whether a series is 
    - random walking,
    - trending,
    - [[Mean reverting]].

