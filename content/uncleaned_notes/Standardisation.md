#data_analysis 

To the correct scales.

```python
from sklearn import preprocessing
df_scaled = preprocessing.scale(df) #scales each variable (column in x) with respect to itself
df_scaled# an array
```





## [[Standardisation]]

```python
# #scale inputs
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# scaler.fit(x1)
# x_scaled = scaler.transform(x1)
```



## [[Standardisation]]

When to Use Feature Scalling? 

- k-nearest neighbors with an Euclidean distance measure is sensitive to magnitudes and hence should be scaled for all features to weigh in equally. 
- Scaling is critical, while performing Principal Component Analysis(PCA). PCA tries to get the features with maximum variance and the variance is high for high magnitude features. This skews the PCA towards high magnitude features.
- We can speed up gradient descent by scaling. This is because θ will descend quickly on small ranges and slowly on large ranges, and so will oscillate inefficiently down to the optimum when the variables are very uneven

[[normalization]] Vs. [[Standardisation]]

¶ The two most discussed scaling methods are Normalization and Standardization. Normalization typically means rescales the values into a range of [0,1]. Standardization typically means rescales data to have a mean of 0 and a standard deviation of 1 (unit variance).