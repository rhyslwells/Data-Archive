---
aliases: []
category:
date modified: 27-07-2025
tags: [data_modeling]
---
**ARIMA** (AutoRegressive Integrated Moving Average) is a popular method for [[Time Series Forecasting]] that models the autocorrelations within the data. It is particularly useful for datasets with trends and patterns that are not seasonal. However, it is not perfect; for example, it struggles with predicting stock trading data.

## ARIMA Components

- **AR (AutoRegressive)**: Utilizes the dependency between an observation and a number of lagged observations.
- **I (Integrated)**: Involves differencing the data to achieve stationarity.
- **MA (Moving Average)**: Models the dependency between an observation and a residual error from a moving average model applied to lagged observations.

### ARIMA Explained

**ARIMA** stands for:

- **A**uto**R**egressive (AR): Uses past values to predict the current one.
- **I**ntegrated (I): Differencing to make the series stationary.
- **MA**ving Average (MA): Uses past forecast errors for prediction.

A typical **ARIMA(p,d,q)** model has:

- $p$: Number of **lagged values** (AR terms)
- $d$: Number of **differences** needed to make the series stationary
- $q$: Number of **lagged forecast errors** (MA terms)

#### 🔧 What ARIMA Does:

1. **Checks for stationarity** – if not, applies differencing ($d$ times).
2. **Models relationships** between current values and:
   - Past values (AR part)
   - Past errors (MA part)
3. **Fits** parameters by minimizing a loss (typically log-likelihood).
4. **Forecasts** future values using this learned structure.
### Why ARIMA Isn’t Enough for Seasonal Data

Your quarterly data might show **repeating patterns every 4 quarters** (seasonality), and ARIMA has **no built-in mechanism to model this periodic structure**. This is where **SARIMA** comes in.
### SARIMA: Seasonal ARIMA

SARIMA extends ARIMA by adding **seasonal components**. It is written as:

$$\text{SARIMA}(p, d, q)(P, D, Q)_s$$

Where:

- $(p, d, q)$ are **non-seasonal** ARIMA parameters (as above).
- $(P, D, Q)_s$ are **seasonal** ARIMA parameters:
  - $P$: Seasonal autoregressive terms.
  - $D$: Seasonal differences.
  - $Q$: Seasonal moving average terms.
  - $s$: Seasonality period (e.g., $s=4$ for quarterly data).

#### What SARIMA Adds:

- **Seasonal differencing** ($D$): e.g., subtract the value from 4 quarters ago to remove annual cycles.
- **Seasonal AR/MA** terms: Model relationships from past seasonal lags and errors.

### ✅ Summary

| Model   | Handles Trend | Handles Seasonality | Use When...                                   |
|---------|---------------|---------------------|------------------------------------------------|
| ARIMA   | ✅            | ❌                  | Data has trend, but no regular cycles         |
| SARIMA  | ✅            | ✅                  | Data has both trend and seasonality           |
## Advanced Variants

### SARIMAX (Seasonal ARIMA with Exogenous Variables)

- Incorporates external variables (e.g., interest rates, volume) into the forecasting model.
- Useful for [[Datasets]] where external factors influence the time series.

### Related terms

In [[ML_Tools]] see:
- https://github.com/rhyslwells/ML_Tools/blob/main/Explorations/Build/TimeSeries/ARIMA.ipynb
- [[Forecasting_AutoArima.py]]
- [[pmdarima]]