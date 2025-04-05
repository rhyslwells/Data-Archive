---
tags:
  - statistics
  - data_cleaning
aliases:
  - anomalies
  - Handling Outliers
---
Outliers are data points that differ significantly from other observations in the dataset. They can skew and mislead the training of machine learning models, especially those sensitive to the scale of data, such as [[Linear Regression]]. They can sway the generality of the model, skewing predictions and increasing the standard deviation.

Related Concepts:
- Handling outliers in similar to [[Handling Missing Data]]
- [[Methods for Handling Outliers]]
- [[Anomaly Detection]]

#### Why Removing Outliers May Improve Regression but Harm Classification

1. Impact on Regression Model: Regression models, particularly linear regression, are sensitive to outliers because they attempt to minimize the sum of squared errors. By removing outliers, the model can better capture the underlying trend of the data, leading to improved performance metrics such as R-squared and reduced mean squared error.

1. Impact on Classification Models
    - Class Boundary Distortion: Classification models, such as decision trees or support vector machines, rely on the distribution of data points to define class boundaries. ==Outliers can provide valuable information about the variability within classes.==
    - Loss of Information: Removing outliers may lead to the loss of important data points that could help in distinguishing between classes, potentially resulting in a less accurate model. For example, an outlier might represent a rare but important class that the model needs to learn from.