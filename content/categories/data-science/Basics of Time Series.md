---
aliases: []
category: DS
date modified: 27-09-2025
tags: []
---
Basics of [[Time Series]]
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