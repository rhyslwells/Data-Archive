---
aliases: []
category: ML
date modified: 1-08-2025
tags: [anomaly_detection]
---
In [[Time Series]]

In [[ML_Tools]] see:
- [[TS_Anomaly_Detection.py]]

To perform [[anomaly detection]] specifically for time series data, you can utilize various techniques that account for the ==temporal nature== of the data. Here are some common methods:

1. Statistical Methods:
   - Moving Average: Calculate a moving average and identify points that deviate significantly from this average.
   - Seasonal Decomposition: Decompose the time series into trend, seasonal, and residual components. Anomalies can be identified in the residuals.

2. Time Series Models:
   - AutoRegressive Integrated Moving Average: Fit an [[ARIMA]] model to the time series data and analyze the residuals for anomalies.
   - State Space Model (ETS): Similar to ARIMA, this model can be used to forecast and identify anomalies in the residuals.

3. Machine Learning Approaches:
   - [[LSTM]] (Long Short-Term Memory): Use LSTM networks to model the time series and detect anomalies based on prediction errors.
   - [[Isolated Forest]]: This algorithm can be adapted for time series data by treating time as an additional feature.

4. Change Point Detection:
   - Identify points in time where the statistical properties of the time series change significantly, which may indicate anomalies.

5. Visual Methods:
   - Time Series Plots: Visual inspection of time series plots can help identify anomalies.
   - Control Charts: Use control charts to monitor the time series and flag points that fall outside control limits.
