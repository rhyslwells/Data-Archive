---
aliases: []
category: DS
date modified: 27-09-2025
tags:
  - time_series
  - ML_Tools
---
When working with [[Time Series]] data, the main goal is often predicting future values based on historical patterns. Can be done:

- Fast: [[Moving Average Forecast]]
- Cheap: [[Exponential Smoothing]]
- Good: Think [[SARIMA]]

Requires (seasonality/trends can be handled separately):
- [[Stationary Time Series]]: because the patterns remain consistent over time (Non stationary makes pattern detection difficult).

May use:
- [[Forecasting using Lags]]

How to estimate the forecastability of a time series?

The more regular and repeatable patterns a time series has, the easier it is to forecast. The ‘Approximate Entropy’ can be used to quantify the regularity and unpredictability of fluctuations in a time series.

The higher the approximate entropy, the more difficult it is to forecast it.

Another better alternate is the ‘Sample Entropy’.

Sample Entropy is similar to approximate entropy but is more consistent in estimating the complexity even for smaller time series. For example, a random time series with fewer data points can have a lower ‘approximate entropy’ than a more ‘regular’ time series, whereas, a longer random time series will have a higher ‘approximate entropy’.

#### Time Series Statistical Methods

Traditional models that explicitly capture trend, seasonality, and autocorrelation in time series data.

Classical Methods: Usually Beats SoTA methods
- [[Baseline Forecast]]
- [[Moving Average Forecast]]
- [[Exponential Smoothing]]
- [[ARIMA]] – Autoregressive Integrated Moving Average.
- [[SARIMA]] – Seasonal ARIMA for multiple seasonal patterns.
- [[Prophet]] – Handles seasonality and holidays well.
- [[Multiple Linear Regression]]
- [[Regression Metrics]]
- [[Mean Absolute Percentage Error]]

Implementations:
- [[Forecasting_Baseline.py]] – Naive or simple baseline forecasting.
- [[Forecasting_AutoArima.py]] – Automated ARIMA model selection.
- See: [[Forecasting_Exponential_Smoothing.py]]
#### Time Series Machine Learning Methods

Modern approaches that use feature-based forecasting or global models across multiple series. These methods require [[Feature Engineering for Time Series]], such as lag features, rolling windows, and time-based features (hour, day, week). Possible [[Data Leakage]] if not setup correctly.

ML/State of the Art Methods:
- [[LSTM in Time Series]]

Examples:
- [[Random Forest]] for time series (global approach)
- [[XGBoost]]
- [[LightGBM]]

#### Time Series Model Selection & Evaluation

To know if a forecasting model is good:
- Use proper [[Evaluation Metrics]] such as MAE, RMSE, MAPE.
- Apply time series cross-validation (rolling or expanding windows). See https://medium.com/@soumyachess1496/cross-validation-in-time-series-566ae4981ce4
- Time series cross validation techniques like Nested Cross Validation, Time Series Split Cross Validation, Blocked Cross Validation

Resources:
[Time Series Forecasting Guide](https://simrenbasra.github.io/simys-blog/2024/09/19/timeseries_part2.html)