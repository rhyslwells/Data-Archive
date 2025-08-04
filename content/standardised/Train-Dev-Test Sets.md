---
aliases: 
category: ML
date modified: 1-08-2025
tags:
  - modeling
---
In [[Model Building]] , we can train the model using the prepared data to learn patterns and make predictions. The model is trained on your dataset, which is typically divided into three main subsets: training, development (dev), and test sets.
### Purpose of Each Set

- Training Set ([[training data]]) : Used to fit the model. This is where the model learns the patterns and relationships within the data. The majority of the data is allocated here to ensure the model has enough information to learn effectively.

- Development (Dev) Set: Also known as the [[validation data]], it is used to tune the [[Model Parameters]] and make decisions about model architecture. It helps in preventing overfitting by providing a separate dataset to evaluate the model's performance during training.

- Test Set: Used to evaluate the final model's performance/ [[Model Evaluation]]. This set is not used during the training process and provides an unbiased evaluation of the model's ability to generalize to new, unseen data.

### Why do it this way

**Preventing Overfitting**: By monitoring performance on the validation set, practitioners can detect overfitting early and take corrective actions, such as adjusting model complexity or applying regularization techniques.

**[[Hyperparameter Tuning]]**: The validation set is crucial for tuning hyperparameters (e.g., [[learning rate]], regularization strength) to optimize model performance.

Historical Suggestions
- Train-Test Sets: 70% training, 30% testing.
- Train-Dev-Test: 60% training, 20% development, 20% testing.

Modern Approach
- With larger [[Datasets]], a split of 98% training, 1% development, and 1% testing is often used. This is because modern models require more data to learn effectively, and larger datasets allow for smaller proportions to be allocated to dev and test sets while still maintaining sufficient data for evaluation.

Code Example
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(inputs, target, test_size=0.3)
```

Considerations
- Data Setup: Be careful when setting up the training and test data to ensure they are ==representative== of the problem domain.
- ==[[Distributions]]: Dev and test sets should be from the same distribution to ensure consistent [[evaluation metrics]]. Avoid having subsets that are biased, such as data from the same geographical area.==
- [[Handling Different Distributions]]: Randomly shuffle the data before splitting to ensure that each subset is representative of the whole dataset.
- [[Cross Validation]]: Consider using cross-validation techniques to make the most of your data, especially when the dataset is small.

Related:
- [[Scikit-Learn]]


