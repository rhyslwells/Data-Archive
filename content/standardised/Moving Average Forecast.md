---
aliases: []
category:
date modified: 19-09-2025
tags: [forecasting, ml, time_series]
---
### Moving Average Forecasts

A **Moving Average (MA) forecast** works by taking the average of the last $n$ observed points and projecting this forward. It is one of the simplest forecasting approaches and is often used as a **baseline model**.

#### Limitations of Simple Moving Averages

* **Equal weighting**: Every value in the chosen window contributes equally, regardless of how recent it is. This means recent shifts in the data are not emphasized.
* **No trend or seasonality**: SMAs produce flat forecasts that cannot capture upward/downward movements or repeating seasonal patterns.
* **Window size sensitivity**: The choice of window length heavily influences the forecast. Too small a window may be noisy; too large a window may overly smooth the series.
* **Forecast horizon problem**: An SMA essentially fails to produce meaningful predictions beyond the averaging window, since it always outputs a constant extension.

Because of these drawbacks, SMA is rarely used for serious forecasting beyond benchmarking. More advanced methods, such as [[Exponential Smoothing]], Holt’s, or Holt-Winters’, address these issues by giving more weight to recent data and modeling trend and seasonality explicitly.

### Variants

**Simple Moving Average (SMA)**
* Uses the last $k$ values to compute a single average.
* Produces a **flat forecast line** into the future.
* Useful as a naive benchmark but not for dynamic patterns.

**Rolling Moving Average**
* Each new prediction is updated iteratively using the most recent window, which can include earlier forecasts.
* Produces a line smoother than Holt’s, but still limited in capturing complex dynamics.
