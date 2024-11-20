---
tags: 
aliases: 
category:
---
Time series forecasting is one of the most common ML problems faced in industry. It’s easy to get started, but finding the right model isn't easy.  
  
What models to use
  
When you’ve got few data points per time series or need long term forecasts: use statistical models like ARIMA / SARIMA / SARIMAX or even prophet. 

AutoARIMA from the statsforecast library built by [Nixtla](https://www.linkedin.com/company/nixtlainc/). It’s great, optimised and super easy to use!  
  
When you’ve got a larger dataset, use boosting algorithms like [[XGBoost]] or [[LightGBM]] since those algorithms are often more powerful. The downside is that you'll need to spend more time engineering features (i.e lags).


