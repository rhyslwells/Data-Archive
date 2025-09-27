---
aliases: []
category: ML
date modified: 27-09-2025
tags:
- explainability
- statistics
---
For [[Feature Selection]]

1. Pearson [[Correlation]] Coefficient:
   - Measures the linear correlation between two continuous variables.
   - Features with low correlation with the target variable are considered less relevant.
   - Features with high correlation among themselves might be redundant.

1. Mutual Information:
   - Measures the amount of information obtained about one variable through another variable.
   - High mutual information indicates strong dependency between features and the target variable.
   - Can handle both continuous and categorical variables.
   - used to rank or score features based on their relevance to the target variable.
   - joint probability distribution
   - information theory,

[[ANOVA]]

1. Chi-Squared Test:
   - Tests the independence between two [[categorical]] variables.
   - Calculates the chi-squared statistic and p-value to determine if the observed frequency distribution differs from the expected distribution.
   - Helpful for [[Feature Selection]] in classification tasks with categorical variables.
