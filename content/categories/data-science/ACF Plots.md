---
aliases:
- ACF
category: DS
date modified: 27-09-2025
tags: []
---
An [[Autocorrelation]] function plot shows how each observation in a time series is correlated with its past values at different lags ([[Forecasting using Lags]]).

In a [[Stationary Time Series]], autocorrelations typically **decay quickly toward zero** as the lag increases. This indicates that past values have decreasing influence on future values over time.

In this case, however, we observe that autocorrelations remain **high across multiple lags**. This suggests:
* The presence of a **trend**, since values are persistently related over time ([[Trends in Time Series]]).
* The presence of **seasonality**, if there are repeating peaks at specific lag intervals ([[Seasonality in Time Series]]).

**Interpretation:** The slow decay and repeated high correlations confirm that the series is **non-stationary**. When examining the ACF plot, you are primarily looking for:

1. **Decay pattern:** Rapid decay indicates stationarity; slow decay suggests non-stationarity.
2. **Significant peaks:** Regular spikes at certain lags indicate seasonality.
3. **Correlation magnitude:** High correlations at large lags indicate a trend or long-term dependencies.

---

**Purpose**
The *Autocorrelation Function (ACF)* measures how correlated a time series is with its own lagged versions. It captures both **direct** and **indirect** relationships.

**Interpretation Guide**

* **Significant spikes** outside the confidence interval → meaningful correlation at that lag.
* **Gradual decay** → indicates an **autoregressive (AR)** process.
* **Sharp cutoff** after a few lags → suggests a **moving average (MA)** process.
* **Alternating signs** (positive/negative correlations) → may indicate oscillatory behaviour.
* **Slow decay over many lags** → possible non-stationarity or trend in data.
* **Seasonal pattern** → repeating peaks at multiples of seasonal lag (e.g., lag 12 for monthly data).

**Useful Notes**

* ACF includes *indirect effects*: correlation at lag 3 may be due to correlations at lags 1 and 2.
* Always apply ACF to **stationary data**; otherwise correlations may be misleading.
* Use ACF to determine **$q$** in an MA($q$) model.

---

[[PACF Plots]]

[[Forecasting with Autoregressive (AR) Models]]

![[Pasted image 20250909163931.png]]