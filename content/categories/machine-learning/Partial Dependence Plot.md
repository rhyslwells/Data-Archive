---
aliases:
  - 
category: ML
date modified: 27-09-2025
tags:
  - evaluation
  - explainability
---
Partial dependence plots (PDP) show the dependence between the target response and a set of input features of interest, marginalizing over the values of all other input features (the ‘complement’ features). Intuitively, we can interpret the partial dependence as the expected target response as a function of the input features of interest.

Need to do [[Feature Importance]] first.

Tells what happens to the target when you change the feature.

https://scikit-learn.org/stable/modules/partial_dependence.html

Related:
- [[Interpretability|interpretable]]
- [[ICE Plot]]
### Examples

Regression example:

![[Pasted image 20241204203338.png]]

Categorical Example

![[Pasted image 20241204203413.png]]

