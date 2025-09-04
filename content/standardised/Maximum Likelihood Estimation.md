---
aliases: 
category: 
date modified: 1-08-2025
tags:
  - statistics
  - modeling
---
Resource:
- https://www.youtube.com/watch?v=YevSE6bRhTo

Used to infer [[Model Parameters]] from collected data for example in [[Linear Regression]] ($\beta_0,\beta_1$).

Definition: [[Likelihood]]

Why is it a good tool for guessing parameter values?

The likelihoods plot a distribution, the max gives the most likely.

This is called the MLE.

Properties of a MLE:
- As more data comes in the [[Estimator]] should approach a true value
- MLE is a ==consistent== [[Estimator]], i.e it gets closer to the true parameter value as the sample size grows.
- Asymptotical Normal
- Asymptotic Efficiency

Assumptions for MLE:
- Regularity

[[parametric vs non-parametric models]]

Likelihood is a function of a parameter

Images:

Tha value obtained from MLE is the average of the data collected

Related to [[EM Algorithm]]

The shape of the [[Likelihood]] helps with finding paramaters.

![[Pasted image 20250902074843.png]]