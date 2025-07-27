---
aliases: []
category:
date modified: 27-07-2025
tags: [data_transformation]
---
Multi-level indexing in pandas—also called hierarchical indexing—enables you to work with higher-dimensional data in a 2D DataFrame. It's particularly useful for working with grouped or nested data structures.

Why use multi-level index:
- MultiIndex makes your data [[interoperable]]
- Enables systematic slicing and aggregation
- Logical grouping of variables

Operations like `.stack()` and `.unstack()` rely on MultiIndex to move between long and wide formats.
- In a flat DataFrame, reshaping often requires column renaming or pivoting.
- With MultiIndex, it's structured and reversible.
- Stack can be used to make a multi index from a flat dataframe.

If you need frequent slicing/aggregation across multiple levels, MultiIndex saves effort and code.

When _not_ to use it
- If your data is simple or small.
- If you're just loading, cleaning, and exporting CSVs.
- If you don’t need `.groupby(level=...)`, `.stack()`, or `.xs()` operations.

Similar to:
- SQL composite keys
- Python nested dictionaries
- [[JSON]] hierarchical structures

Related:
- [[Groupby]]
- [[Pandas Stack]]

In [[DE_Tools]] see:
- https://github.com/rhyslwells/DE_Tools/blob/main/Explorations/Transformation/multi__level_index.ipynb

How this mimics a 3D array:
- You can think of each (Product, Store) pair as defining a "slice" of a 2D array.
- The columns (Jan, Feb) represent time-like progression (3rd axis).
- Visually, it’s like you’ve flattened a cube into a matrix while retaining the ability to slice along all original axes.

```python
Month             Jan  Feb
Product   Store            
Product A Store X  100  110
          Store Y  120  115
Product B Store X   90  105
          Store Y   95  100
```