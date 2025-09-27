---
aliases: []
category: ML
date modified: 27-09-2025
tags:
- classifer
- mlprocess
- regressor
---
CART stands for Classification and Regression Trees. It is one of the most widely used algorithms for building decision trees.

Breakdown:

- Decision Trees: These are tree-like structures where internal nodes represent tests on features, branches represent outcomes of those tests, and leaves represent the predicted class (classification) or predicted value (regression).
  
- CART Algorithm:
    - It can handle both classification (predicting categories) and regression (predicting continuous values).
    - For classification, CART uses Gini Impurity (sometimes entropy) to measure the "purity" of splits.
    - For regression, CART uses Mean Squared Error (MSE) or Mean Absolute Error (MAE) as the splitting criterion.
    - CART builds the tree recursively:
        1. Choose the feature and split point that best separates the data according to the criterion.
        2. Partition the dataset into two child nodes.
        3. Repeat the process until a stopping condition (e.g., max depth, min samples per leaf) is reached.
    - CART always creates binary splits (each node splits into two children), unlike some older decision tree methods (like ID3 or C4.5) which can create multiway splits.

- Advantages:
    - Handles numerical and categorical data.
    - Easy to interpret and visualize.
    - Works for both classification and regression tasks.

- Limitations:
    - Can overfit easily (high variance).
    - Sensitive to small changes in data.
    - Requires pruning or ensemble methods (Random Forest, Gradient Boosted Trees) to generalize well.

Example:
- Classification: Predicting if a customer will churn (yes/no).
- Regression: Predicting house prices given features like size, location, and number of rooms.

