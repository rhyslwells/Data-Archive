---
aliases: []
category: DS
date modified: 1-08-2025
tags: [preprocessing, transformation]
---
Missing data can provide insights into the data collection process. It's important to determine whether the missing data is randomly distributed or specific to certain features. Filling in data is a type of [[Data Transformation]].

In [[DE_Tools]]see: 
- [[Handling_Missing_Data_Basic.ipynb]]
- [[Handling_Missing_Data.ipynb]]

Resources:
- https://scikit-learn.org/stable/modules/impute.html
## Identifying Missing Data
How do you find which features have the most missing data?

To find where missing values (NA) are located in your dataset, use the following commands:
```python
df.isnull().sum()
df.isna().sum()
df[df.columns[df.isnull().sum() > 0].tolist()].info()
```
## Treating Missing Values ([[Imputation Techniques]])

There are two main strategies for handling missing values: removing them or replacing them.

Remove Missing Values:
  - `dropna`: Drops rows with missing values.
  - `df.dropna(inplace=True)`: Drops rows with NA values and updates the DataFrame in place.
  - `df.reset_index(inplace=True, drop=True)`: Resets the index after dropping rows.

Replace Missing Values:
  - `fillna`: Fills missing values with specified values.
	- Example: `df['var1'] = df['var1'].fillna(df['var1'].mean())` fills missing values in `var1` with the column's average.  
  - `isnull`: Checks for missing values.
  - `df.reindex`: Reindexes the DataFrame.
  - Imputation methods for filling in missing data so that it has a higher likelyhood of being true.

