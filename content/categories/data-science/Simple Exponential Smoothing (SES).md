---
aliases: []
category: DS
date modified: 27-09-2025
tags:
  - time_series
---
Simple Exponential Smoothing is a forecasting method designed for time series ==without trend or seasonality==. It applies a single smoothing parameter $\alpha$ to update the series’ **level**, producing forecasts that are constant over time. The forecasts adapt gradually to changes in the average level but do not account for upward or downward trends.