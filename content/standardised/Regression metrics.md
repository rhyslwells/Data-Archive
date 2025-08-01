---
aliases: []
category: 
date modified: 27-07-2025
tags: [code_snippet, evaluation]
title: 
---
These metrics provide various ways to evaluate the performance of regression models.
### Evaluating Regression Models

These metric provide:

1. **Comprehensive Evaluation**: Each metric provides a different perspective on model performance. For example, while MSE and RMSE give insights into the average error magnitude, MAE provides a straightforward average error measure, and R-squared indicates how well the model explains the variance in the data.

2. **Sensitivity to [[Outliers]]**: Metrics like MSE and RMSE are sensitive to outliers due to the squaring of errors, which can be useful if you want to emphasize larger errors. In contrast, MAE and Median Absolute Error are more robust to outliers.

3. **[[Interpretability]]**: RMSE is in the same units as the target variable, making it easier to interpret in the context of the data. This can be particularly useful for stakeholders who need to understand the model's performance in practical terms.

4. **Model Comparison**: These metrics allow you to compare different models or configurations to determine which one performs best on your data.

5. **Variance Explanation**: R-squared and Explained Variance Score provide insights into how much of the variability in the target variable is captured by the model, which is crucial for understanding the model's effectiveness.
### Common Regression Metrics

#### [[Mean Absolute Error]]

#### [[Mean Squared Error]]
#### [[Root Mean Squared Error]]
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

