---
aliases: 
category: 
date modified: 27-07-2025
tags:
  - statistics
---
Prediction intervals estimate the range within which a future observation from the same distribution is likely to fall, with a specified confidence level.

**Formula**:

$$\bar{x} \pm t_{\alpha/2, n-1} \cdot s \cdot \sqrt{1 + \frac{1}{n}}$$

**Where**:
- $\bar{x}$: Sample mean
- $s$: Sample standard deviation
- $n$: Sample size
- $t_{\alpha/2, n-1}$: t-critical value for the chosen confidence level

**Notes**:
- Prediction intervals are always **wider** than a confidence interval for the mean.
- They use the t-distribution due to sample uncertainty.
- The interval is centered around $\bar{x}$ but accounts for:
    - **Estimation error** of the mean
    - **Natural variability** of new values

**Use Cases**:
- Forecasting where a new measurement is likely to fall.
- Risk assessment and operational thresholds.

Related:
- [[Probability]]