---
aliases: []
category: DS
date modified: 27-09-2025
tags:
- time_series
---
### Additive Model

In an **additive model**, the observed time series is expressed as the **sum of its components**:

$Y_t = T_t + S_t + R_t$

Where:

* $Y_t$: observed value at time $t$
* $T_t$: trend component
* $S_t$: seasonal component
* $R_t$: residual (random noise)

This assumes each component contributes **independently and linearly** to the series.

We typically use an **additive model** when:

* The **seasonal effect is stable over time** (e.g., summer–winter differences remain consistent).
* The **trend does not distort or amplify seasonality**.
* Seasonal fluctuations stay within a fixed range, even if minor noise exists.

For example, in daily minimum temperature data, the **seasonal swings remain steady** year after year. This stability indicates that the **additive model is appropriate**, since seasonality does not depend on the trend.
### Multiplicative Model

In a **multiplicative model**, the components interact by scaling:

$Y_t = T_t \times S_t \times R_t$

Where:

* $Y_t$: observed value
* $T_t$: trend
* $S_t$: seasonal effect
* $R_t$: residual

This model is suited for series where the **magnitude of seasonality changes with the trend**. For example, when seasonal peaks and troughs **grow larger as the trend increases**.

### Choosing Between Models

* **Additive model** ->stable seasonal effect, constant magnitude, independent of trend.
* **Multiplicative model** -> seasonal effect scales with trend.

The choice can often be made by visually inspecting the decomposition plot. See [[Decomposition in Time Series]].

Example:

- **Additive**: seasonal effect is constant in magnitude (e.g., demand increases by +100 GWh every winter).
- **Multiplicative**: seasonal effect scales with the level (e.g., winter demand is 20% higher than the baseline).  
### Related

See [[Baseline Forecast]] for once the models type is selected.