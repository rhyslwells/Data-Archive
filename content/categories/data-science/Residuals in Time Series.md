---
aliases: []
category: DS
date modified: 27-09-2025
tags: []
---
**Residuals (Noise)  
**This is the random “leftover” part of the data, the unpredictable ups and downs that can’t be explained by trend or seasonality.  
Example: A one-time car purchase showing up in your monthly expense pattern.

Residuals may still show **temporary patterns**, such as a sales spike during a promotion or a sudden drop due to strikes or weather events.

 ## Residual Analysis: How do you know if [[ARIMA]] is good model

 - The residuals should approximate a Gaussian distribution (aka white noise).

 - Visual inspection:

     - ACF plot.: auto cor in residuals: expect no correlations

     - Histogram.

     - QQ plot. =  - White noise should ideally follow a normal distribution.

 - Statistical tests:

     - Normality.

 - &x2705; Histogram/Density plot.

 - 🤔 QQ-plot

 - &x274C; Jarque-Bera (reliable for large sample size).

 - &x274C; Shapiro-Wilk (reliable for large sample size).

     - Autocorrelation.

     - Heteroskedasticity.