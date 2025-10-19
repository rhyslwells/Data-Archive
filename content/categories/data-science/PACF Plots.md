---
aliases: []
category: DS
date modified: 27-09-2025
tags: []
---
Let’s decompose this time series by viewing the PACF (Partial Auto Correlation Function) plot, which measures how much the y variable, in our case, air passengers, is correlated to past values of itself and how far back a statistically significant correlation exists. 

The PACF plot is different from the ACF plot in that PACF controls for correlation between past terms. 

It is good to view both

How to interpret?

[[Decomposition in Time Series]]

[[ACF Plots]]

**Purpose**
The *Partial Autocorrelation Function (PACF)* isolates the **direct correlation** between a time series and its lagged version, removing intermediate effects.

**Interpretation Guide**

* **Significant spike at lag $k$** → direct influence of $X_{t-k}$ on $X_t$.
* **Sharp cutoff after lag $p$** → indicates an **autoregressive model of order $p$ (AR($p$))**.
* **Gradual decay** → suggests an MA or mixed process (ARMA).
* **Few isolated spikes** → may indicate only short memory.

**Useful Notes**

* The first significant lag in PACF suggests the **order $p$** of an AR model.
* PACF complements ACF — together they guide model identification in ARIMA.
* If both ACF and PACF decay slowly → data is likely non-stationary.


![[Pasted image 20250909160420.png]]

Dataset

![[Pasted image 20250909160435.png | 500]]

