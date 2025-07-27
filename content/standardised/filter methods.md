---
aliases: []
category:
date modified: 27-07-2025
tags: [statistics]
---

For [[Feature Selection]]

1. **Pearson [[Correlation]] Coefficient**:
   - Measures the linear correlation between two continuous variables.
   - Features with low correlation with the target variable are considered less relevant.
   - Features with high correlation among themselves might be redundant.

2. **Mutual Information**:
   - Measures the amount of information obtained about one variable through another variable.
   - High mutual information indicates strong dependency between features and the target variable.
   - Can handle both continuous and categorical variables.
   - used to rank or score features based on their relevance to the target variable.
   - joint probability distribution
   - information theory,

3. **[[ANOVA]] (Analysis of Variance)**:
   - Assesses the differences in means among groups of a categorical variable.
   - Calculates the F-statistic and p-value to determine if there are significant differences in the means of the target variable across different levels of a categorical feature.
   - Useful for selecting features with significant impact on the target variable in classification tasks.

4. **Chi-Squared Test**:
   - Tests the independence between two [[categorical]] variables.
   - Calculates the chi-squared statistic and p-value to determine if the observed frequency distribution differs from the expected distribution.
   - Helpful for [[Feature Selection]] in classification tasks with categorical variables.
