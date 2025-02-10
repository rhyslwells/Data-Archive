---
type: 
tags:
  - code_snippet
  - statistics
---
Multicollinearity refers to the ==instability== of a model due to ==highly correlated independent variables.==

It occurs when two or more independent variables in a regression model are highly correlated, which can make it difficult to determine the individual effect of each variable on the dependent variable.

Multicollinearity affects regression models primarily because it leads to instability in the estimated coefficients of the independent variables.

1. **Difficulty in Estimating Coefficients**: When independent variables are highly correlated, it becomes challenging to isolate the individual effect of each variable on the dependent variable. This can result in large standard errors for the coefficients, making them unreliable.
    
2. **Inflated Variance**: The presence of multicollinearity inflates the variance of the coefficient estimates, which can lead to less precise estimates. This means that small changes in the data can lead to large changes in the estimated coefficients.
    
3. **Misleading Significance Tests**: Multicollinearity can cause some variables to appear statistically insignificant when they might actually be significant. This can lead to incorrect conclusions about the importance of predictors in the model.
    
4. **Model Interpretation**: The interpretation of the coefficients becomes complicated, as the effect of one variable may be confounded with the effect of another correlated variable.

[[Addressing Multicollinearity]]

In [[ML_Tools]] see: [[Addressing_Multicollinearity.py]]
### Key Points

- Assumption: The multicollinearity assumption suggests that ==independent variables should not be collinear.==
- Detection: Use tools like [[Heatmap]] or [[Clustering]] to visualize [[Correlation]] and identify multicollinearity.
- Variance Inflation Factor (VIF): High VIF values (typically greater than 10) indicate a high degree of multicollinearity. ==Features with high VIF should be dropped to improve model stability.==
### Example Code

```python

# edit this to explore how to address multi collinusing pca 
from statsmodels.stats.outliers_influence import variance_inflation_factor
import pandas as pd

variables = data_cleaned[['var1', 'var2', 'var3']]
vif = pd.DataFrame()
vif["VIF"] = [variance_inflation_factor(variables.values, i) for i in range(variables.shape[1])]
vif["features"] = variables.columns

# Drop feature with VIF > 10
data_no_multicollinearity = data_cleaned.drop(['Year'], axis=1)
```
