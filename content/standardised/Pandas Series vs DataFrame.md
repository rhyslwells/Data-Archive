---
aliases: []
category:
date modified: 28-08-2025
tags: [pandas]
---
Series: One-dimensional labeled array.

  * Shape: `(n,)` -> single axis of length `n`.
  * Can store numbers, strings, or other data types.
  * Example:

  ```python
  import pandas as pd
  s = pd.Series([22, 24, 19], index=['Day1', 'Day2', 'Day3'])
  ```

* DataFrame: Two-dimensional labeled data structure (rows × columns).

  * Shape: `(n, m)` -> `n` rows, `m` columns.
  * Each column is a Series.
  * Example:

  ```python
  df = pd.DataFrame({'Temperature': [22, 24, 19]}, index=['Day1', 'Day2', 'Day3'])
  ```

* Single-column DataFrame vs Series:

  * `df` with one column is still 2D -> shape `(n,1)`.
  * `df['Temperature']` or `df.iloc[:,0]` converts it to Series (1D -> shape `(n,)`).
  * Some functions require 1D Series; others require 2D DataFrame.

Rule of thumb:

* Use Series for single-variable operations.
* Use DataFrame for multiple columns or when 2D operations are needed.