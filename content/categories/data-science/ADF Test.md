---
aliases: []
category: DS
date modified: 19-10-2025
tags: [analysis, statistics, time_series]
---
### **Augmented Dickey-Fuller (ADF) Test**

The **ADF test** is a statistical procedure used to determine whether a time series is **stationary** or **non-stationary**. It is an extension of the Dickey-Fuller test that allows testing for [[Stationary Time Series|stationarity]] in series with more complex autocorrelation structures by including multiple lags.

### **Hypotheses**

1. **Null hypothesis ($H_0$):** The series is non-stationary (has a unit root).
2. **Alternative hypothesis ($H_A$):** The series is stationary (no unit root).

### **Key Concepts**

* **Unit root:** Indicates that ([[Time Series Shocks]]) shocks to the time series have a **permanent effect** and the series is non-stationary.
* **Integration:**
  * If [[Differencing in Time Series|differencing]] a non-stationary series once produces a stationary series, it is said to be **integrated of order 1** ($I(1)$).
  * Some processes may require differencing multiple times (order $d>1$).
* **Mean reversion ([[Mean reverting]]):** A stationary series tends to revert around a constant mean (can be sinusoidal).

### **Notes**

* The ADF test generalizes the Dickey-Fuller test by testing multiple lags simultaneously.
* Its conclusion focuses on the **absence of a unit root**, indicating stationarity.
* Useful reference: [Dickey-Fuller Test](https://en.wikipedia.org/wiki/Dickey%E2%80%93Fuller_test).
