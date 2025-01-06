Standardisation is a [[Preprocessing|data preprocessing]] technique used to [[Data Transformation]] features so that they have a mean of 0 and a standard deviation of 1. This process is essential in preparing data for various machine learning algorithms.

Definition: Standardisation involves rescaling the features of your data so that they have a mean of 0 and a standard deviation of 1. This is achieved by subtracting the mean of the feature from each data point and then dividing by the standard deviation.

Purpose: 
- Useful for algorithms that assume the data is normally distributed.
- Uniformity: It helps in bringing all features to the same scale.

### Use Case

- Centred Data Assumption: Standardisation is beneficial when the model assumes that the data is centred around zero. This is common in algorithms such as linear regression, logistic regression, and [[principal component analysis]] (PCA), and distance-based algorithms like [[K-nearest neighbours|KNN]] and [[Gradient Descent]] descent optimization.
  
- Improved Performance: It can improve the performance and convergence speed of machine learning algorithms by ensuring that each feature contributes equally to the result.
### Formula

The formula for standardisation is:

$$z = \frac{x - \mu}{\sigma}$$

Where:
- $x$ is the original data point.
- $\mu$ is the mean of the feature.
- $\sigma$ is the standard deviation of the feature.

By applying this transformation, the data becomes more suitable for training models that rely on the assumption of [[Gaussian Distribution]].

