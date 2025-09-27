---
aliases:
- SVC
category: ML
date modified: 27-09-2025
tags:
- classifier
---
## Overview

**Support Vector Classifiers (SVCs)** are a fundamental component of [[Support Vector Machines|SVM]]s, designed to find the optimal hyperplane that separates data into distinct classes. The primary objective of an SVC is to ==maximize the margin between different classes==, ensuring that the separation is as clear as possible.

## Key Concepts

- **Hyperplane**: A decision boundary that separates different classes in the feature space. In a two-dimensional space, this is a line; in higher dimensions, it becomes a plane or hyperplane.
- **Support Vectors**: The data points that are closest to the hyperplane. These points are critical as they define the position and orientation of the hyperplane.
- **Margin**: The distance between the hyperplane and the nearest data point from either class. SVC aims to maximize this margin to improve [[Classification]] robustness.

## SVC vs. SVM

- **SVC**: Primarily focuses on placing a hyperplane between datasets for separation. It is effective when the data is linearly separable.
- **SVM**: Extends the concept of SVC by using kernel functions to handle cases where data is **not linearly separable** in its original space. Kernels transform the data into a higher-dimensional space where a linear separation is possible.