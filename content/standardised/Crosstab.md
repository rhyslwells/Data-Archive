Used to compute a simple cross-tabulation of two (or more) factors. It is particularly useful for computing frequency tables. Here's an example:

```python
# Sample DataFrame
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Subcategory': ['X', 'X', 'Y', 'Y', 'X']
})

# Cross-tabulation of 'Category' and 'Subcategory'
crosstab = pd.crosstab(df['Category'], df['Subcategory'])
print(crosstab)
```

Input
```
  Category Subcategory
0        A           X
1        B           X
2        A           Y
3        B           Y
4        A           X
```

Output:
```
Subcategory  X  Y
Category         
A            2  1
B            1  1
```

In [[DE_Tools]] see:
- https://github.com/rhyslwells/DE_Tools/blob/main/Explorations/Transformation/reshaping.ipynb