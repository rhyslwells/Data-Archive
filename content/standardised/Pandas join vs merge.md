---
aliases: []
category: 
date modified: 1-08-2025
tags: [cleaning, transformation]
---
In pandas, both `.join()` and `pd.merge()` are used to combine DataFrames, but they differ in **syntax**, **defaults**, and **use cases**.

[[Merge]] is better than Join.

|Feature|`df.join()`|`pd.merge()`|
|---|---|---|
|**Default key**|Uses index of caller and index/column of other|Requires explicit column(s) to merge on|
|**Syntax style**|Method on a DataFrame|Function (`pd.merge(left, right)`)|
|**Column join**|Must specify `on=` and use one column from each|Can merge on multiple columns|
|**Index join**|Default behavior (index-to-index)|Requires `left_index=True`, `right_index=True`|
|**Suffixes**|`lsuffix`, `rsuffix`|`suffixes=('_x', '_y')`|
|**Complex joins**|Not well-suited|Supports full SQL-style joins|
|**Use case**|Simple joins on index or one column|Complex joins with control over join behavior| 