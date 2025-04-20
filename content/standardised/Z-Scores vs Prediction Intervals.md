---
tags:
  - statistics
aliases: 
category: 
phase: 
topic: 
filename:
---
[[Z-Score]] and [[Prediction Intervals]] serve different purposes. Z-scores assess existing values within a dataset, while prediction intervals estimate the likely range for future observations.

Use Z-scores to evaluate existing values or standardize. Use prediction intervals to express uncertainty about where a **new** observation is likely to fall.

**Comparison Table**:

|Feature|Z-Score|Prediction Interval|
|---|---|---|
|**Purpose**|Assess deviation from the mean|Forecast future values|
|**Formula**|$Z = \frac{x - \bar{x}}{s}$|$\bar{x} \pm t_{\alpha/2, n-1} \cdot s \cdot \sqrt{1 + \frac{1}{n}}$|
|**Distribution**|Standard Normal (Z)|Student’s t-distribution|
|**Use case**|Outlier detection, normalization|Prediction of new measurements|
|**Width of range**|Based on fixed $\sigma$|Wider—accounts for both sampling error and variability|
|**Needs population $\sigma$?**|Yes (or large $n$ to approximate)|No (uses sample $s$ and $t$ for small $n$)|