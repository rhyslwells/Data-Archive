---
aliases: []
category: DE
date modified: 27-09-2025
tags:
- cleaning
---
Purpose
* Investigate gaps in the dataset to understand their causes and impact.
* Decide how to treat missing values (retain, remove, or impute).
* Ensure the dataset remains useful for analysis and modeling.
* Assess missingness: how much, patterns, and impact.
* Impute or drop as appropriate based on project context.
* Document decisions for reproducibility and stakeholder communication.

Key Questions
* How much data is missing overall and per variable?
* Are there patterns in missingness (random vs systematic)?
* Do related columns share similar missing values?
* Are missing values clustered (e.g., certain groups, neighborhoods, or time periods)?
* Can the chosen model handle missing data directly, or is [[Preprocessing]] required?

Exploration Approaches
* Use data exploration tools (Python, JavaScript, etc.) to summarize each column:
  * Mean, [[Variance]], skewness, min, max, sum.
  * Count of zeros and count of missing values.
* Inspect repeating patterns in missingness.
* Compare across related features (column dependencies).

Techniques
* Simple imputation: mean, median, or mode.
* Predictive imputation: regression or ML-based methods (more complex).
* Row/column filtering: dropping rows or columns when appropriate.
* Type conversion: e.g., numbers → strings to preserve categorical meaning.
* Some models (e.g., tree-based methods) can handle missing values directly.

Outcome
* A documented set of working theories on why values are missing.
* A strategy (or multiple strategies) for dealing with missingness before modeling ([[Handling Missing Data]]).

Reference
* NASA (2023). *Dealing with Missing Data: The Art and Science of Imputation*. [Link](https://www.nasa.gov/wp-content/uploads/2023/06/01-dealing-with-missing-data-the-art-and-science-of-imputation.pdf)


