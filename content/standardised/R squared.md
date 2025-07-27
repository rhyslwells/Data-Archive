---
aliases: []
category:
date modified: 27-07-2025
tags: [statistics]
---
R², or the coefficient of determination, ==measures the proportion of variance in the dependent variable that is explained by the independent variables== in a [[regression]] model.

**Interpretation**:  
- R² values range from 0 to 1.
- A value of 1 indicates perfect predictions, meaning the model explains all the variability of the response data around its mean.
- Higher R² values signify a better fit of the model to the data. However, it can be misleading when adding more predictors, as R² will never decrease when more variables are added to a model. See [[Adjusted R squared]].

**Formula**:  
$$R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}$$

Where:
- $y_i$ = actual values
- $\hat{y}_i$ = predicted values
- $\bar{y}$ = mean of the actual values

**Example**:  
An R² of 0.60 indicates that 60% of the variability observed in the target variable is explained by the regression model.

#### Follow up Questions
- [[R-squared metric not always a good indicator of model performance in regression]]