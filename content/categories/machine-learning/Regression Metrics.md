---
aliases: []
category: ML
date modified: 27-09-2025
tags:
- code_snippet
- evaluation
---
These metrics provide various ways to evaluate the performance of regression models.

 [[Mean Absolute Error]]
 [[Mean Absolute Percentage Error]]
 [[Mean Squared Error]]
 [[Root Mean Squared Error]]
 [[R squared]]
 [[Adjusted R squared]]
 [[Median Absolute Error]]
### Evaluating Regression Models

These metric provide:

1. **Comprehensive Evaluation**: Each metric provides a different perspective on model performance. For example, while MSE and RMSE give insights into the average error magnitude, MAE provides a straightforward average error measure, and R-squared indicates how well the model explains the variance in the data.

2. **Sensitivity to [[uncategorised/Outliers]]**: Metrics like MSE and RMSE are sensitive to outliers due to the squaring of errors, which can be useful if you want to emphasize larger errors. In contrast, MAE and Median Absolute Error are more robust to outliers.

3. **[[Interpretability]]**: RMSE is in the same units as the target variable, making it easier to interpret in the context of the data. This can be particularly useful for stakeholders who need to understand the model's performance in practical terms.

4. **Model Comparison**: These metrics allow you to compare different models or configurations to determine which one performs best on your data.

5. **Variance Explanation**: R-squared and Explained Variance Score provide insights into how much of the variability in the target variable is captured by the model, which is crucial for understanding the model's effectiveness.
### Implementation

See Regression_Metrics.py
