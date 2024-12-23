---
title: Deep Learning Overview
tags:
  - deep_learning
aliases:
  - DL
  - Neural Networks
category: Machine Learning
---
>[!Summary]
> Deep learning is a subset of machine learning that uses neural networks to process large-scale data for tasks like image and speech recognition, natural language processing, and recommendation systems. 
> 
> A neural network consists of layers of nodes where each node performs weighted sums of its inputs, applies activation functions like ReLU or sigmoid, and produces an output. 
> 
> Backpropagation is the primary algorithm for training neural networks by minimizing error through gradient descent. Regularization techniques, such as dropout, prevent overfitting. 
> 
> Popular frameworks like [[PyTorch]] and [[TensorFlow]] facilitate deep learning model development.

Questions:
- [[What is the role of gradient-based optimization in training deep learning models. ]]
- [[Explain different gradient descent algorithms, their advantages, and limitations.]]

Areas of Deep Learning:
- [[LLM]]
- [[Recurrent Neural Networks]]
- [[Convolutional Neural Networks]]
- [[Neural network|Neural Network]]

 Improving the response:
 - [[Backpropagation]] works by determining the [[Loss function]]/loss (or error) at the output and then propagating it back into the network. The weights are updated to minimize the error resulting from each neuron.
  - [[Regularisation]] techniques are used to remove/ignore nodes in the network and reduce [[Overfitting]].

>[!attention]
> - [[Overfitting]] is a significant challenge in deep learning, addressed by regularization or limiting model complexity.
> - Training deep learning models is computationally intensive, requiring high-performance hardware like GPUs.

>[!Example]
> Consider a convolutional neural network (CNN) applied to image recognition. The network uses convolutional layers to extract features like edges, followed by pooling layers to reduce dimensionality. Backpropagation adjusts the weights of the filters based on the difference between predicted and actual labels, refining the feature extraction process over several epochs.

>[!Follow up questions]
> - How does the choice of activation function affect the performance of deep learning models across different tasks?
> - What are the trade-offs between different gradient descent algorithms (e.g., SGD vs. Adam) in training neural networks?

>[!Related Topics]
> - [[Transfer Learning]]: Applying pre-trained models to new tasks.

# Notes:

Deep Learning is taking off now because we have more data and faster computation speeds.

Differences between [[Machine Learning]] (Traditional) and [[Deep Learning]]:
- [[Feature Extraction]] required for ML, DL dont need or when this is hard to do.
- DL needs more data
- DL requires high comp power.