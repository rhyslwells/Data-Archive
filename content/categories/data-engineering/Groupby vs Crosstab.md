---
aliases:
- null
category: DE
date modified: 27-09-2025
tags:
- transformation
---
In pandas, [[Groupby]] and [[Crosstab]] serve related but distinct purposes for data ==aggregation== and summarization.

- groupby is more flexible for aggregation and transformations,
- whereas `crosstab` is specifically designed for creating frequency tables and exploring the relationship between categorical variables.


In [[DE_Tools]] see:
- https://github.com/rhyslwells/DE_Tools/blob/main/Explorations/Transformation/reshaping.ipynb
### Key Differences

1. **Purpose**:
   - `groupby`: Used for performing aggregate functions (sum, mean, count, etc.) on grouped data.
   - `crosstab`: Used for generating frequency tables or contingency tables.

2. **Output**:
   - `groupby`: Returns a DataFrame with aggregated values.
   - `crosstab`: Returns a DataFrame with counts or specified aggregation functions applied across two or more columns.

3. **Usage**:
   - `groupby`: Can be used with multiple aggregation functions and complex groupings.
   - `crosstab`: Typically used for counting occurrences and exploring the relationship between two categorical variables.



