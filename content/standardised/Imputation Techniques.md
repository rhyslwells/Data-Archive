---
tags: 
category: 
---
### Imputation Techniques

For columns with say less than 30% missing data, you can fill in missing values using various imputation techniques.

```python
from sklearn.preprocessing import Imputer
```
#### Column Average Imputation
Fill missing values with the column's average:
```python
df['var1'] = df['var1'].fillna(df['var1'].mean())
```

#### Using [[Groupby]]

Use `groupby` to calculate averages for a variable with respect to another variable and fill missing values:

Using `groupby` to fill in missing values involves aggregating data based on certain groups and then using the aggregated values to fill in the blanks. This method is particularly useful when you want to fill missing values with statistics (like mean, median, or mode) calculated within specific groups of data. Here's how you can do it:

Suppose you have a DataFrame with missing values in a column, and you want to fill these missing values with the mean of the group to which each row belongs.

```python
import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C','B'],
    'Value': [10, np.nan, 20, 25, np.nan, 30,np.nan]
}
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Group by 'Category' and calculate the mean for each group
grouped_means = df.groupby('Category')['Value'].transform('mean')

# Fill missing values with the group mean
df['Value'] = df['Value'].fillna(grouped_means)

# Display the DataFrame after filling missing values
print("\nDataFrame after filling missing values with group means:")
print(df)

  Category  Value
0        A   10.0
1        A   10.0
2        B   20.0
3        B   25.0
4        C   30.0
5        C   30.0
6        B   22.5
```

Explanation:
1. Grouping: The `groupby('Category')` groups the DataFrame by the 'Category' column.
2. Transformation: The `transform('mean')` function calculates the mean of the 'Value' column for each group and returns a Series with the same index as the original DataFrame. This allows you to align the group means with the original data.
3. Filling Missing Values: The `fillna(grouped_means)` function fills the missing values in the 'Value' column with the corresponding group mean.

Benefits:
- Contextual Filling: By using group-specific statistics, you ensure that the imputed values are more contextually relevant compared to using a global statistic like the overall mean.
- Preservation of Group Characteristics: This method helps maintain the ==inherent characteristics of each group==, which might be lost if a single value is used for imputation across all groups.

This approach is part of data transformation techniques that help in cleaning and preparing data for analysis or modeling, ensuring that the data is as accurate and representative as possible.
#### Using functions
```python
def funct(cols):
    var1 = cols[0]
    var2 = cols[1]
    if pd.isnull(var1): # It uses predefined means (`element_1_mean`, `element_2_mean`, `generic_mean`) depending on the value of `var2`.
        if var2 == 0:
            return element_1_mean
        elif var2 == 1:
            return element_2_mean
        else:
            return generic_mean
    else:
        return var1
df['var1'] = df[['var1', 'var2']].apply(funct, axis=1)
```

#### Filling with Specific Values

Fill missing values with specific common values:
```python
test.loc[test.KitchenQual.isnull(), 'KitchenQual'] = 'TA'
data.loc[data['Electrical'].isnull(), 'Electrical'] = 'SBrkr'
test.loc[test['LotFrontage'].isnull(), 'LotFrontage'] = test['LotFrontage'].mean()
```
#### Other Imputation Methods

##### KNN

https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html

K-nearest neighbors (KNN) imputation: Uses the average of the K most similar data points.
	- Example: `from sklearn.impute import KNNImputer` initializes the KNN imputer.
##### Other
- Hot deck imputation: Randomly selects existing data points from the group.
- Cold deck imputation: Replaces missing values with a constant value, often a default like "0".