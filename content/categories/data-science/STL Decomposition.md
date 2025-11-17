---
aliases: []
category: DS
date modified: 27-09-2025
tags:
- time_series
---
When trend and seasonal patterns in a time series are messy or evolving, we use STL to extract them.

Trends may change gradually, and seasonal behaviours can vary year to year. This is why we need a more adaptable approach than classical decomposition.

```python
from statsmodels.tsa.seasonal import STL
```

Seasonal-Trend decomposition using LOESS
* Unlike classical decomposition, ==STL allows seasonal patterns to change gradually.==
* Better suited for real-world, non-stationary data.
* Produces adaptive seasonality and cleaner residuals compared to classical methods.
* Useful when you want to deseasonalize but the seasonality is not straightforward.

Key ideas:
* STL identifies one-off events (e.g., COVID dip) as irregular, not trend or seasonality.
* LOESS (Locally Estimated Scatterplot Smoothing) underpins STL, refining trend and seasonal estimates iteratively.
* Initial estimates use moving averages (trend via 12-month MA, seasonality via grouped monthly averages).
* Refinement ensures the seasonal component is centered (mean = 0 per cycle), preventing contamination of the trend.

Takeaway:
STL is more flexible and robust than classical decomposition, making it a preferred choice when patterns evolve over time.

Related:
- [[Decomposition in Time Series]]

Resources:
- https://towardsdatascience.com/time-series-forecasting-made-simple-part-3-1-stl-decomposition-understanding-initial-trend-and-seasonality-prior-to-loess-smoothing/

Classical

![[Pasted image 20250909171538.png]]

With STL

![[Pasted image 20250909171641.png]]