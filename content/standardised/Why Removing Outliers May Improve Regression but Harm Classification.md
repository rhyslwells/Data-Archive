---
aliases: 
category: ML
date modified: 27-07-2025
tags:
  - anomaly_detection
---
Removing [[Outliers]] May Improve Regression but Harm Classification

### Impact on Regression Model:

Regression models, particularly linear [[regression]], are sensitive to outliers because they attempt to minimize the sum of squared errors. By removing outliers, the model can better capture the underlying trend of the data, leading to improved performance metrics such as R-squared and reduced [[mean squared error]].

### Impact on [[Classification]] Models

- Class Boundary Distortion: Classification models, such as decision trees or support vector machines, rely on the [[Distributions|distribution]] of data points to define class boundaries. ==Outliers can provide valuable information about the variability within classes.==

- Loss of Information: Removing outliers may lead to the loss of important data points that could help in distinguishing between classes, potentially resulting in a less accurate model. For example, an outlier might represent a rare but important class that the model needs to learn from.