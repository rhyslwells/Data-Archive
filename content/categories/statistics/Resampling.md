---
aliases: []
category: STATISTICS
date modified: 27-09-2025
tags:
- statistics
---
**Resampling** refers to the process of repeatedly drawing samples from an existing dataset (or population) to estimate the variability of a statistic or to generate new sample [[distributions]].

It is not about collecting new data but **reusing existing data** to make inferences or improve model [[Generalisation|robustness]].
### Common Uses

* **[[Bootstrap sampling]]:** Drawing random samples *with replacement* to estimate confidence intervals or standard errors.
* **[[Cross Validation]]:** Repeatedly splitting data into training and test sets to evaluate model performance.
* **Permutation tests:** Randomly shuffling data labels to test hypotheses without parametric assumptions.

### In Time Series

Resampling can also refer to **changing the frequency of observations**, such as aggregating daily data into monthly means or interpolating to higher frequency - see [[Time sampling]].
