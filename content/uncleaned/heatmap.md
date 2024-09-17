## Description

Nullity correlation ranges from(-1 to 1):

- -1 means if one column(attribute) is present, the other is almost certainly absent.
- 0 means there is no dependence between the columns(attributes).
- 1 means if one column(attributes) is present, the other is also certainly present.
## Why do it?

Remove one or more feature to reduce [[Multicollinearity]] (instability of the model) and redundancy.
## Implementation 

`sb.heatmap(df.corr())`


