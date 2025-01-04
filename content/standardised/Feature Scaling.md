---
title: 
tags:
  - data_cleaning
  - data_processing
category: Data Science
phase: preprocess
---
Used in preparing data for machine learning models. 

**Feature Scaling** is a preprocessing step in machine learning that involves adjusting the range and distribution of feature values. 

This ensures that all features contribute equally to the model's performance, especially when they are measured on different scales, which is particularly important for distance-based algorithms, [[Principal Component Analysis]], and optimization techniques like [[Gradient Descent]]. 

By using methods like normalization and standardization, you can enhance the performance and accuracy of your models.

Examples of algorithms not affected by feature scaling are [[Naive Bayes]], [[Decision Tree]], and [[Linear Discriminant Analysis]].
### Why Use Feature Scaling?
Feature scaling is important for several reasons:

1. **Distance-Based Algorithms**: Algorithms like k-nearest neighbors (KNN) rely on distance measures (e.g., Euclidean distance). If features are on different scales, those with larger magnitudes will disproportionately influence the distance calculations. Scaling ensures that all features weigh equally.

2. **Principal Component Analysis (PCA)**: PCA aims to identify the directions (principal components) that maximize variance in the data. If features have high magnitudes, they will dominate the variance calculation, skewing the results. Scaling helps to mitigate this issue.

3. **Gradient Descent Optimization**: In optimization algorithms like gradient descent, features with larger ranges can cause inefficient convergence. Scaling ensures that all features are on a similar scale, allowing for faster and more stable convergence to the optimal solution.

### Common Scaling Methods
The two most discussed methods for feature scaling are:

- **[[Normalisation]]**: ==Rescales the feature values== to a range of [0, 1]. This is useful when you want to ensure that all features contribute equally to the distance calculations.

    ```python
    from sklearn.preprocessing import MinMaxScaler

    scaler = MinMaxScaler()
    df_normalized = scaler.fit_transform(df)  # Rescales each feature to [0, 1]
    ```

- **[[Standardisation]]**: ==Rescales the data to have a mean of 0 and a standard deviation of 1== (unit variance). This method is particularly useful when the data follows a Gaussian distribution.

    ```python
    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()
    df_standardized = scaler.fit_transform(df)  # Rescales each feature to have mean 0 and std deviation 1
    ```

### Example of Scaling
Here’s how you can scale a DataFrame using the `scale` function from `sklearn`:

```python
from sklearn import preprocessing

df_scaled = preprocessing.scale(df)  # Scales each variable (column) with respect to itself
```

This will return an array where each feature has been standardized.

Apply normalization or standardization to ensure that features have a similar scale (this is important for algorithms sensitive to scaling, though linear regression can handle unscaled features in some cases).