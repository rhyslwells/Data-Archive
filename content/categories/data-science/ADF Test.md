---
aliases: []
category: DS
date modified: 27-09-2025
tags: []
---
### Augmented Dickey-Fuller Test

- This is a statistical procedure to determine whether a time series is stationary or not. 
- We will discuss more details about the test in the next lectures.
- For now, that's what we need to know:
    1. **Null hypothesis:** $H_0$: the series is nonstationary.
    2. **Alternative hypothesis:** $H_A$: the series is stationary.
    3. 
Dickey-Fuller test for sationarity

This is the main idea behind the [Dickey-Fuller test](https://en.wikipedia.org/wiki/Dickey%E2%80%93Fuller_test) for stationarity of time series (testing the presence of a unit root). If we can get a stationary series from a non-stationary series using the first difference, we call those series integrated of order 1. The null hypothesis of the test is that the time series is non-stationary, which was rejected on the first three plots and finally accepted on the last one. We have to say that the first difference is not always enough to get a stationary series as the process might be integrated of order d, d > 1 (and have multiple unit roots). In such cases, the augmented Dickey-Fuller test is used, which checks multiple lags at once.

Notes:
-  The ADF test specifically looks for a *unit root* (more on this later on).
- A unit root indicates that shocks ([[Time Series Shocks]]) to the time series have a permanent effect
- The test's conclusion is about the *absence of a unit root*.
- [[Mean reverting]] - sinusoidal. 