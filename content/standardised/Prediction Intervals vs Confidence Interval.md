---
aliases: []
category:
date modified: 2-09-2025
tags:
  - statistics
  - ml
  - time_series
---
A [[Prediction Intervals]] and a [[Confidence Interval]] are related but serve different purposes:

1. Prediction Interval (`PI`)
   * Estimates the range where a ==future single observation== is expected to fall.
   * Accounts for both the uncertainty in the model parameters and the natural variability/noise of the data.
   * Example: "We predict that tomorrow’s temperature will be between 15°C and 20°C with 95% probability."

1. Confidence Interval (`CI`)
   * Estimates the uncertainty around an ==estimated parameter== (like the mean of a population).
   * Only reflects the uncertainty in the parameter estimate, not the variability of individual observations.
   * Example: "We are 95% confident that the average temperature this month is between 16°C and 18°C."

Key difference:
* PI is about where a ==new observation== will fall.
* CI is about where a ==statistical estimate== (like the mean) lies.

In [[Time Series Forecasting]] a 95% prediction interval tells you the likely range of the next actual value, while a 95% confidence interval would tell you the uncertainty around the expected forecasted mean.