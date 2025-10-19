---
aliases: []
category: DS
date modified: 19-10-2025
tags:
  - analysis
  - statistics
  - time_series
---
The rolling mean and cumulative mean are both methods for smoothing or summarising data over time, but they differ in *scope* and *window size*.
### Rolling Mean (Moving Average)

* Definition:  The *rolling mean* calculates the average of a fixed-size window that moves across the dataset.
* Purpose:  Captures *local trends* and smooths short-term fluctuations.
* Example:

  ```
  Data: [2, 4, 6, 8, 10]
  Window = 3
  Rolling mean = [NaN, NaN, 4, 6, 8]
  ```

  (Each value is the mean of the previous 3 observations.)

* Use Cases:

  * Smoothing noisy data.
  * Detecting local trends or seasonal effects.
  * Feature creation in time series models.

### Cumulative Mean (Expanding Mean)

* Definition:  The *cumulative mean* computes the average from the start of the dataset up to the current point.

* Purpose:
  Shows the *long-term average* as more data becomes available.

* Example:
  ```
  Data: [2, 4, 6, 8, 10]
  Cumulative mean = [2, 3, 4, 5, 6]
  ```

  (Each value is the mean of all previous observations up to that point.)

Use Cases:
  * Monitoring convergence of a process.
  * Observing long-term stability.
  * Evaluating cumulative performance metrics.
### Comparison Summary

| Feature          | Rolling Mean                    | Cumulative Mean             |
| ---------------- | ------------------------------- | --------------------------- |
| Window Size  | Fixed (e.g., last 7 days)       | Expanding (start → current) |
| Focus        | Local trends                    | Global, long-term trend     |
| Sensitivity  | Reacts to short-term changes    | Smoothed by all past values |
| Example Tool | `Series.rolling(window).mean()` | `Series.expanding().mean()` |
