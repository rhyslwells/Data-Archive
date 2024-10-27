---
tags:
  - "#analysis"
  - statistics
  - drafting
  - anomaly_detection
aliases:
  - anomalies
---

There are different ways to clip outliers:

1. **Trimming**: Removing data points that are identified as outliers based on some criteria, such as being beyond a certain number of standard deviations from the mean or falling outside a specified percentile range. This effectively "clips" the dataset by discarding the extreme values.
    
2. **Capping or Flooring**: Setting a maximum or minimum threshold beyond which data points are considered outliers and replacing them with the threshold value. This approach ensures that extreme values are retained but are capped at a certain level.
    
3. **Winsorizing**: Similar to capping and flooring, winsorizing involves replacing extreme values with less extreme values within a specified range. Instead of setting a fixed threshold, winsorizing replaces outliers with values at a certain percentile of the dataset.
## Description

For example, you might decide to consider values below the 1st percentile or above the 99th percentile as potential outliers.

need to go through each feature.
```python
lower_quantile = df["var1"].quantile(0.01)
upper_quantile = df["var1"].quantile(0.99)
df_no_outliers = df[(df["var1"] >= lower_quantile) & (df["var1"] <= upper_quantile)]

# visualise and pick a reasonable bound
sns.distplot(df['EngineV'])
df.describe(include='all')
```

## Q&As

What is the issue with [[Outliers]] in [[Model Deployment]]?;;Can sway the generality of the model. Statistically the sway the mean and increase the standard deviation.

How can [[Outliers]] be detected?
?
- Use a [[Boxplot]] which displays the distribution (IQR),
- visually determine a theresold in a plot,
- Or use a Z-score stastistically.
- Use [[clustering]], outliers will be in small clusters.


### Detection

`outForest` is a multivariate anomaly detection method. Each numeric variable is regressed onto all other variables using a random forest. If the scaled absolute difference between observed value and out-of-bag prediction is larger than a prespecified threshold, then a value is considered an outlier.

A benefit of this technique is noise reduction, at least at the most anomylous observations. A drawback is of applying it at this point to the training data and the cross validation folds is that the CV out of sample estimates of error are smaller than we would see with raw.

Computationally, it is faster to run it here.

```python
def pca_anamolies(data):
    data_pure=data.copy()
    drop_cols=[f for f in data_pure.columns if f in target]

    features = data_pure.drop(columns=drop_cols)

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    pca = PCA(n_components=2)  # Choose the number of components for visualization
    principal_components = pca.fit_transform(scaled_features)

    # Calculate the reconstruction error (MSE) for each data point
    reconstruction_errors = ((scaled_features - pca.inverse_transform(principal_components)) ** 2).mean(axis=1)

    # Set a threshold for anomaly detection
    threshold = 3.5 # Adjust the threshold based on your data and desired sensitivity

    # Identify potential outliers
    potential_outliers = [index for index, error in enumerate(reconstruction_errors) if error > threshold]

    # Create a new column 'outliers' in the DataFrame
    data_pure['outliers_PCA'] = False
    data_pure.loc[potential_outliers, 'outliers_PCA'] = True

    print(f"Number of detected Potential outliers: {len(potential_outliers)}")
    
    data_clean=data[~data_pure['outliers_PCA']]
    print(data_clean.shape)

    # Plot the data with potential outliers highlighted
    plt.scatter(principal_components[:, 0], principal_components[:, 1], c='green', label='Normal Data')
    plt.scatter(principal_components[potential_outliers, 0], principal_components[potential_outliers, 1], c='red', label='Potential Outliers')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend()
    plt.title('PCA with Potential Outliers')
    plt.show()
    return data_clean
```
### Handling outliers

Outlier handling is a technique for removing outliers from a data set. This method can be used on a variety of scales to produce a more accurate data representation. This has an impact on the model’s performance. Depending on the model, the effect could be large or minimal. For example, [[Linear Regression]] is particularly susceptible to outliers. This procedure should be completed prior to model training. The various methods of handling outliers include:

1. **Removal**: Outlier-containing entries are deleted from the distribution. However, if there are outliers across numerous variables, this strategy may result in a big chunk of the datasheet being missed.
2. **Replacing values**: Alternatively, the outliers could be handled as missing values and replaced with suitable imputation.


outliers
How to find outliers in a dataset?;; Use scatter plot, boxplot, IQR

- Objective: Identify and handle outliers in the dataset that could disproportionately affect the model's predictions. Outliers can lead to skewed predictions, especially in linear models.
    
- Techniques:
    
    - Outlier Removal: Detect and remove extreme outliers.
        
    - Robust Scaler: Use robust scaling methods that are less sensitive to outliers (e.g., scaling based on interquartile range).
        
    - Term: 
        
    
    python
    
    Copy code
    
    `from sklearn.preprocessing import RobustScaler scaler = RobustScaler() X_train_scaled = scaler.fit_transform(X_train)`



#### [[Outliers]]

- Objective: Identify and handle outliers in the dataset that could disproportionately affect the model's predictions. Outliers can lead to skewed predictions, especially in linear models.
    
- Techniques:
    
    - Outlier Removal: Detect and remove extreme outliers.
        
    - Robust Scaler: Use robust scaling methods that are less sensitive to outliers (e.g., scaling based on interquartile range).
        
    - Term: #data_cleaning #preprocessing
        
    
    python
    
    Copy code
    
    `from sklearn.preprocessing import RobustScaler scaler = RobustScaler() X_train_scaled = scaler.fit_transform(X_train)`

- Objective: Identify and handle outliers in the dataset that could disproportionately affect the model's predictions. Outliers can lead to skewed predictions, especially in linear models.
    
- Techniques:
    
    - Outlier Removal: Detect and remove extreme outliers.
        
    - Robust Scaler: Use robust scaling methods that are less sensitive to outliers (e.g., scaling based on interquartile range).
        
    - Term: #data_cleaning #preprocessing
        
    
    python
    
    Copy code
    
    `from sklearn.preprocessing import RobustScaler scaler = RobustScaler() X_train_scaled = scaler.fit_transform(X_train)`