---
aliases: []
category: ML
date modified: 1-08-2025
tags: [evaluation, exploration]
type: process
---
Effective models depend on high-quality, ==informative features==. Feature evaluation helps identify which features contribute meaningfully to model performance and which may be redundant or harmful.

#### Objectives
* Determine the relevance, predictive power, and redundancy of features.
* Guide [[feature selection]], engineering, and model interpretation.

#### Core Aspects

[[Feature Importance]]

Feature Relationships Assess:
* [[Correlation]] between features to detect redundancy
* Interactions that may impact the target variable

Performance Impact: Measure how feature inclusion/exclusion affects:
* Model accuracy, precision, [[AUC]], etc.
* Stability and generalisability of results

#### When Evaluation is Complete
* Feature set achieves optimal model performance
* Further changes offer no significant improvement
* Feature effects are [[interpretability|interpretable]] and aligned with domain knowledge
