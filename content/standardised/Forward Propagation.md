---
aliases: [feedforward pass, forward pass]
category: DS
date modified: 27-07-2025
tags: [deep_learning, statistics]
title: Forward Propagation in Neural Networks
---

>[!Summary]  
> Forward propagation is the process by which input data moves through a neural network, layer by layer, to produce an output. During this process, each layer’s weights and biases are applied to the input data, and an activation function is used to transform the data at each layer. 
> 
> Mathematically, for each layer, the input $x$ is transformed into an output $y$ through the equation $y = f(Wx + b)$, where $W$ represents the weights, $b$ is the bias, and $f$ is the activation function (e.g., ReLU, sigmoid). The output from one layer becomes the input to the next, and this continues until the final layer produces the predicted output. 
> 
> This process does not involve learning; it only ==computes the prediction based on current weights.==

>[!Breakdown]  
> Key Components:  
> - Input data: Initial values fed into the network.  
> - Weights ($W$) and biases ($b$): Parameters adjusted during training.  
> - Activation function: Non-linear transformation, e.g., ReLU or sigmoid.  
> - Output: Prediction made by the network.

>[!important]  
> - Forward propagation calculates predictions ==by applying current model parameters== to inputs.  
> - It is the first step before backpropagation, where the error is used to adjust weights.

>[!attention]  
> - Forward propagation does not involve ==learning or updating weights.==  
> - The accuracy of forward propagation depends entirely on the current values of weights and biases.

>[!Example]  
> In a simple neural network with one hidden layer, forward propagation can be described as:  
> $$ z_1 = W_1 x + b_1 $$  
> $$ a_1 = \text{ReLU}(z_1) $$  
> $$ z_2 = W_2 a_1 + b_2 $$  
> $$ y = \text{sigmoid}(z_2) $$  
> Here, $x$ is the input, and $y$ is the output prediction.

>[!Follow up questions]  
> - How does the choice of [[activation function]] impact the forward propagation process?  
> - In deep networks, how can [[vanishing and exploding gradients problem]] during forward propagation affect training?

>[!Related Topics]  
> - [[Backpropagation]] in neural networks  
> - Activation functions in deep learning