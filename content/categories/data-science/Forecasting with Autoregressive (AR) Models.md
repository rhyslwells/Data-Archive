---
aliases: []
category:
date modified: 14-10-2025
tags:
  - classifer
  - ml_process
  - statistics
  - time_series
---
Predict future values using past observations ([[Autoregression]]), assuming linear dependence on previous time steps.

**Procedure**

1. **Ensure [[Stationary Time Series|Stationarity]]**

   * Remove trend and seasonality via *[[Differencing in Time Series|differencing]]* or *decomposition*.
   * Test for stationarity with the **[[ADF test]]**.

2. **Model Identification**

   * Use **PACF** to determine AR order $p$.
   * Fit an **AR($p$)** model:
     $$X_t = c + \phi_1 X_{t-1} + \phi_2 X_{t-2} + \dots + \phi_p X_{t-p} + \epsilon_t$$

3. **Model Fitting & Diagnostics**

   * Estimate coefficients via Maximum Likelihood or Least Squares.
   * Check residuals: should resemble **white noise** (no autocorrelation).

4. **Forecasting**

   * Generate forecasts $\hat{X}_{t+h}$ recursively using the fitted coefficients.
   * For differenced data, **reconstruct** forecasts by reversing the differencing operation.

5. **Interpretation**

   * AR models describe *persistence* or *memory* in data.
   * A slow decay in [[ACF Plots|ACF]] or significant PACF lags indicates how many past values drive predictions.