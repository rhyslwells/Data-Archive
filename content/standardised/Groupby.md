---
type: grouping
tags:
  - data_transformation
  - data_transformation
---

See [[Groupby vs Crosstab]] too

![[Pasted image 20250323081619.png]]
# What it is used for:

```python
	df.groubpy("var1").describe()
```


# How to use:

```
# Grouping by 'var1' 
var1_groups = df.groupby(df['var1']]) 
# Accessing the group for 'element' 
element_var1=var1_groups.get_group(element)
```
### [[Groupby]]

`groupby` is a versatile method in pandas used to group data based on one or more columns, and then perform aggregate functions on the grouped data. Here's a simple example:
```python
# Sample DataFrame
df = pd.DataFrame({'Category': ['A', 'B', 'A', 'B', 'A'],'Values': [10, 20, 30, 40, 50]})
# Group by 'Category' and calculate the sum of 'Values'
grouped = df.groupby('Category').sum()
print(grouped)
```
Output:
```
          Values
Category        
A              90
B              60
```