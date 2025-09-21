---
aliases: []
category:
date modified: 21-09-2025
tags:
  - time_series
---

### Why Do Differencing in Time Series?

**Differencing** is a technique used to make a non-stationary time series **stationary** ([[Stationary Time Series]]) by removing trends and, if needed, seasonal effects.

- **First-order differencing:**
    - Subtracts each observation from its previous value.
    - Captures the **change from one time step to the next**.
    - Helps remove **linear trends** in the series.
    
- **Higher-order differencing:**
    - If first-order differencing is not enough, you can apply **second-order differencing**:
    - Captures changes in the rate of change, useful for stronger trends.
    
- **Seasonal differencing:**
    - If seasonal patterns remain after first-order differencing, perform **seasonal differencing**
    
- **Why it matters:**
    - Differencing stabilizes the mean of the series.
    - Makes the series suitable for models like [[ARIMA]] and [[SARIMA]], which assume stationarity.
    
- **Next steps:**
    - After differencing, check stationarity with statistical tests such as [[ADF Test]] and [[KPSS Test]].
    - Visual inspection and [[ACF Plots]] can also confirm whether trends or seasonality have been removed.
    
