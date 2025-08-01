---
aliases: [anomalies, Handling Outliers]
category:
date modified: 27-07-2025
tags: [anomaly_detection, cleaning, statistics]
---
What are they?
- Outliers are data points that differ significantly from other observations in the dataset. 
- Outliers are not just points that are *far* from the mean or *visually strange*.

Their effects:
- They can skew and mislead the training of machine learning models, especially those sensitive to the scale of data, such as [[Linear Regression]]. 
- They can sway the generality of the model, skewing predictions and increasing the standard deviation.

Related Concepts:
- [[Anomaly Detection]]
- [[Methods for Handling Outliers]] similar to [[Handling Missing Data]]
- [[Why Removing Outliers May Improve Regression but Harm Classification]]
- [[Business value of anomaly detection]]