In [[ML_Tools]] see: [[Addressing_Multicollinearity.py]]

Multicollinearity can impact the performance and [[interpretability]] of regression models by causing instability in coefficient estimates and complicating the analysis of variable significance. Techniques like PCA can help by transforming correlated variables into uncorrelated principal components, thereby improving model stability and interpretability.

[[Principal Component Analysis]] (PCA) is a [[dimensionality reduction]] technique that can help address [[multicollinearity]] in regression models.

1. **Combining Correlated Variables**: PCA transforms the correlated independent variables into a set of uncorrelated variables called principal components. These components capture the majority of the variance in the data while reducing redundancy.

2. **Reducing Dimensionality**: By selecting a smaller number of principal components that explain most of the variance, PCA can simplify the model. This reduces the complexity and potential overfitting associated with having too many correlated predictors.

3. **Improving Model Stability**: By using principal components instead of the original correlated variables, the regression model can achieve greater stability and reliability in coefficient estimates, as the issues caused by multicollinearity are mitigated.

4. **Enhanced Interpretability**: While the principal components may not have a direct interpretation in terms of the original variables, they can still provide insights into the underlying structure of the data and the relationships among variables.
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

