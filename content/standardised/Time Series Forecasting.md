---
aliases: 
category: DS
date modified: 27-07-2025
tags:
  - time_series
---
When working with [[Time Series]] data, the main goal is often predicting future values based on historical patterns. Can be done:

- Fast: [[Moving Average Forecast]]
- Cheap: [[Exponential Smoothing]]
- Good: Think [[SARIMA]]

Requires (seasonality/trends can be handled separately):
- [[Stationary Time Series]]: because the patterns remain consistent over time (Non stationary makes pattern detection difficult).

May use:
- [[Forecasting using Lags]]

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
	- In [[ML_Tools]] see: https://github.com/rhyslwells/ML_Tools/blob/main/Explorations/Build/TimeSeries/TS_Random_Forest.py
- [[XGBoost]]
- [[LightGBM]]

#### Time Series Model Selection & Evaluation

To know if a forecasting model is good:
- Use proper [[Evaluation Metrics]] such as MAE, RMSE, MAPE.
- Apply time series cross-validation (rolling or expanding windows). See https://medium.com/@soumyachess1496/cross-validation-in-time-series-566ae4981ce4
- Time series cross validation techniques like Nested Cross Validation, Time Series Split Cross Validation, Blocked Cross Validation
- In [[ML_Tools]]: See https://github.com/rhyslwells/ML_Tools/blob/main/Explorations/Build/TimeSeries/TS_Cross_Validation.py

Resources:
[Time Series Forecasting Guide](https://simrenbasra.github.io/simys-blog/2024/09/19/timeseries_part2.html)