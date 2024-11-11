---
title: 
tags:
  - deep_learning
  - classifier
aliases:
  - FFNN
category:
---
A **Feedforward Neural Network (FFNN)** is the simplest type of [[Neural network]].

In this model, information moves in ==one direction==—from the input layer, through the hidden layers, to the output layer—without any loops or backward connections. 

This straightforward design is primarily used for [[supervised learning]] tasks.

- **Structure**: Information flows in one direction (input → hidden layers → output).
- **Learning**: FFNNs learn by adjusting weights and biases during training to minimize the [[Loss function]].
- **Limitations**: ==Cannot handle sequential data== and may struggle with complex data without deeper architectures.

### Key Features of a Feedforward Neural Network:
1. **Layers**:
   - **Input Layer**: The input layer consists of nodes (neurons) that receive the raw data. Each node in this layer represents a feature of the input data.
   - **Hidden Layer(s)**: These layers lie between the input and output layers and are responsible for learning complex patterns in the data. The number of hidden layers and the number of neurons in each layer are design choices that affect the network’s performance.
   - **Output Layer**: This layer produces the final prediction or classification. The number of neurons in this layer depends on the specific task (e.g., one neuron for binary classification, multiple neurons for multi-class classification).

2. **Neurons**:
   - Each neuron in the network receives inputs from the previous layer, processes these inputs using a **weighted sum**, adds a **bias**, and applies a **nonlinear activation function**. This allows the network to learn non-linear relationships between inputs and outputs.

3. **Activation Functions**: [[Activation Function]]
   - The activation function introduces non-linearity into the network, allowing it to model complex relationships. Common activation functions include:


1. [[Forward Propagation]]
   - In feedforward networks, information flows in one direction during **forward propagation**: input data is passed through the network, processed by each layer, and an output is produced.
   - No information or weights are shared between layers, unlike recurrent neural networks (RNNs) where the model maintains memory of past inputs.

2. **Loss Function and Optimization**:
   - The **loss function** quantifies how far the network’s output is from the actual target value. Common loss functions include **mean squared error (MSE)** for regression tasks and **cross-entropy loss** for classification tasks.
   - The network’s weights and biases are updated through **backpropagation** and **gradient descent** to minimize the loss function and improve performance. This is done iteratively, adjusting the network's parameters based on the gradient of the loss function with respect to those parameters.

3. **Training**:
   - FFNNs are trained using a dataset where both the input features and target outputs (labels) are known. During training, the model makes predictions, calculates the loss, and adjusts its weights to minimize the error over time.

### Example of a Simple Feedforward Neural Network:
Consider a binary classification task with a feedforward neural network:
- **Input Layer**: 3 neurons (representing 3 features from the dataset)
- **Hidden Layer**: 2 neurons with ReLU activation
- **Output Layer**: 1 neuron with sigmoid activation to produce a probability for the binary classification (e.g., class 0 or class 1)

Each input is connected to the neurons in the hidden layer, and the hidden layer is connected to the output layer. Forward propagation moves from the input layer to the output, computing the final prediction. During backpropagation, the error is used to adjust weights and biases to improve future predictions.
### Limitations:
- **Shallow vs. Deep Networks**: Simple feedforward networks with only a few hidden layers (shallow networks) may struggle to learn complex, hierarchical representations of data. Deeper networks (deep feedforward networks) with many layers can model more complex patterns but require more data and computational resources to train.
- **[[Overfitting]]**: FFNNs can overfit on the training data, especially if they have many parameters and not enough regularization (e.g., dropout, L2 regularization).
- ==**No Temporal Understanding**==: Unlike [[RNNs]] or transformers, FFNNs cannot model sequential dependencies in data. They are better suited for static, non-sequential tasks.



