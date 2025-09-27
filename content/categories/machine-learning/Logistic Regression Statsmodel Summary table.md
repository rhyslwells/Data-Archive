---
aliases:
- null
category: ML
date modified: 27-09-2025
tags:
- ml
- regressor
---
Statsmodel has this summary table unlike [[Scikit-Learn]]

[Explanation of summary](https://youtu.be/JwUj5M8QY4U?t=658)

The dependent variable is 'duration'. The model used is a Logit regression (logistic in common lingo), while the method 
- Maximum Likelihood Estimation ([[MLE]]). It has clearly converged after classifying 518 observations.
- The Pseudo R-squared is 0.21 which is within the 'acceptable region'.
- The duration variable is significant and its coefficient is 0.0051.
- The constant is also significant and equals: -1.70 (p value close to 0)
- High p value, suggests to remove from model, drop one by one, ie [[Feature Selection]].

Specifically a graph such as,
![[Pasted image 20240124095916.png]]



$$\mathbb{N}$$