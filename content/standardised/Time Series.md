---
tags: 
aliases: []
category:
---
Time series data is a sequence of data points collected or recorded at successive points in time, typically at uniform intervals. It captures the temporal ordering of data, which is crucial for analyzing trends, patterns, and changes over time.

Time series data is widely used across various domains, including:
- Finance: Stock prices, interest rates, and economic indicators.
- Weather Forecasting: Temperature, precipitation, and wind speed data.

In [[ML_Tools]] see: TimeSeries folder

"Explorations\Build\TimeSeries"
## What Can You Do with Time Series Data?

With time series data, you can:

- [[Time Series Forecasting]]
- [[Time Series Identify Trends and Patterns]]
- [[Anomaly Detection]]

```python
# We set the 'day' column as the index to facilitate time-series operations.
df.set_index('day', inplace=True)
print(df)
```
