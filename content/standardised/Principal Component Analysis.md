---
title: 
tags:
  - preprocessing
  - analysis
  - ml
  - data_visualization
aliases:
  - PCA
category:
---
### Overview

PCA is a powerful tool for [[Dimensionality Reduction]] in [[Unsupervised learning]] to reduce the dimensionality of data. 

It transforms the original data into a new coordinate system defined by the principal components, which are ==orthogonal vectors== that capture the most variance in the data.

It helps simplify models, enhances [[interpretability]], and improves computational efficiency by transforming data into a lower-dimensional space while ==retaining the most significant variance==, and reducing noise.
### How PCA Works

- ==Linear Technique==: PCA is a linear technique, meaning it assumes that the relationships between features are linear. This distinguishes it from methods like [[Manifold learning]] which can capture non-linear relationships.

- Principal Components: PCA identifies principal components, which are linear combinations of the original features. These components are ordered by the amount of variance they capture from the data, with the first principal component capturing the most variance, the second capturing the second most, and so on.
### Comparison with Other Techniques

- [[t-SNE]]: Unlike PCA, t-SNE is a non-linear technique used for visualization, preserving local structures in high-dimensional data.
- [[Manifold Learning]]: Techniques like Isomap and Locally Linear Embedding (LLE) are designed to capture non-linear structures, which PCA might miss due to its linear nature
#### Code Implementation
  ```python

      import pandas as pd
      from sklearn.model_selection import train_test_split
      from sklearn.decomposition import PCA
      from sklearn.linear_model import LinearRegression
      from sklearn.metrics import r2_score
      # create a dataframe with sample data
      data = {'X1':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'X2':[11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
              'X3':[21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 'y':[31, 32, 33, 34, 35, 36, 37, 38, 39, 40]}
      df = pd.DataFrame(data) 
      # split the data into training and test sets
      X = df.drop('y', axis=1)
      y = df['y']
      X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
      # apply PCA
      pca = PCA(n_components=2)
      X_train_pca = pca.fit_transform(X_train)
      X_test_pca = pca.transform(X_test)
      # train a linear regression model
      model = LinearRegression()
      model.fit(X_train_pca, y_train)
      # evaluate the model
      y_pred = model.predict(X_test_pca)
      r2_score(y_test, y_pred)
      # you should get 0.9999
```