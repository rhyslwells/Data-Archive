---
aliases: []
category: DS
date modified: 9-11-2025
tags: [analysis, ml_process, statistics]
---
Residual analysis is the process of examining the difference between observed values and the values predicted by a model. These differences, known as residuals, indicate what the model has *not* explained. Studying residuals helps determine whether the model is appropriate and whether there are patterns left to model.

## What are residuals?

For a model prediction $\hat{y}_t$, the residual is:

$e_t = y_t - \hat{y}_t$

Residuals represent unexplained variation in the data. If the model is suitable, this unexplained component should resemble random noise.
## Why residual analysis matters

Residual analysis provides diagnostic information about model fit. It can reveal:

* Missed structure in the data (trend, seasonality, cycles).
* Remaining autocorrelation or lagged effects.
* Nonlinear relationships not captured by the model.
* Variance changes (heteroskedasticity).
* Deviations from normality that may affect inference.
* Outliers or one-off events influencing the model.

Residuals that show patterns suggest the model can be improved.

## What good residuals look like

A well-specified model produces residuals with these properties:

* Mean close to $0$.
* No visible trend or seasonality.
* Constant variance through time.
* No significant autocorrelation.
* Roughly Gaussian distribution.

This behaviour resembles **white noise**, indicating the model has extracted all systematic structure from the data.
## Common diagnostic tools

### Plots

* **Residual time plot:** should show no structure or drift.
* **ACF/PACF:** should have no significant autocorrelation.
* **Histogram/Density plot:** should appear symmetric and bell-shaped.
* **Q-Q plot:** points should align with the $45^\circ$ reference line.
* **Residuals vs fitted values:** should show no patterns or funnels.

### Statistical tests

* **Normality tests:** Jarque–Bera, Shapiro–Wilk.
* **Autocorrelation tests:** Ljung–Box or Box–Pierce.
* **Heteroskedasticity tests:** Breusch–Pagan or ARCH tests.
## When residuals indicate problems

Patterns in residuals often reveal specific issues:

* **Trend in residuals:** the model has missed an underlying trend.
* **Seasonal patterns:** missing seasonal components.
* **Clusters of volatility:** heteroskedasticity; consider GARCH-type models.
* **Significant autocorrelation:** the model is under-differenced or missing lag structure.
* **Skewness or heavy tails:** distributional assumptions may not hold.

These signals suggest that model refinement, transformation, or a different modelling approach may be needed.
