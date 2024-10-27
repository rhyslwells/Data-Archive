---
title: 
tags:
  - classifer
  - clustering
aliases:
  - SVM
category:
---
# Summary

SVM is a type of [[supervised learning]] algorithm primarily used for classification tasks, although it can also be adapted for regression. The main idea behind SVM is to find an optimal ==hyperplane== that divides data into different classes by maximizing the margin between them. The support vectors are the data points closest to the hyperplane, and these points influence the position and orientation of the hyperplane.   It ==maximizes the margin== between the classes, with the support vectors being the closest points to the hyperplane that influence its position.
####  Support Vector Classifier (SVC) vs. Support Vector Machine (SVM):

   - Support Vector Classifiers (SVCs) are the foundation of SVMs, where the goal is to place a hyperplane between datasets to separate them.

   - SVM generalizes this concept by using kernels to deal with cases where the data is ==not linearly separable in its original space==. When there is no clear linear way to separate the data, SVMs are employed. It pushes the data to higher dimension using kernelling.

#### How SVM Works:
   - Step 1: Start in the low-dimensional space, where the data may not be linearly separable.
   - Step 2: Use a kernel function to move the data into a higher dimension where the separation is clearer.
   - Step 3: Place hyperplanes (decision boundaries) between the data clusters to classify the data.
#### Margins

Outliers and Soft Margins:
   - SVM allows for some ==miscalculations== or errors in classification to handle outliers. This is known as the [[Bias and variance]] tradeoff, where the model is allowed to make a few mistakes to improve generalization.
   
   - Soft margins are a concept in SVM that allows some data points to be within the margin or even on the wrong side of the hyperplane. These points lie at the edges of data [[Clustering]], enabling the SVM to handle imperfect separations.

![[Pasted image 20240128193726.png|500]]

Soft margins are a measure of how the borders mix, softer more mixing

![[Pasted image 20240128193838.png|500]]

#### Kernelling

[[Kernelling]] is a technique where the SVM uses a kernel function to map the dataset into a higher-dimensional space, making it easier to identify separable clusters that may not be apparent in the original low-dimensional space.

 Kernel Trick:
   - When the data cannot be separated by a straight line or plane in its original (low-dimensional) space, SVM uses a technique called kernelling to project the data into a higher dimension where it becomes easier to separate.
   - The Kernel Trick allows the transformation of data into a higher dimension without explicitly computing the transformation. There are different types of kernels, with common examples being:
     - Polynomial kernel
     - Radial Basis Function (RBF) or exponential kernel

#### Advantages and disadvantages of SVM

   - Advantages: 
     - SVM is highly effective for high-dimensional data (datasets with many features).
     - It is useful for classification tasks where a clear margin of separation exists between classes.
   - Disadvantages: 
     - SVM can be computationally expensive for large datasets.
     - The performance of SVM is highly dependent on the ==Kernelling== choice, and selecting the right kernel requires careful tuning.


Support Vector Machines (SVMs):
Limitations
Can be computationally expensive for large datasets and sensitive to the choice of hyperparameters.