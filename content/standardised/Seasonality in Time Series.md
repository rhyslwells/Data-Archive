---
aliases: []
category:
date modified: 10-09-2025
tags:
  - time_series
---
Seasonality refers to patterns that repeat at fixed intervals (daily, weekly, monthly, or yearly).
Example: higher sales of cold drinks during summer.
#### Ways to Handle Seasonality

1. Seasonal Differencing
   Remove seasonal effects by subtracting the value from the same season in a previous cycle:

   $y'_t = y_t - y_{t-s}$

   where $s$ is the seasonal period (e.g., $s = 12$ for monthly data with yearly seasonality).

2. Break the series into trend (T), seasonal (S), and residual (R) components:
	1. [[Decomposition in Time Series]]
	2. [[Additive vs Multiplicative Models Time Series]]
	3. [[STL Decomposition]]

3. Seasonal Dummy Variables
   Encode seasonality as categorical indicators (e.g., month or quarter dummies) to use as features in machine learning models.
