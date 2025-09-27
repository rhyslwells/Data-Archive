---
aliases:
- null
category: STATISTICS
date modified: 27-09-2025
tags:
- statistics
---
R-squared (R²) is a commonly used metric for assessing the performance of regression models, but it is not always a reliable indicator of model quality. It should not be the sole criterion for evaluating model performance. It is essential to consider other metrics, such as [[Adjusted R squared]], [[Cross Validation]] results, and the overall context of the analysis.

1. **Increased Complexity**: R² will never decrease when more predictors are added to a model, even if those predictors do not have a meaningful relationship with the dependent variable. This can lead to overfitting, where the model captures noise rather than the underlying data pattern.

2. **Lack of Context**: A high R² value does not necessarily imply that the model is appropriate for prediction. ==It only indicates the proportion of variance explained==. A model with a high R² might still have poor predictive performance if it does not generalize well to new data.

3. **Non-linearity**: R² assumes a linear relationship between the independent and dependent variables. If the true relationship is non-linear, R² may provide a false sense of model adequacy.

4. **Ignoring Model Assumptions**: R² does not account for whether the assumptions of the regression model (such as homoscedasticity, independence, and normality of residuals) are met. A model may have a high R² but still violate these assumptions, leading to unreliable results.

5. **Adjusted R²**: To address some of these issues, Adjusted R² is often used, which adjusts the R² value based on the number of predictors in the model. It provides a more accurate measure of model performance when comparing models with different numbers of predictors.

