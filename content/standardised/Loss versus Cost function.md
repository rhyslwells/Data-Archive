---
aliases: []
category: ML
date modified: 27-07-2025
tags: [optimisation]
---
In machine learning, the terms "loss function" and "cost function" are often used interchangeably, but they can have slightly different meanings depending on the context:

1. [[Loss function]]: This typically refers to the function that measures the error for a single training example. It quantifies how well or poorly the model is performing on that specific example - data point. Common examples include Mean Squared Error (MSE) for regression tasks and Cross-Entropy Loss for classification tasks.

2. [[Cost Function]]: This is generally used to refer to the average of the loss function over the entire training dataset. It provides a measure of how well the model is performing overall. 
   
   The cost function is what is minimized during the training process to improve the model's performance, see [[Model Optimisation|Optimisation]]. Used with the parameters to determine the best ones.

[[Model parameters vs hyperparameters]]
