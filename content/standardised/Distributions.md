---
title: 
tags:
  - statistics
  - drafting
aliases: 
category:
---
Types of Distributions:

Discrete Distributions: Probability concentrated on specific values (e.g., coin flips, number of customers).
    
- Uniform: All outcomes equally likely (e.g., drawing a card from a shuffled deck).
- Bernoulli: Two possible outcomes (e.g., coin flip, true/false).
- Binomial: Sequence of Bernoulli trials (e.g., number of heads in 10 coin flips).
- Poisson: Frequency of events in a fixed interval (e.g., website visits per hour).

Common Continuous Distributions: Probability spread over a continuous range
- [[Gaussian Distribution]]/Normal: Bell-shaped curve, symmetric, thin tails (e.g., heights, exam scores). 
- T: Similar to normal but with fatter tails, used with limited data. 
- Chi-squared: Asymmetric, non-negative, used in hypothesis testing. 
- Exponential: Models time between events (e.g., website traffic, radioactive decay). 
- Logistic: S-shaped curve, used in forecasting and modeling growth.

## Practical 

What is the distribution of numerical feature values across the samples?

	Observation:
	Decision:

What is the distribution of categorical features?
```python
g = sns.FacetGrid(df, col='Survived')
g.map(plt.hist, 'var1', bins=20)
```

[[Violin plot]]

[[Boxplot]]

