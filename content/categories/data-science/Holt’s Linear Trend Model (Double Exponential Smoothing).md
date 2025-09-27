---
aliases: []
category: DS
date modified: 27-09-2025
tags:
- forecasting
- ml
- time_series
---
Double Exponential Smoothing extends [[Simple Exponential Smoothing (SES)]] by introducing a **trend component** ([[Trends in Time Series]]), allowing it to capture both the *level* and the *trend* of a time series.

It is governed by two smoothing parameters:

* $\alpha$ : level smoothing
* $\beta$ : trend smoothing

**Update equations:**

* Level: $L_t = \alpha X_t + (1 - \alpha)(L_{t-1} + T_{t-1})$
* Trend: $T_t = \beta (L_t - L_{t-1}) + (1 - \beta) T_{t-1}$
* Forecast: $\hat{X}_{t+h} = L_t + hT_t$

This method is especially useful for datasets exhibiting consistent upward or downward trends.
