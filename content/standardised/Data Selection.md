---
aliases: []
category: 
date modified: 1-08-2025
tags: [selection, transformation]
---
Data selection is a crucial part of data manipulation and analysis. Pandas provides several methods to select data from a DataFrame.

In [[DE_Tools]] we explore how to do Data Selection with Pandas
- https://github.com/rhyslwells/DE_Tools/blob/main/Explorations/Transformation/selection.ipynb

Related:
- [[Data Selection in ML]]
## Examples
### Selecting Columns

You can select a single column from a DataFrame using either bracket notation or dot notation:

```python
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
column_a = df['A']  # or df.A
```
### Selecting Rows by Index

To select rows by their index position, you can use slicing:
```python
rows_0_to_2 = df[0:3]  # Selects the first three rows
```
### Selecting Rows by Date Range

If your DataFrame has a DateTime index, you can select rows within a specific date range:

```python
date_rng = pd.date_range(start='2013-01-01', end='2013-01-06', freq='D')
df = pd.DataFrame(date_rng, columns=['date'])
df.set_index('date', inplace=True)
selected_dates = df['2013-01-02':'2013-01-04']
```
### Label-based Selection

Use `.loc` or `.at` to select rows by label:

```python
df = pd.DataFrame({'Weather': ['Sunny', 'Rain', 'Cloudy'], 'Temp': [30, 22, 25]})
df.set_index('Weather', inplace=True)
rain_row = df.loc['Rain']  # or df.at['Rain']
```
### Position-based Selection

Use `.iloc` or `.iat` to select rows by position:

```python
third_row = df.iloc[2]  # Selects the third row
specific_value = df.iat[1, 1]  # Selects the value at row 1, column 1
```
### Conditional Selection

Create a new DataFrame based on a condition:
```python
df_new = df[df['var1'] >= 999]  # Selects rows where 'var1' is greater than or equal to 999
```
The condition `df["var1"] >= 999` creates a boolean Series that filters the rows of `df`.

