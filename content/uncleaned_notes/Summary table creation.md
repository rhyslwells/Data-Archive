---
tags:
  - pandas
---


What does 
```python
reg_summary = pd.DataFrame(data = x.columns.values, columns=['Features'])
```
do?

x.columns.values: Assuming `x` is a DataFrame, `x.columns` retrieves the column names of the DataFrame, and `values` converts them into a NumPy array. 

columns=['Features']: This sets the column name for the feature names array in the new DataFrame. The resulting DataFrame has one column named 'Features' containing the names of the features.