---
aliases: []
category:
date modified: 27-07-2025
tags: [evaluation, statistics]
---
Adjusted R-squared is a [[Regression Metrics]]or assessing the quality of a regression model, ==especially when multiple predictors== are involved. It helps ensure that the model remains [[parsimonious]] while still providing a good fit to the data.

When evaluating a regression model, if you notice a ==large difference== between [[R squared]] and adjusted R², it indicates that the additional predictors may not be improving the model's performance.

In such cases, it may be beneficial to drop those extra variables to simplify the model without sacrificing predictive power.

Key features:

1. **Penalty for Number of Predictors**:
   - Adjusted R² adjusts the R² value by penalizing the addition of ==unnecessary predictors==. This means that if you add a variable that does not improve the model significantly, the adjusted R² will decrease, reflecting that the model may be overfitting.

2. **Comparison with R-squared**:
   - Adjusted R² is always less than or equal to R². While R² can artificially inflate with the addition of more predictors (even if they are not useful), adjusted R² provides a ==more reliable== assessment of model fit by considering the number of predictors relative to the number of observations.

3. **Interpretation**:
   - Like R², adjusted R² values range from 0 to 1, where values closer to 1 indicate a better fit. However, a significant difference between R² and adjusted R² suggests that the model may be penalized for including extra variables that do not contribute meaningfully to the prediction.

4. **Formula**:
   $$R^2_{adj.} = 1 - (1 - R^2) \cdot \frac{n - 1}{n - p - 1}$$
   - Where:
     - $R^2$ = R-squared value
     - $n$ = number of observations
     - $p$ = number of predictors (independent variables)


