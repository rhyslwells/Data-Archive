---
tags:
  - data_exploration
  - data_transformation
  - analysis
aliases: 
category: DATA_ANALYSIS
---
EDA is an approach to analyzing datasets to summarize their main characteristics, often through visual and statistical methods. It helps with:
* Understanding data structure and organization
* Detecting patterns and trends
* Choosing appropriate statistical techniques
* Selecting and assessing variables
* Addressing [[Data Quality]] issues
* Identifying [[Outliers]] and [[storage/utils/file_getter/selected_files/Outliers|anomalies]]
* Formulating and testing hypotheses
* Verifying assumptions prior to modelling

Related to:
- [[Data Assessment]]

## 1. Understanding Variable Behaviour

[[Univariate vs Multivariate]] Analysis
* Univariate: Focuses on single variable distributions, central tendency, and spread.
* Multivariate: Explores interactions between variables and their collective behavior.

Techniques:
* Descriptive statistics: mean, median, mode, percentiles, [[standard deviation]]
* [[Data Visualisation]]: histograms, box plots, bar charts
* Pair plots: for relationships between multiple numerical variables
* Correlation matrices: to assess linear relationships
* Box plots: numeric vs categorical comparison

[[Feature Importance]]Determine which variables matter most:
* Check distributional shape and variance
* Assess predictive separation (e.g. class imbalance in categorical predictors)
* Compute correlation with the target variable
## 2. Distributions and [[Data Transformation]]

Understand the shape and scale of each variable:
* Use [[Log transformation]] to reduce skewness and approximate normal distributions
* For imbalanced categorical features (e.g. 90% in one class), assess usefulness (see [[Imbalanced Datasets]])
* Always interpret [[distributions]] in domain context, not just statistical form

## 3. Data Relationships and [[Correlation]]

Explore dependencies and associations between variables:
* Use scatter plots and correlation coefficients
* Investigate how multiple features interact with the target variable
* Be mindful of spurious correlations-use domain knowledge to guide interpretation
## 4. Purpose-Driven Exploration

EDA should be goal-oriented:
* What modelling or analysis task will follow?
* Are you preparing for [[feature engineering]], selecting variables, or cleaning data?
* Tailor your EDA accordingly to inform future modelling or decision-making
## 5. Evaluating Limitations and Risk

Be explicit about the constraints of your analysis:
* Log issues such as missing data, small subgroup sizes, measurement bias
* Check assumptions ([[Statistical Assumptions]]) where relevant (e.g., normality, linearity)
## 6. Summary and Action

Always conclude with a clear summary:
* Key patterns, outliers, and relationships
* Variables to engineer, discard, or investigate further
* Questions or hypotheses to carry into the modelling phase

## 7. Continuous Development

EDA is iterative-refine your insights as your understanding of the data deepens.

Use implementation tools in [[ML_Tools]], e.g.:
* [[EDA_Pandas.py]]
