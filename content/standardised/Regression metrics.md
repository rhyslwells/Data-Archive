---
title: 
tags:
  - code_snippet
  - evaluation
aliases: 
category: 
filename: Regression_Metrics.py
---
These metrics provide various ways to evaluate the performance of regression models.

### Evaluating Regression Models

These metric provide:

1. **Comprehensive Evaluation**: Each metric provides a different perspective on model performance. For example, while MSE and RMSE give insights into the average error magnitude, MAE provides a straightforward average error measure, and R-squared indicates how well the model explains the variance in the data.

2. **Sensitivity to [[standardised/Outliers]]**: Metrics like MSE and RMSE are sensitive to outliers due to the squaring of errors, which can be useful if you want to emphasize larger errors. In contrast, MAE and Median Absolute Error are more robust to outliers.

3. **[[Interpretability]]**: RMSE is in the same units as the target variable, making it easier to interpret in the context of the data. This can be particularly useful for stakeholders who need to understand the model's performance in practical terms.

4. **Model Comparison**: These metrics allow you to compare different models or configurations to determine which one performs best on your data.

5. **Variance Explanation**: R-squared and Explained Variance Score provide insights into how much of the variability in the target variable is captured by the model, which is crucial for understanding the model's effectiveness.
### Common Regression Metrics

#### Mean Absolute Error (MAE):
   - Definition: MAE measures the average absolute differences between predicted and actual values.
   - Interpretation: Lower values indicate better model performance, as it reflects fewer errors in predictions.
   - Formula: 
   $$\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$
   - Where:
     - $n$ = number of observations
     - $y_i$ = actual value
     - $\hat{y}_i$ = predicted value

#### Mean Squared Error (MSE):
   - Definition: MSE calculates the average of the squares of the errors (the differences between predicted and actual values).
   - Interpretation: Like MAE, lower values are better. However, MSE is more sensitive to outliers due to the squaring of errors, which can disproportionately affect the metric. Greater error values are exaggerated.
   - Formula: 
   $$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$
   - Where:
     - $n$ = number of observations
     - $y_i$ = actual value
     - $\hat{y}_i$ = predicted value

#### Root Mean Squared Error (RMSE):
   - Definition: RMSE is the square root of MSE, providing an error metric in the same units as the target variable.
   - Interpretation: Lower RMSE values indicate better model performance, and it also emphasizes larger errors due to the squaring process. Easier to interpreted ([[interpretability]]), back to the same scale as the input.
   - Formula: 
   $$\text{RMSE} = \sqrt{\text{MSE}} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$$

#### [[R squared]]

#### [[Adjusted R squared]]

#### Median Absolute Error:
   - Definition: This metric measures the median of the absolute errors between predicted and actual values.
   - Interpretation: It provides a robust measure of prediction accuracy, especially in the presence of [[standardised/Outliers]].
   - Formula: 
   $$ \text{MedAE} = \text{median}(|y_i - \hat{y}_i|) $$

#### Explained Variance Score:
   - Definition: This metric measures the proportion of variance in the target variable that is predictable from the features.
   - Interpretation: Higher values indicate that the model explains a greater proportion of the [[Variance]] in the target variable.
   - Formula: 
  $$\text{Explained Variance} = 1 - \frac{\text{Var}(y - \hat{y})}{\text{Var}(y)}$$
   - Where:
     - $\text{Var}(y)$ = variance of the actual values
     - $\text{Var}(y - \hat{y})$ = variance of the prediction errors

### Implementation

See Regression_Metrics.py

