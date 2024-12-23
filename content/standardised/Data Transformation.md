---
title: What is data transformation?
tags:
  - data_cleaning
  - data_transformation
---
Data transformation is the process of converting data from one format into a different format. Reasons for doing this could be to optimize the data for a different use case than it was originally intended for, or to meet the requirements for storing data in a different system. Data transformation may involve steps such as cleansing, normalizing, [structuring](term/structured%20data.md), validation, sorting, joining, or [enriching](term/data%20enrichment.md) data. 

Data Transformation: Normalizing or scaling numerical values, encoding categorical variables, and converting data types.

 ## Transformation with Pandas

In [[Pandas]]

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

### Change the Layout of Data using a [[Stack]]

See [[Stack]] for when to use
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
## Other types of transformation
Transform raw data into a format that best describes the problem to the model. 

- **[[Supervised Learning]]**: This involves annotating the dataset with the correct answers (labels) to teach the model. For example, labeling images of apples to distinguish them from other fruits.
- **Manual and Automated Labeling**: Manual labeling by humans or leveraging existing labeled data. Tools like Google’s reCAPTCHA help in building labeled datasets.
- [[Database Normalization]]:Ensure consistent data representation and scale features appropriately.
- Convert data into the required format, e.g., from .xls to .csv.
- [[Encoding Categorical Variables]]
- Transform raw data into a format that best describes the problem to the model. This includes formatting and normalization/ [[Normalisation of data]]

## Transformation in Data Engineering
Data is often transformed as part of an [ETL (Extract, Transform, Load)](ETL.md) or [ELT (Extract, Load, Transform)](term/elt.md) approach to [data integration](term/data%20integration.md). 

See [ETL vs. ELT](term/etl%20vs%20elt.md) for a comparison of these two approaches.  

Additionally, a hybrid approach has recently emerged which is known as [EtLT (Extract, “tweak”, Load, Transform)](term/etlt.md). This combines aspects of both ETL and ELT. 
# Other
## Benefits of data transformation
When used correctly, data transformation can provide the following benefits:

- Improved query-time efficiency and speed. 
- Conversion of data into a format that is required by a target system.
- Enrichment of data with additional information that allows insights to be more easily extracted.
- Improved data quality by validating and fixing data, and removal of duplicates. 
## Improved efficiency and speed
One kind of transformation could be the extraction of structured data from data that is stored in a string. Imagine data that looks as follows: 

```
input_string: "Bob is 29"
```

In order to efficiently process this data in the future, it may preferable to transform this data into additional/new fields, and store it as:

```
name: "Bob"
age: 29
```

Storing the data in this manner makes it much more efficient to analyze with operations such as:

```sql
SELECT * FROM X where Age=29
```
