# Anomaly Detection

There are several ways to detect [[Outliers]]

Use visual methods like boxplots, statistical methods like Z-scores, or clustering techniques.

## Visual Methods

- [[Boxplot]]: Displays the distribution and identifies outliers using the interquartile range (IQR).
- Scatter Plot: Helps visually identify outliers.

## [[Clustering]]

- Description: Outliers often form small clusters or are isolated from main clusters.

## PCA-Based Anomaly Detection

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

## Statistical Methods

-  [[Z-Score]]: Identifies outliers by measuring how many standard deviations a data point is from the mean.
### Gaussian method

![[Pasted image 20241230202826.png|500]]