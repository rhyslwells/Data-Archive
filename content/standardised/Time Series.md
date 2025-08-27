---
aliases: []
category:
date modified: 1-08-2025
tags:
  - modeling
  - time_series
---

Time series data is a sequence of data points collected or recorded at successive points in time, typically at uniform intervals. Its key characteristic is the ==temporal ordering of observations,== which makes it essential for analyzing trends, patterns, and changes over time.

Related:
* [[Time Series Forecasting]]
* [[Anomaly Detection in Time Series]]
* [[Querying Time Series]]
* [[Joining Time Series]]
* [[Time Series Python Packages]]

To investigate:
- [[Feature Engineering for Time Series]]
- [[Time Series Forecasting]]
- [[MLOPS for Time Series]]

---

 Key Characteristics
* Each record consists of timestamps with measurements.
* Different time series can have different frequencies (e.g., hourly, daily).
* Always check the unit of measurement for each field (e.g., cm, \$, etc.).

Metric types:
  * Counter: Monotonically increases.
  * Gauge: Can go up or down.
  * Summary: Aggregate calculation over a period.

 Data Structure Considerations
* Time series data is often stored in a long column format.
* Partition datasets by period (e.g., monthly) for:
	- Easier period-based querying.
	- Computing aggregates.
	- Focusing on recent data efficiently.

Common Applications
* Finance: Stock prices, interest rates, economic indicators.
* Weather Forecasting: Temperature, precipitation, wind speed.

Relevant Resources
* In [[ML_Tools]], see the TimeSeries folder:  [GitHub: Time Series Explorations](https://github.com/rhyslwells/ML_Tools/blob/main/Explorations/Build/TimeSeries)