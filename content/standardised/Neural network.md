---
aliases: [Neural Network]
category:
date modified: 1-08-2025
tags: ["#deep_learning", drafting]
---
A [[Neural network|Neural Network]] is a computational model inspired by biological neural networks in the human brain. It consists of layers of interconnected nodes (neurons) that process and transmit information. Neural networks are fundamental to [[Deep Learning]].

Resources:  
- [Keras Guide](https://keras.io/guides/sequential_model/)

Also see:  
- [[Types of Neural Networks]]  
- [[Neural network in Practice]]
### Key Components

The number of starting nodes depends on the input parameter, similar for output. The width and depth of the net are called [[Hyperparameter]].

Neurons (Nodes):  
- The basic units of a neural network. Each neuron receives input, processes it, and passes it to the next layer. A neuron’s output is typically computed using a mathematical function known as the activation function.

Layers:  
- Neural networks are structured in layers of neurons:
  - Input Layer: Receives the raw input data (features) that are fed into the network.
  - Hidden Layers: Process the inputs received from the previous layer. There can be multiple hidden layers, making a neural network "deep." These layers transform the data to learn complex relationships and patterns.
  - Output Layer: Produces the final prediction or result, such as a class label in classification tasks or a continuous value in regression.

Weights and Biases: [[Model Parameters]]
- There are weights and biases at each layer. The shape of the weights is determined by the number of units in the previous layer and the number of units in the current layer.
- Each connection between neurons has a weight that determines how much influence one neuron has on another. Weights are adjusted during the learning process to minimize prediction errors.
- Biases allow the network to shift the output of the [[activation function]] and help it better fit the data.

Training: See [[Fitting weights and biases of a neural network]]

Optimization: See [[Optimisation techniques]]
- The optimization process (often gradient descent) updates the network's weights to minimize the loss function, ensuring the model improves with training and generalizes well to new, unseen data.

Inputs:
- We need [[Normalisation]] of values (inputs) here for feeding the network to have balanced weights at the nodes.

### Context

Example of Neural Network:  
A neural network can be used for a task like image classification. For instance:
- The input layer receives the pixel values of the image.
- Hidden layers transform these pixel values through a series of mathematical operations, learning important features such as edges, shapes, and textures.
- The output layer classifies the image into one of the predefined categories (e.g., "cat" or "dog").

Pros:  
- Flexibility: Can model complex, non-linear relationships.
- Adaptability: Can be applied to a wide range of problems like image recognition, speech processing, and game playing.
- Automatic Feature Extraction: Neural networks, especially CNNs, can automatically learn important features from raw data without manual intervention.

Cons:  
- Data-hungry: Neural networks typically require large datasets to perform well.
- Computationally Intensive: Training deep networks can require substantial computational resources.
- Black Box Nature: The internal decision-making process is often difficult to interpret, although research into interpretability is addressing this.

