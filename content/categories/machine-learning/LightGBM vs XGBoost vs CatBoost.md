---
aliases:
- null
category: ML
date modified: 27-09-2025
tags:
- ml
---
This table summarizes the key differences and strengths of each [[Gradient Boosting]] framework.

| Feature/Aspect                    | [[LightGBM]] (LGBM)                                                        | [[XGBoost]]                                                                     | [[CatBoost]]                                                           |
| --------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Tree Growth Strategy          | Leaf-wise growth, leading to deeper trees and potentially better accuracy. | Level-wise growth, resulting in more balanced trees.                            | Ordered boosting, reducing overfitting and improving generalization.   |
| Speed and Memory              | High speed and low memory usage, especially with large datasets.           | Balanced speed and accuracy with robust regularization options.                 | Competitive performance with minimal hyperparameter tuning.            |
| Handling Categorical Features | Requires preprocessing (e.g., [[Label encoding]]).                             | Requires preprocessing of categorical features.                                 | Natively handles categorical features without preprocessing.           |
| [[Regularisation]]            | Supports regularization but not as robust as XGBoost.                      | Strong regularization options (L1 and L2) to prevent overfitting.               | Utilizes techniques like ordered boosting to mitigate overfitting.     |
| Use Cases                     | Ideal for large datasets and when computational efficiency is a priority.  | Suitable for structured data and tabular datasets; widely used in competitions. | Useful for datasets with many categorical features and missing values. |
| Performance                   | Fast training and efficient on large datasets.                             | Accurate and flexible, often used in competitions.                              | Provides competitive performance, especially with categorical data.    |

