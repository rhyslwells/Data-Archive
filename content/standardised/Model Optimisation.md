---
aliases: [Optimisation]
category:
date modified: 1-08-2025
tags: [drafting]
---
Model optimization is a step in the machine learning workflow aimed at enhancing a model's performance by fine-tuning its parameters and hyperparameters. The goal is to improve the model's accuracy, efficiency, and ability to generalize to new data. 
### Purpose:
- Accuracy: Improve the model's predictive performance.
- Efficiency: Ensure the model runs efficiently in terms of computation and resource usage.
- Generalization: Enhance the model's ability to perform well on unseen data, avoiding overfitting.

### Process:
0. [[Model Parameters]] tuning

1. [[Hyperparameter|Hyperparameter tuning]]
   - Adjust hyperparameters such as learning rate, number of layers in a neural network, and regularization strength to find the optimal configuration.
   - Techniques like grid search, random search, or Bayesian optimization can be used for this purpose.

2. [[Feature Engineering]]
   - Involves selecting, transforming, or creating new features that can improve model performance.
   - This step can significantly impact the model's ability to learn patterns from the data.

3. [[Model Evaluation]]
   - Evaluate the model using appropriate metrics based on the problem type (e.g., classification or regression).
   - Metrics for classification include accuracy, precision, recall, F1-score, and confusion matrix.
   - Metrics for regression include [[Mean Absolute Error]] (MAE), Mean Squared Error (MSE), [[Root Mean Squared Error]] (RMSE), and R-squared (R²).

4. [[Cross Validation]]
   - A technique to assess the model's performance by splitting the data into multiple subsets for training and testing.
   - Helps in detecting overfitting and provides reliable performance estimates.

5. [[Model Ensemble]]: Combining models to get better performance