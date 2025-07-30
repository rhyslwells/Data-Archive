---
aliases: []
category:
date modified: 27-07-2025
tags: []
---
==Measures numerical proximity.==
#### Mean Squared Error
   - Definition: MSE calculates the average of the squares of the errors (the differences between predicted and actual values).
   - Interpretation: Like MAE, lower values are better. However, MSE is more sensitive to outliers due to the squaring of errors, which can disproportionately affect the metric. Greater error values are exaggerated.
   - Formula: 
   $$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$
   - Where:
     - $n$ = number of observations
     - $y_i$ = actual value
     - $\hat{y}_i$ = predicted value