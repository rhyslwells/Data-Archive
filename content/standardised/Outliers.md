---
tags:
  - statistics
  - anomaly_detection
  - data_cleaning
aliases:
  - anomalies
  - Handling Outliers
---

Outliers are data points that differ significantly from other observations in the dataset. They can skew and mislead the training of machine learning models, especially those sensitive to the scale of data, such as [[Linear Regression]].

Handling outliers in similar to [[Handling Missing Data]]

## Methods for Handling Outliers

### 1. Trimming

- Description: Removing data points identified as outliers based on criteria such as being beyond a certain number of standard deviations from the mean or outside a specified percentile range.
- Implementation Example:
  ```python
  lower_quantile = df["var1"].quantile(0.01)
  upper_quantile = df["var1"].quantile(0.99)
  df_no_outliers = df[(df["var1"] >= lower_quantile) & (df["var1"] <= upper_quantile)]
  ```

### 2. Capping or Flooring

- Description: Setting a maximum or minimum threshold beyond which data points are considered outliers and replacing them with the threshold value.

### 3. Winsorizing 

- Description: Similar to capping and flooring, winsorizing replaces extreme values with less extreme values within a specified range, typically using percentiles.

## Detection Techniques

Use visual methods like boxplots, statistical methods like Z-scores, or clustering techniques.

### 1. Visual Methods

- [[Boxplot]]: Displays the distribution and identifies outliers using the interquartile range (IQR).
- Scatter Plot: Helps visually identify outliers.

### 2. Statistical Methods

-  [[Z-Score]]: Identifies outliers by measuring how many standard deviations a data point is from the mean.
### 3. [[Clustering]]

- Description: Outliers often form small clusters or are isolated from main clusters.

### 4. PCA-Based Anomaly Detection

- Implementation Example:
  ```python
  from sklearn.decomposition import PCA
  from sklearn.preprocessing import StandardScaler
  import matplotlib.pyplot as plt

  def pca_anomalies(data):
      scaler = StandardScaler()
      scaled_features = scaler.fit_transform(data)
      pca = PCA(n_components=2)
      principal_components = pca.fit_transform(scaled_features)
      reconstruction_errors = ((scaled_features - pca.inverse_transform(principal_components))  2).mean(axis=1)
      threshold = 3.5
      potential_outliers = [index for index, error in enumerate(reconstruction_errors) if error > threshold]
      data['outliers_PCA'] = False
      data.loc[potential_outliers, 'outliers_PCA'] = True
      plt.scatter(principal_components[:, 0], principal_components[:, 1], c='green', label='Normal Data')
      plt.scatter(principal_components[potential_outliers, 0], principal_components[potential_outliers, 1], c='red', label='Potential Outliers')
      plt.xlabel('Principal Component 1')
      plt.ylabel('Principal Component 2')
      plt.legend()
      plt.title('PCA with Potential Outliers')
      plt.show()
      return data[~data['outliers_PCA']]
  ```


