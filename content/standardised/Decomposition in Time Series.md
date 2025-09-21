---
aliases: []
category:
date modified: 3-09-2025
tags:
  - analysis
  - statistics
  - time_series
---
When analyzing a [[Time Series]], we often use [[Decomposition in Time Series]] to separate it into three main components:
* [[Trends in Time Series]] – long-term direction in the data
* [[Seasonality in Time Series]] – repeating patterns at fixed intervals
* [[Residuals in Time Series]] – the unexplained variation after removing trend and seasonality

A common method for decomposition is [[STL Decomposition]], which flexibly extracts trend and seasonal components.

### Why Decompose?

* Helps identify stable trend and seasonal structures.
* Makes it easier to test whether the series is a [[Stationary Time Series]] (constant mean and variance).
* Prepares the data for forecasting models.

### Handling Trend and Seasonality

To model effectively, you often need to **make the data stationary**:
* Remove trends
* Remove seasonality

This can be checked using:
* Plots of the series
* [[ACF Plots]] and [[PACF Plots]]
* Statistical tests (e.g., ADF test)

### Practical Considerations

* **Check stationarity** before modeling [[Stationary Time Series]].
* **Split into components** (trend, seasonality, residuals) where helpful.
* **Avoid over-differencing** — too much differencing removes useful information.
* **Model choices**:
  * Classical approaches: [[SARIMA]], [[Exponential Smoothing]]
  * Decomposition + ML: [[Random Forest for Time Series]], Gradient Boosting

Resource:
[Understanding Stationarity in Time Series](https://towardsdatascience.com/time-series-forecasting-made-simple-part-4-1-understanding-stationarity-in-a-time-series/)

### Image

![[Pasted image 20250909160252.png]]

