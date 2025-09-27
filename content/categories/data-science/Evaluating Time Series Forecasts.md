---
aliases: []
category: DS
date modified: 27-09-2025
tags:
- business
- evaluation
- time_series
---
Evaluating a **time series forecast** involves measuring how well your predictions match the actual observed data. There are several approaches and metrics, depending on the goal of your analysis.

## Point Forecast Accuracy Metrics

These metrics compare the predicted values directly with the observed values:

- [[Mean Absolute Error]] (MAE): Measures the average magnitude of errors without considering their direction. It is simple and easy to interpret.  
- [[Mean Squared Error|MSE]]: Squares the errors to penalize larger deviations more heavily.  
- [[Root Mean Squared Error|RMSE]]: Square root of MSE; in the same units as the data and emphasizes large errors.  
- [[Mean Absolute Percentage Error|MAPE]]: Expresses errors as a percentage of the actual values, useful for understanding relative accuracy.  

These metrics provide a quick sense of overall accuracy, but they do not capture patterns in the errors.
## Residual Analysis

Residuals are the differences between the ==actual values and the predicted values==: Analyzing residuals helps identify whether the model has left any systematic patterns unexplained:

- Plot **residuals** over time to check for trends or cycles.  
- Residuals should ideally be **uncorrelated** and **approximately normally distributed**.  
- Tools for residual analysis:  
  - **ACF of residuals**: Detects any remaining autocorrelation in the errors [[ACF Plots|ACF]].  
  - **Histogram or Q-Q plot**: Checks whether residuals are roughly normally distributed [[Q-Q Plot]].  
## [[Out-of-sample rolling forecast evaluation]]

This approach tests how well the model performs on **data that was not available during training**:

- **Train-test split**: Train the model on historical data, forecast future points, and compare with actual outcomes.  
- **Rolling / walk-forward validation**: Refit the model as new data becomes available, forecast ahead, and record errors. This approach shows **how forecast accuracy evolves over time** and across different forecast horizons. Rolling evaluation mimics real-world forecasting conditions and gives a realistic estimate of forecast reliability.

## Business / Decision-Oriented Evaluation

Accuracy metrics alone are not always sufficient; forecasts should be evaluated in the context of their **practical impact**: [[Time Series Forecasts in Business]]:

- Does the forecast support decision-making?  
- Are critical thresholds or targets met?  
- For example, in energy demand forecasting, errors may translate into over- or under-supply penalties, which are more meaningful than purely numerical accuracy.  

Evaluating forecasts from a business perspective ensures that models are not only statistically sound but also operationally useful.
