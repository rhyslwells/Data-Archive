---
aliases: []
category:
date modified: 27-08-2025
tags: []
---

Core Concepts

* Lag Features: Use past values as predictors for future points.
* Rolling Windows / Aggregations: Compute moving averages, sums, or other statistics over fixed intervals.
* Time-Based Features: Include hour of day, day of week, or calendar effects; can be per SIM, per cell tower, etc.

Data Quality

* Handle missing timestamps and irregular events appropriately.
* Impute missing values or resample data to regular intervals if needed.

Statistical Properties

* Stationarity: Check if mean, variance, and autocorrelation are constant over time. Use tests like ADF.
* Trend and Seasonality: Identify and potentially remove to stabilize the series.
* ACF / PACF Analysis: Understand autocorrelation structure; helps determine relevant lag features.

Practical Feature Engineering

* Combine lags, rolling statistics, and time-based features to create predictive input matrices.
* Adjust features for irregular timestamps and missing data.

Common Interview Questions
* *“How do you check if a time series is stationary?”*
	* You typically examine whether its **statistical properties** (mean, variance, autocorrelation) remain constant over time. You can visualise it, get summary stats, do ADF tests.
