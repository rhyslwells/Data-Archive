---
aliases: []
category: STATISTICS
date modified: 27-09-2025
tags:
- preprocessing
---
Standardisation is a [[Preprocessing|data preprocessing]] technique used to [[Data Transformation]]. Centers data with zero mean and unit [[Variance]], suitable for algorithms sensitive to variance.

Definition: Standardisation involves rescaling the features of your data so that they have ==a mean of 0 and a standard deviation of 1==. This is achieved by subtracting the mean of the feature from each data point and then dividing by the standard deviation.

Purpose: 
- Useful for algorithms that assume the data is normally distributed ([[Gaussian Distribution]].
- Uniformity: It helps in bringing all features to the same scale.

### Use Case

- Centred Data Assumption: Standardisation is beneficial when the model assumes that the data is centred around zero. This is common in algorithms such as linear regression, logistic regression, and [[Principal Component Analysis]] (PCA), and distance-based algorithms like [[K-nearest neighbours|KNN]] and [[Gradient Descent]] descent optimization.
  
- Improved Performance: It can improve the performance and convergence speed of machine learning algorithms by ensuring that each feature contributes equally to the result.
### Formula

The formula for standardisation is:

$$z = \frac{x - \mu}{\sigma}$$

Where:
- $x$ is the original data point.
- $\mu$ is the mean of the feature.
- $\sigma$ is the standard deviation of the feature.

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df_standardized = scaler.fit_transform(df)  # Rescales each feature to have mean 0 and std deviation 1
```
