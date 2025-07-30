---
aliases: []
category:
date modified: 27-07-2025
tags: []
---
The concept of a Cost Function is central to [[Model Optimisation]], particularly in training models.

A cost function, also known as a loss function or error function, is a mathematical function used in optimization and machine learning to measure the difference between predicted values and actual values. It quantifies the error or "cost" of a model's predictions. The goal of many machine learning algorithms is to minimize this cost function, thereby improving the accuracy of the model. Common examples of cost functions include [[Mean Squared Error]] (MSE) for regression tasks and Cross-Entropy Loss for classification tasks.

1. Relation to [[Loss Function]]: The cost function is related to the loss function. While the loss function measures the error for a single data point, the cost function typically aggregates these errors over the entire dataset, often by taking an average. See [[Loss versus Cost function]].

3. Parameter Space ([[Model Parameters]]) and Surface Plotting: By plotting the cost function over the parameter space, you can visualize how different parameter values affect the cost. This surface can have various peaks and valleys representing different levels of error.

4. [[Gradient Descent]]: This is an optimization algorithm used to find the minimum of the cost function. By iteratively adjusting the parameters in the direction that reduces the cost, gradient descent helps in finding the optimal parameters for the model.

5. Caveats: The cost function is dependent on the dataset and may not always have an explicit formula. This means that the shape of the cost function surface can vary greatly depending on the data, and finding the global minimum can be challenging.



![[Pasted image 20241216202825.png|500]]

![[Pasted image 20241216202917.png|500]]


**[[Reward Function]]**: Mentioned as the opposite of a cost function, typically used in [[Reinforcement learning]] to indicate the desirability of an outcome.