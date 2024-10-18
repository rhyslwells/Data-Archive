---
type: 
tags:
  - "#data"
  - "#analysis"
---
## Description

The multicollinearity assumption refers only to the idea that the **independent variables** should not be collinear.

Given a feature, f1 (say target), there may exist others that are correlated to it f2,f3,f4. Then you remove those that are strongly correlated.

To see [[Correlation]] use [[heatmap]] or [[Clustering]]

Multicollinearity occurs when two or more independent variables in a regression model are highly correlated

High VIF values (typically greater than 10) indicate a high degree of multicollinearity for the corresponding variable. you drop this feature.

ensure [[Encode categorical features]]

Now you see why we need to drop one of the dummy variables for each feature.
else we get division by 0 when calcualting IVF

```python
from statsmodels.stats.outliers_influence import variance_inflation_factor
variables = data_cleaned[['var1','var2','var3']]
vif = pd.DataFrame()
vif["VIF"] = [variance_inflation_factor(variables.values, i) for i in range(variables.shape[1])]
vif["features"] = variables.columns
#drop feature with VIF >10
data_no_multicollinearity = data_cleaned.drop(['Year'],axis=1)
```