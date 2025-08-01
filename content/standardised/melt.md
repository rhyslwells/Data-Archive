---
aliases: 
category: DATA_ANALYSIS
created: 2024-06-21 15:32
date modified: 27-07-2025
tags:
  - transformation
type:
---
In pandas, the `melt` function is used to ==transform ([[Data Transformation]]) a DataFrame from a wide format to a long format==. This is especially useful for data analysis and visualization tasks where long-format data is preferred or required. The wide format typically has multiple columns for different variables, whereas the long format has a single column for variable names and a single column for values. 

Related:
- [[Database Techniques]]
- [[Turning a flat file into a database]]

In [[DE_Tools]] see:
- https://github.com/rhyslwells/DE_Tools/blob/main/Explorations/Transformation/reshaping.ipynb
### Key Reasons to Use `melt`:

1. [[Normalisation]]
   - Wide to Long Transformation: `melt` helps in converting data with many columns (wide format) into a more normalized form with fewer columns (long format). This is useful for many statistical and visualization libraries that prefer long-format data.
   
1. Easier Analysis and [[Data Visualisation]]:
   - Compatibility with Plotting Libraries: Many plotting libraries like `[[seaborn]]` and `ggplot` require data in a long format for creating certain types of plots, such as [[Grouped plots]].

1. Simplifying Complex Data Structures:
   - Handling [[Multi-level index]]: If a DataFrame has multiple levels of columns, `melt` can help flatten this structure, making it easier to work with.
   
3. Preparation for Aggregation:
   - Facilitating [[Groupby]] Operations: Long-format data is often more suitable for these.

### Parameters of `melt`:

- `id_vars`: Columns to use as identifier variables. These columns are kept as-is in the output.
- `value_vars`: Columns to unpivot. These columns are transformed into a single column.
- `var_name`: Name to use for the `variable` column in the output.
- `value_name`: Name to use for the `value` column in the output.

### Example Usage:

Consider a DataFrame in wide format:

```python
import pandas as pd

# Sample wide format data
data = {
    'id': [1, 2, 3],
    'math_score': [88, 92, 95],
    'science_score': [85, 90, 89],
    'english_score': [78, 85, 88]
}
df_wide = pd.DataFrame(data)
print(df_wide)
```

Output:

```
   id  math_score  science_score  english_score
0   1          88             85             78
1   2          92             90             85
2   3          95             89             88
```

To convert this wide-format DataFrame into a long-format DataFrame using `melt`:

```python
# Melt the DataFrame
df_long = pd.melt(df_wide, id_vars=['id'], 
                  value_vars=['math_score', 'science_score', 'english_score'], 
                  var_name='subject', value_name='score')
print(df_long)
```

Output:

```
   id       subject  score
0   1    math_score     88
1   2    math_score     92
2   3    math_score     95
3   1  science_score     85
4   2  science_score     90
5   3  science_score     89
6   1  english_score     78
7   2  english_score     85
8   3  english_score     88
```


