---
tags:
  - data_transformation
aliases: 
category: 
phase: 
topic: 
filename:
---
Using [[pandas]] we can do the following:


- [[Merge]]
- [[Concatenate]]
- [[Joining Datasets]] 
- [[Pandas join vs merge]]
- [[Multi-level index]]

- [[Aggregation]]

- [[Pandas Stack]]
- [[Crosstab]]

A summary of transformations steps can be helpful:

|Step|Operation|Result|
|---|---|---|
|1|`set_index`|Rows get hierarchical keys|
|2|`stack`|Wide → long with 3-level row index|
|3|`reset + extract`|Parse variable names into fields|
|4|`pivot`|Tidy format with metric columns|
|5|`unstack`|Wide format with MultiIndex columns|

In [[DE_Tools]] see:
- https://github.com/rhyslwells/DE_Tools/blob/main/Explorations/Investigating/Transformation

Related terms:

### Split-Apply-Combine

![[Pasted image 20250323081817.png]]
