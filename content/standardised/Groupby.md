---
aliases: []
category:
date modified: 1-08-2025
tags: [transformation]
type: grouping
---
Groupby is a versatile method in pandas used to group data based on one or more columns, and then perform aggregate functions on the grouped data. 

Related:
- [[Groupby vs Crosstab]]

In [[DE_Tools]] see:
- https://github.com/rhyslwells/DE_Tools/blob/main/Explorations/Investigating/Transformation/group_by.ipynb
### Implementation
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


![[Pasted image 20250323081619.png]]
