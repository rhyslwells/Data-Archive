---
title: 
tags:
  - deep_learning
  - classifier
aliases:
  - FFNN
category:
---
A **Feedforward Neural Network (FFNN)** is the simplest type of [[Neural network]]. In this model, connections between neurons do not form a cycle, allowing data to flow in one direction—from the input layer, through the hidden layers, to the output layer—without any loops or backward connections. This straightforward design is primarily used for [[supervised learning]] tasks.

### Structure
- Information flows in one direction: input → hidden layers → output.
- During **[[forward propagation]]**, input data is passed through the network, processed by each layer, and an output is produced.
- Unlike [[recurrent neural networks]] (RNNs), FFNNs do not share information or weights between layers, meaning the model does not maintain memory of past inputs.

### Learning
- FFNNs learn by adjusting weights and biases during training to minimize the [[Loss function]].

### Limitations
- **Shallow vs. Deep Networks:** Simple feedforward networks with only a few hidden layers (shallow networks) may struggle to learn complex, hierarchical representations of data. Deeper networks (deep feedforward networks) with many layers can model more complex patterns but require more data and computational resources to train.
- **[[Overfitting]]:** FFNNs can overfit on the training data, especially if they have many parameters and not enough regularization (e.g., dropout, [[Ridge|L2]] regularization).
- **No Temporal Understanding:** Unlike [[Recurrent Neural Networks]] or transformers, FFNNs cannot model sequential dependencies in data. They are better suited for static, non-sequential tasks.