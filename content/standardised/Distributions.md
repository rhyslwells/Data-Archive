---
title: 
tags:
  - statistics
  - drafting
aliases:
  - Distribution
category:
---
In [[ML_Tools]] see:
- [[Distribution_Analysis.py]]
#### Discrete Distributions
These distributions have probabilities concentrated on specific values.

- [[Uniform]] Distribution: All outcomes are equally likely. Example: Drawing a card from a shuffled deck. A boxplot can be meaningful if there’s variation in the distribution. Since the values are discrete, the boxplot will show the range and quartiles effectively.
- [[Bernoulli]] Distribution: Represents two possible outcomes. Example: Coin flip (heads or tails), true/false scenarios. A bar chart or frequency plot would be better for visualizing the proportions. or rolling a dice.
- [[Binomial]] Distribution: Represents the number of successes in a sequence of Bernoulli trials. Example: Number of heads in 10 coin flips,
- [[Poisson]] Distribution: Models the frequency of events in a fixed interval. Example: Number of website visits per hour. A boxplot is suitable for this distribution, showing central tendencies, spread, and potential outliers.

#### Continuous Distributions
These distributions have probabilities spread over a continuous range.

- [[Gaussian Distribution]]: Characterized by a bell-shaped curve, symmetric with thin tails. Example: Heights, exam scores.
- T Distribution: Similar to the normal distribution but with fatter tails, useful with limited data.
- Chi-squared Distribution: Asymmetric and non-negative, commonly used in [[hypothesis testing]].
- Exponential Distribution: Models the time between events. Example: Time between website traffic hits, radioactive decay.
- Logistic Distribution: S-shaped curve, often used in forecasting and modeling growth.
  ![[Pasted image 20250308191945.png]]
  
#### Q-Q plots (Quantile-Quantile Plots)

A Q-Q (quantile-quantile) plot is a graphical tool used to compare the distribution of a dataset against a theoretical distribution (e.g., normal, logistic, exponential). It helps assess how well a given distribution fits the data.

How Q-Q Plots Work:

1. Sort your dataset → Compute the sample quantiles (percentiles).
2. Compute the theoretical quantiles → Take the same number of points from the theoretical distribution (e.g., normal, logistic).
3. Plot sample quantiles vs. theoretical quantiles:
    - If the points lie on a straight diagonal line, the data follows the theoretical distribution.
    - If the points deviate significantly, the data does not fit that distribution.

Interpreting a Q-Q Plot:

- Straight diagonal line → Data follows the chosen distribution.
- Curved S-shape → Data has skewness.
    - Upward curve (right tail high) → Right-skewed.
    - Downward curve (left tail high) → Left-skewed.
- Heavy tails (outliers) → Points at the ends deviate from the line.
- Light tails (thin-tailed distribution) → Points at the ends fall below the line.
### Practical Applications

Feature Distribution: Understanding the distribution of numerical/ categortical feature values across samples can provide insights into data characteristics.

  - Observation: Analyze the spread and central tendency of data.
  - Decision: Determine appropriate statistical methods or transformations.

### Related Notes

In [[ML_Tools]] see: [[Feature_Distribution.py]]

- [[Violin plot]]
- [[Boxplot]]
