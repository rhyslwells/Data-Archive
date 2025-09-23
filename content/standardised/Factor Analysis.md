---
aliases: 
category: 
date modified: 27-07-2025
tags:
  - analysis
  - statistics
---
Factor Analysis (FA) is a statistical method used for:
- [[Dimensionality Reduction]],
- [[EDA]]
- or latent variable detection

It identifies underlying relationships between observed variables by modeling them as linear combinations of a smaller number of ==unobserved latent factors==.

In simpler terms, it helps reduce a large number of variables into fewer factors while retaining the core information and structure of the data. It assumes that observed variables are influenced by some common latent factors and unique errors.

### Key Features of Factor Analysis:

1. Latent Factors: These are unobserved variables that capture the shared variance among observed variables.
2. Variance Decomposition: FA splits the total variance of observed variables into:
    - Common variance: Shared by latent factors.
    - Unique variance: Specific to each observed variable.

In [[ML_Tools]] see: [[Factor_Analysis.py]]

### Next Steps:

1. Would you like to visualize the factors to understand how the data clusters in the new latent space?
2. Should we explore the relationships between the factors and target classes (e.g., species in the Iris dataset)?