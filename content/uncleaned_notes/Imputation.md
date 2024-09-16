---
type: term
tags:
  - data_analysis
---
# What does it do:

For columns that have not been dropped (with less than 30% missing), e.g var1. Fill in missing values in a given column with a given term.


#### Column average
We can fill any NA terms with column average 
`df.var1 = df.var1.fillna(inputs.var1.mean())`

#### Using groupby
Use [[Groupby]] to get averages for var1 wrt var2. We then can input the averages to the missing values of var1 with:

```
def funct(cols):
    var1 = cols[0]
    var2 = cols[1]
    if pd.isnull(var1):
        if var2 == 0:
            return element_1_mean
        elif Parch == 1:
            return element_2_mean
        else:
            return generic_mean
    else:
        return var1
        
df['var1']= df[['var1', 'var2']].apply(funct, axis=1)
```

**More specific terms:**

- **Group mean imputation:** This emphasizes that the average is calculated from the group or subgroup the missing data belongs to (e.g., income by profession).



#### Filling in NA with specific values



```python
#Fill NA with common values.
test.loc[test.KitchenQual.isnull(), 'KitchenQual'] = 'TA'
data.loc[data['Electrical'].isnull(), 'Electrical'] = 'SBrkr'
test.loc[test['LotFrontage'].isnull(), 'LotFrontage'] = test['LotFrontage'].mean()
```


```python


    import pandas as pd
    import numpy as np
    from sklearn.impute import SimpleImputer
    from sklearn.compose import ColumnTransformer
    my_imputer = SimpleImputer(strategy = "most_frequent")
    df = pd.DataFrame({'a' : [6, 8, 6, np.NaN]})
    imputer = ColumnTransformer( [ ('imp', my_imputer, ['a']) ] )
    fitted = imputer.fit_transform(df)
    df_filled = pd.DataFrame(fitted)

```

#### Other methods

- **K-nearest neighbors (KNN) imputation:** This uses the average of the K most similar data points to the missing point.
- **Hot deck imputation:** This randomly selects existing data points from the group to replace the missing values.
- **Cold deck imputation:** This replaces missing values with a constant value, not necessarily the average, often a default value like "0" or "unknown."

Explore : [[Imputation]]
```python
from sklearn.impute import KNNImputer
```