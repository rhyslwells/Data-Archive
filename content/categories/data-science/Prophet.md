---
aliases: []
category: DS
date modified: 16-10-2025
tags:
  - analysis
  - forecasting
  - ml_process
  - time_series
---
**Prophet** is a [[Time Series Forecasting]] method developed by [[facebook]] for modeling time series data with **trend**, **seasonality**, and **holiday effects**. It is designed to handle business time series with strong seasonal patterns and missing data.

### How it Works

Prophet models a time series as an additive combination of components:

$$y(t) = g(t) + s(t) + h(t) + \epsilon_t$$

where:

* $g(t)$ - trend component (piecewise linear or logistic growth)
* $s(t)$ - seasonal component (modeled with Fourier series)
* $h(t)$ - holiday effects
* $\epsilon_t$ - error term (irregular noise)

It fits these components using [[curve fitting]] and regression, rather than classical statistical assumptions (e.g., stationarity).
### Benefits

* **Interpretable:** Components (trend, seasonality, holidays) are explicitly modeled and easy to visualize.
* **Robust:** Handles missing data, outliers, and irregular time series.
* **Flexible:** Captures both additive and multiplicative seasonal effects.
* **Automatic:** Minimal tuning required - works well with default settings.
* **Scalable:** Efficient for large datasets and multiple time series.
