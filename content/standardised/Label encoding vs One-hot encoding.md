---
aliases: 
category: ML
date modified: 27-07-2025
tags:
  - preprocessing
---
[[Label Encoding]] and [[One-hot encoding]] give different predictions because they represent categorical variables in fundamentally different ways. 

- [[Label Encoding]] might cause issues by implying an ==ordinal== relationship between categories, leading to biased predictions.
- One-Hot Encoding prevents this by treating categories independently, resulting in more accurate predictions when there's no natural order among the categories.

Key Differences in Predictions:
1. Ordinal vs. Non-Ordinal Data Representation:
    - With Label Encoding, the model might treat "Robbinsville" (encoded as 1) as closer to "West Windsor" (encoded as 0) than "Princeton" (encoded as 2), even though these categories don't have any inherent numerical relationship. This can lead the model to incorrectly infer relationships based on these numeric values.
    - With One-Hot Encoding, no such relationship is assumed. Each category is represented as a vector of 0s and 1s, and the model treats them as distinct entities, preventing any assumptions about their order.

2. Model Interpretation:
    - Label Encoding introduces an implicit ordinal relationship (e.g., 0 < 1 < 2) that can influence the model, especially for linear models like Linear Regression, which assumes that the input features are on a similar scale. This may lead to inappropriate relationships in the regression model.
    - One-Hot Encoding avoids this issue by using binary columns for each category, effectively preventing the model from assuming an ordinal relationship between the categories.

3. Feature Space:
    - Label Encoding results in a single feature column for the categorical variable.
    - One-Hot Encoding expands the feature space, creating as many columns as there are categories. In the case of a categorical feature with many unique values, this can significantly increase the dimensionality of the model.

Why Predictions Differ:
- In Label Encoding, a linear regression model might learn that "Robbinsville" is numerically closer to "West Windsor" than "Princeton," and this might distort the predictions.
- In One-Hot Encoding, the model treats each category independently, leading to different relationships being learned (if any) between the categories and the target variable.
