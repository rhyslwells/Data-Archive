---
aliases: []
category:
date modified: 27-08-2025
tags:
  - time_series
---
When working with multiple time series, joining them typically involves aligning records by timestamp. This can serve two purposes:

* Combine metrics: Add additional measurements from different sources.
* Extend time span: Append data to create a longer series.

Key Consideration: [[Granularity]]
* The time granularity of each series matters when joining.
* If one series has hourly data and another has daily data, you must decide how to aggregate or resample before the join.


Clock Skew
* Clock skew occurs when timestamps do not perfectly align across sources.
* A common solution is to truncate or round timestamps to the desired precision (e.g., nearest minute, hour).

Related Analysis Patterns
* [[Views]]
* [[SQL Joins]]

