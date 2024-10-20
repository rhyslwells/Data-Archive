---
tags:
  - statistics
  - metric
---
For example, an r-squared of 60% reveals that 60% of the variability observed in the target variable is explained by the regression model.

Generally, a higher r-squared indicates more variability is explained by the model.

Definition: R², or the coefficient of determination, indicates the proportion of variance in the dependent variable that can be explained by the independent variables in the model.

Interpretation: R² values range from 0 to 1, where a value of 1 indicates perfect predictions. Higher R² values signify a better fit of the model to the data, but it can be misleading when adding more predictors.

 Formula: 
   $$R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}$$
Where:
     - $\bar{y}$ = mean of the actual values