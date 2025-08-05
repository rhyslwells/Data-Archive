---
aliases: 
category: 
date modified: 27-07-2025
tags:
  - regressor
  - statistics
  - ml
---


In logistic regression, the model predicts the ==odds of an event happening rather than directly predicting probabilities.== The odds are defined as:

$$ \text{Odds} = \frac{P(\text{success})}{P(\text{failure})} = \frac{p}{1-p} $$

  where $p$ is the probability of success. The log-odds (or logit function) is the natural logarithm of the odds:
  $$ \text{Log-Odds} = \ln\left(\frac{p}{1-p}\right) = b_0 + b_1 x $$
  This ==transformation makes the relationship between the independent variables and the dependent variable linear,== allowing logistic regression to estimate the parameters $b_0$ and $b_1$.

Resources:
- [Explanation of log odds](https://www.youtube.com/watch?v=ARfXDSkQf1Y)
- [Explanation of log odd function](https://www.youtube.com/watch?v=fJ53tIDbvTM)

[[Odds vs Probability]]