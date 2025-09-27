---
aliases:
- null
category: ML
date modified: 27-09-2025
tags:
- anomaly_detection
- preprocessing
---
### Trimming

- Description: Removing data points identified as outliers based on criteria such as being beyond a certain number of standard deviations from the mean or outside a specified percentile range.
- Implementation Example:
  ```python
  lower_quantile = df["var1"].quantile(0.01)
  upper_quantile = df["var1"].quantile(0.99)
  df_no_outliers = df[(df["var1"] >= lower_quantile) & (df["var1"] <= upper_quantile)]
  ```

### Capping or Flooring

- Description: Setting a maximum or minimum threshold beyond which data points are considered outliers and replacing them with the threshold value.

### Winsorizing 

- Description: Similar to capping and flooring, winsorizing replaces extreme values with less extreme values within a specified range, typically using percentiles.