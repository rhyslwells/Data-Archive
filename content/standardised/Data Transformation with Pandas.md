---
tags:
  - data_transformation
aliases: 
category: 
phase: 
topic: 
filename:
---
Using [[pandas]] we can do the following:

In [[DE_Tools]] see:
- https://github.com/rhyslwells/DE_Tools/blob/main/Explorations/Investigating/Transformation
### Combining Datasets

```python
# Merge
df1 = pd.DataFrame({'key': ['A', 'B'], 'value': [1, 2]})
df2 = pd.DataFrame({'key': ['A', 'B'], 'value': [3, 4]})
merged_df = pd.merge(df1, df2, on='key')

# Concat
concat_df = pd.concat([df1, df2])

# Join
df1.set_index('key', inplace=True)
df2.set_index('key', inplace=True)
joined_df = df1.join(df2, lsuffix='_left', rsuffix='_right')
```

### Aggregating Data [[Groupby]]

```python
df = pd.DataFrame({'category': ['A', 'B', 'A'], 'value': [10, 20, 30]})
grouped_df = df.groupby('category').sum()
```
### Split-Apply-Combine

![[Pasted image 20250323081817.png]]
### Change the Layout of Data using a [[Pandas Stack]]

See [[Pandas Stack]] for when to use
```python
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['first', 'second'])
stacked_df = df.stack()
unstacked_df = stacked_df.unstack()
```
### Pivot Table: Summarize Data
```python
df = pd.DataFrame({'A': ['foo', 'foo', 'bar'], 'B': ['one', 'two', 'one'], 'C': [1, 2, 3]})
pivot_table = df.pivot_table(values='C', index='A', columns='B', aggfunc='sum')
```

### Handle Time-Based
```python
date_rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')
time_series_df = pd.DataFrame(date_rng, columns=['date'])
time_series_df['data'] = range(len(time_series_df))
```
### Sorting Order Data

```python
df = pd.DataFrame({'A': [3, 1, 2]})
sorted_df = df.sort_values(by='A')
```
### Rename Columns

```python
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df = df.drop(columns=['B'])
df = df.rename(columns={'A': 'new_A'})
```
### Identify Duplicate Entries
```python
df = pd.DataFrame({'A': [1, 1, 2], 'B': [3, 4, 4]})
duplicates = df.duplicated()
```