---
tags:
  - data_exploration
aliases: 
category:
---
Exploratory Data Analysis (EDA) is an approach to analyzing data sets to summarize their main characteristics, often using visual methods. 

Allowing the user to:
- understand the data's structure, 
- understand how to provide a good model,
- detect patterns, 
- decide of [[Statistics]] techniques by looking at [[Distributions]] and [[Correlation]]
- decide on which variabled to include,
- how to handle [[Data Quality]]
- spot anomalies & [[Outliers]]
- Generating/testing hypotheses with stastical methods, 
- and check assumptions through statistical summaries and graphical representations.
### Common Techniques Used in EDA

- **Descriptive Statistics**: Calculating measures such as mean, median, mode, standard deviation, and percentiles to summarize data.
- **Data Visualization**: Using plots and charts like histograms, box plots, scatter plots, and bar charts to visually explore data.
- **Correlation Analysis**: Assessing relationships between variables using correlation coefficients and scatter plots.
- **Data Transformation**: Applying transformations to data, such as normalization or log transformation, to better understand its characteristics.

### Tools and Libraries for EDA

- **Python Libraries**: Pandas, Matplotlib, Seaborn, and Plotly are commonly used for EDA in Python.
- **Data Visualization Tools**: Tools like [[Tableau]] and [[PowerBI]] can also be used for interactive exploratory analysis.

### code snippets:

```python
sns.pairplot(
    penguins,
    x_vars=["bill_length_mm"],
    y_vars=["bill_depth_mm"],hue="species")
```

**What are the data types for various features?**
`df.info()`

Get a summary of missing data of a df.
```python
def get_numerical_summary(df):
    total = df.shape[0]
    missing_columns = [col for col in df.columns if df[col].isnull().sum() > 0]
    missing_percent = {}
    for col in missing_columns:
        null_count = df[col].isnull().sum()
        per = (null_count/total) * 100
        missing_percent[col] = per
        print("{} : {} ({}%)".format(col, null_count, round(per, 3)))
    return missing_percent
```

