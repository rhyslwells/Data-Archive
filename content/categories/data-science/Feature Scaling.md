---
aliases: []
category: DS
date modified: 27-09-2025
tags:
- cleaning
- preprocessing
---
Used in preparing data for machine learning models. 

Feature Scaling is a [[Preprocessing]] step in machine learning that involves adjusting the range and distribution of feature values. 

This ensures that all features contribute equally to the model's performance, especially when they are measured on different scales, which is particularly important for distance-based algorithms, [[Principal Component Analysis]], and optimization techniques like [[Gradient Descent]]. 

By using methods like normalization and standardization, you can enhance the performance and accuracy of your models.

See sklearn.preprocessing

Examples of algorithms not affected by feature scaling are [[Naive Bayes Classifier]], [[Decision Tree]], and [[Linear Discriminant Analysis]].
### Why Use Feature Scaling?
Feature scaling is important for several reasons:

1. Distance-Based Algorithms: Algorithms like k-nearest neighbors (KNN) rely on distance measures (e.g., Euclidean distance). If features are on different scales, those with larger magnitudes will disproportionately influence the distance calculations. Scaling ensures that all features weigh equally.

2. Principal Component Analysis (PCA): PCA aims to identify the directions (principal components) that maximize variance in the data. If features have high magnitudes, they will dominate the variance calculation, skewing the results. Scaling helps to mitigate this issue.

3. Gradient Descent Optimization: In optimization algorithms like gradient descent, features with larger ranges can cause inefficient convergence. Scaling ensures that all features are on a similar scale, allowing for faster and more stable convergence to the optimal solution.

[[Feature Scaling]] is useful for models that use distances like [[Support Vector Machines|SVM]] and [[K-means]]
### When Scaling Is Unnecessary

1. Tree-based Algorithms:
    - Algorithms like [[Decision Tree]], [[Random Forest]], and Gradient Boosted Trees are invariant to feature scaling because they split data based on thresholds, not distances.
    - Example: Splits are determined by feature values, not their magnitude.
      
2. Data with Uniform Scales:
    - If all features have the same range or are already normalized (e.g., percentages), scaling may not be required.

### Common Scaling Methods
- [[Normalisation]]
- [[Standardisation]]

Min-Max Scaling: Scales features to a fixed range (e.g., $[0, 1]$), preserving relative distances.
### Example of Scaling
Here’s how you can scale a DataFrame using the `scale` function from `sklearn`:

```python
from sklearn import preprocessing
df_scaled = preprocessing.scale(df)  # Scales each variable (column) with respect to itself
```

This returns an array where each feature is standardized.

### Note:
- Scaling is done when one feature is at a significantly different scale.
- For each data point, subtract the mean and divide by the range (max-min).

![[Pasted image 20241224083928.png]]