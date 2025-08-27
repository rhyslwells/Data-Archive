---
aliases: 
category: 
date modified: 28-07-2025
tags:
  - statistics
---
#### Root Mean Squared Error
   - Definition: RMSE is the square root of MSE, providing an error metric in the same units as the target variable.
   - Interpretation: Lower RMSE values indicate better model performance, and it also emphasizes larger errors due to the squaring process. Easier to interpreted ([[Interpretability]]), back to the same scale as the input.
   - Formula: 
   $$\text{RMSE} = \sqrt{\text{MSE}} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$$