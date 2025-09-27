---
aliases:
- AIC
category: ML
date modified: 27-09-2025
tags:
- evaluation
---
AIC stands for Akaike Information Criterion. It is a metric used to compare the goodness-of-fit of statistical models, taking into account both accuracy and complexity. For SARIMA (or any [[ARIMA]]-type model), the formula is:

$$
\text{AIC} = 2k - 2\ln(L)
$$

Where:

* $k$ = number of estimated parameters in the model (including AR, MA, seasonal AR/MA, and variance terms).
* $L$ = maximum likelihood of the model (how probable the observed data is given the model).

Key points:

Lower AIC is better. It balances model fit and complexity.
   * A model with too many parameters may fit the training data well but overfit; AIC penalizes extra parameters.

Relative metric: AIC itself has no absolute meaning; it is only useful for comparing models on the same dataset.

Use in [[SARIMA]]: When tuning $(p,d,q)(P,D,Q)_s$, we often compute AIC for each combination. The model with the lowest AIC is considered the most efficient balance of fit and ==parsimony==.

#### Related

[[Evaluation Metrics]]