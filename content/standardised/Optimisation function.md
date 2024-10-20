---
title: 
tags: 
aliases: 
category:
---
Optimisation functions vary the parameters of the model to minimize the [[Loss function]].

In short, the **loss function** defines the objective (minimizing error), while the **optimization function** determines how the model's parameters are adjusted to achieve this goal.

An **optimization function** and a **[[Loss function]]** are related but not the same. Here's a breakdown of the difference:

- **Loss Function**: This function measures how well a model's predictions match the actual target values. It ==quantifies the error between the predicted output and the true output==. Examples include [[Mean Squared Error]] (MSE) for regression and [[Cross-Entropy]] for classification. The loss function is what the model aims to minimize during training.
  
- **Optimization Function**: This is the algorithm ==used to minimize the loss function== by adjusting the model's parameters (weights and biases). The most common optimization method is [[Gradient Descent]] where the optimization function computes the gradient of the loss function with respect to the model parameters and updates them accordingly. Other optimization algorithms include [[Adam]], RMSprop, and [[Stochastic Gradient Descent]] (Stochastic Gradient Descent).

