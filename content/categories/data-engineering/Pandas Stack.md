---
aliases: []
category: DE
date modified: 27-09-2025
tags:
- transformation
---
Tool for reshaping data, particularly when you need to pivot a DataFrame ([[Pandas Pivot Table]]) from a wide format to a long format. 

See:
- [[Pandas_Common.py]]
- [[Pandas_Stack.py]]

In [[DE_Tools]] see:
- https://github.com/rhyslwells/DE_Tools/blob/main/Explorations/Transformation/reshaping.ipynb
#### Why Use `stack`? ([[Data Transformation]])

Data Reshaping:
   - ==Wide to Long Format==: Convert a DataFrame from a wide format to a long format, which is often preferred for statistical models and visualizations.

Handling Multi-Index DataFrames:
   - Simplifying Structure: Move the inner level of a column MultiIndex to the row index, simplifying the DataFrame's structure.

[[Data Cleansing]]:
   - Aggregation and Operations: Facilitate data cleaning by allowing aggregation or operations across columns in a more manageable long format.

Preparing Data for Grouping or Aggregation ([[Groupby]]):
   - Ease of Grouping: Simplify group-by operations and aggregations on data with columns representing different categories or time periods.
#### Example of Using `stack`

Consider the following example to illustrate how `stack` works:

```python
import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Using stack
stacked_df = df.stack()
print("\nStacked DataFrame:")
print(stacked_df)
```

Output:
```
Original DataFrame:
   A  B  C
0  1  4  7
1  2  5  8
2  3  6  9

Stacked DataFrame:
0  A    1
   B    4
   C    7
1  A    2
   B    5
   C    8
2  A    3
   B    6
   C    9
dtype: int64
```

In this example:
- The original DataFrame has three columns ('A', 'B', 'C') and three rows.
- After stacking, the DataFrame is transformed into a Series with a MultiIndex/[[Multi-level index]]. The outer level of the index corresponds to the original DataFrame’s row index, and the inner level corresponds to the original column labels.

#### When Not to Use `stack`

- Wide Format Requirements: If your analysis or processing requires a wide format, such as some [[Machine Learning Algorithms]], stacking may not be appropriate.
- Complexity: If stacking makes the data too complex to manage or understand, it might be better to keep the original structure.
- Simplicity: When the current structure of your DataFrame already suits your analysis needs, stacking may be unnecessary.