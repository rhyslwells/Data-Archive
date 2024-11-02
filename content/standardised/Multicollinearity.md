---
type: 
tags:
  - code_snippet
  - statistics
---
Multicollinearity refers to the ==instability== of a model due to ==highly correlated independent variables.==

It occurs when two or more independent variables in a regression model are highly correlated, which can make it difficult to determine the individual effect of each variable on the dependent variable.

### Key Points

- Assumption: The multicollinearity assumption suggests that ==independent variables should not be collinear.==
- Detection: Use tools like [[Heatmap]] or [[Clustering]] to visualize [[Correlation]] and identify multicollinearity.
- Variance Inflation Factor (VIF): High VIF values (typically greater than 10) indicate a high degree of multicollinearity. ==Features with high VIF should be dropped to improve model stability.==
### Example Code

```python
from statsmodels.stats.outliers_influence import variance_inflation_factor
import pandas as pd

variables = data_cleaned[['var1', 'var2', 'var3']]
vif = pd.DataFrame()
vif["VIF"] = [variance_inflation_factor(variables.values, i) for i in range(variables.shape[1])]
vif["features"] = variables.columns

# Drop feature with VIF > 10
data_no_multicollinearity = data_cleaned.drop(['Year'], axis=1)
```
