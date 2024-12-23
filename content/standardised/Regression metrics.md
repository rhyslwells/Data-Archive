---
title: 
tags:
  - code_snippet
  - evaluation
aliases: 
category:
---
These metrics provide various ways to evaluate the performance of regression models, each with its strengths and weaknesses. The choice of metric often depends on the specific characteristics of the data and the goals of the analysis.

[[Loss function]]
### Common Regression Metrics

1. **Mean Absolute Error (MAE)**:
   - **Definition**: MAE measures the average absolute differences between predicted and actual values.
   - **Interpretation**: Lower values indicate better model performance, as it reflects fewer errors in predictions.
   - **Formula**: 
   $$\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$
   - **Where**:
     - $n$ = number of observations
     - $y_i$ = actual value
     - $\hat{y}_i$ = predicted value

2. **Mean Squared Error (MSE)**:
   - **Definition**: MSE calculates the average of the squares of the errors (the differences between predicted and actual values).
   - **Interpretation**: Like MAE, lower values are better. However, MSE is more sensitive to outliers due to the squaring of errors, which can disproportionately affect the metric.
   - **Formula**: 
   $$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$
   - **Where**:
     - $n$ = number of observations
     - $y_i$ = actual value
     - $\hat{y}_i$ = predicted value

3. **Root Mean Squared Error (RMSE)**:
   - **Definition**: RMSE is the square root of MSE, providing an error metric in the same units as the target variable.
   - **Interpretation**: Lower RMSE values indicate better model performance, and it also emphasizes larger errors due to the squaring process.
   - **Formula**: 
   $$\text{RMSE} = \sqrt{\text{MSE}} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$$

4. [[R squared]]

6. [[Adjusted R squared]]

7. **Median Absolute Error**:
   - **Definition**: This metric measures the median of the absolute errors between predicted and actual values.
   - **Interpretation**: It provides a robust measure of prediction accuracy, especially in the presence of outliers.
   - **Formula**: 
   $$ \text{MedAE} = \text{median}(|y_i - \hat{y}_i|) $$

6. **Explained Variance Score**:
   - **Definition**: This metric measures the proportion of variance in the target variable that is predictable from the features.
   - **Interpretation**: Higher values indicate that the model explains a greater proportion of the variance in the target variable.
   - **Formula**: 
  $$\text{Explained Variance} = 1 - \frac{\text{Var}(y - \hat{y})}{\text{Var}(y)}$$
   - **Where**:
     - $\text{Var}(y)$ = variance of the actual values
     - $\text{Var}(y - \hat{y})$ = variance of the prediction errors

### Code snippets

Regression Metrics

1. Mean Absolute Error (MAE). Lower better.

```python
from sklearn.metrics import mean_absolute_error
# Assuming y_true and y_pred are your true and predicted values respectively
mae = mean_absolute_error(y_true, y_pred)
print("Mean Absolute Error:", mae)
```

2. Mean Squared Error (MSE). Lower better. MSE is more sensitive to outliers

```python
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_true, y_pred)
print("Mean Squared Error:", mse)
```

3. Root Mean Squared Error (RMSE)

```python
import numpy as np
rmse = np.sqrt(mean_squared_error(y_true, y_pred))
print("Root Mean Squared Error:", rmse)
```

4. R-squared (R2)I [[R squared]]. t ranges from 0 to 1, where 1 indicates perfect predictions. Higher R2 values signify better model fit to the data

```python
from sklearn.metrics import r2_score
r2 = r2_score(y_true, y_pred)
print("R-squared:", r2)
```

5. Median Absolute Error

```python
from sklearn.metrics import median_absolute_error
median_abs_err = median_absolute_error(y_true, y_pred)
print("Median Absolute Error:", median_abs_err)
```

6. Explained Variance Score

```python
from sklearn.metrics import explained_variance_score
explained_var = explained_variance_score(y_true, y_pred)
print("Explained Variance Score:", explained_var)
```
