ARIMA (AutoRegressive Integrated Moving Average) is a popular [[TimeSeries Forecasting]]method that models the autocorrelations within the data. It is particularly useful for datasets with trends and patterns that are not seasonal.

Not perfect, think of stock trading data and the inability to predict the future.

## Key Concepts

**ARIMA Components:**
  - **AR (AutoRegressive):** Uses the dependency between an observation and a number of lagged observations.
  - **I (Integrated):** Involves differencing the data to make it stationary.
  - **MA (Moving Average):** Models the dependency between an observation and a residual error from a moving average model applied to lagged observations.

## Advanced Variants

 **SARIMA (Seasonal ARIMA):**
   - Extends ARIMA by capturing seasonality in the data.
   - Suitable for datasets with both trend and seasonal patterns.

**SARIMAX (Seasonal ARIMA with Exogenous Variables):**
   - Incorporates external variables (e.g., interest rates, volume) into the forecasting model.
   - Useful for [[datasets]] where external factors influence the time series.

## Tools and Resources

- **AutoARIMA:** Automatically selects the best ARIMA [[model parameters]]. Available in the statsforecast library by [Nixtla](https://www.linkedin.com/company/nixtlainc/).
- **Implementation Example:** See `TS_AutoArima.py` in [[ML_Tools]] for practical implementation.

## Performance Insights

- **[[Evaluation Metrics]]:** Marginal differences in evaluation metrics across ARIMA models may occur due to the volatile nature of the data.
