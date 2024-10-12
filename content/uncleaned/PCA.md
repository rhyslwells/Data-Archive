---
title: 
tags:
  - preprocessing
  - analysis
  - ml
aliases: 
category:
---
PCA - [[Unsupervised learning]]

is a linear technique ,unlike [[Manifold learning]]

[[What is Dimension reduction]]
A: involves reducing the number of features in a dataset while retaining its essential information.

[[Explain the curse of dimensionality]]

Give an example of Dimension reduction
[[PCA]] i.e. Principal Component Analysis (PCA) is a common technique that identifies orthogonal axes representing the most significant variance in the data.

Apply Principal Component Analysis (PCA) to reduce the dimensionality of a dataset and then train a machine learning model on the reduced data. Compare the model's performance before and after dimensionality reduction.

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

![[Pasted image 20240128194148.png|500]]





[[PCA]]
Principal Component Analysis ([[PCA]]): 

PCA finds the principal components, which are linear combinations of the original features that capture the most variance.