---
title: 
tags:
  - "#question"
  - "#deep_learning"
importance: 6
engagement: 7
recency_of_interest: 2024-09-28
aliases:
  - Neural Network
---


>[!Summary]
> A [[Neural network|Neural Network]] **neural net**) is a computational model inspired by the way biological neural networks in the human brain work. It consists of layers of interconnected nodes (also called neurons) that process and transmit information. Neural networks are fundamental to [[Deep Learning]]a subset of machine learning, and are used to recognize patterns, make predictions, and solve complex problems.

>[!Example]
>   neural network can be used for a task like image classification. For instance:
>  - The **input layer** receives the pixel values of the image.
>  - **Hidden layers** transform these pixel values through a series of mathematical operations, learning important features such as edges, shapes, and textures.
>  - The **output layer** classifies the image into one of the predefined categories (e.g., "cat" or "dog").

### Key Concepts of Neural Networks:

1. **Neurons (Nodes)**:
   - The basic units of a neural network. Each neuron receives input, processes it, and passes it to the next layer. A neuron’s output is typically computed using a mathematical function known as the **activation function**.

2. **Layers**:
   - Neural networks are structured in layers of neurons:
     - **Input Layer**: Receives the raw input data (features) that are fed into the network.
     - **Hidden Layers**: Process the inputs received from the previous layer. There can be multiple hidden layers, and this is what makes a neural network "deep." These layers transform the data to learn complex relationships and patterns.
     - **Output Layer**: Produces the final prediction or result, such as a class label in classification tasks or a continuous value in regression.

3. **Weights and Biases**:
   - Each connection between neurons has a weight that determines how much influence one neuron has on another. Weights are adjusted during the learning process to minimize the error in predictions.
   - Biases allow the network to shift the output of the activation function and help it better fit the data.

4. [[Activation Function]]:
   - An activation function introduces ==non-linearity== to the model, enabling the neural network to learn complex patterns. Popular activation functions include:
     - **[[ReLU]] (Rectified Linear Unit)** : Outputs zero for negative inputs and the input value itself for positive inputs.
     - **[[Sigmoid]]**: Squashes the input to a range between 0 and 1.
     - **Tanh**: Squashes the input to a range between -1 and 1.

5. **Training**:
   - Neural networks learn by adjusting weights and biases through a process called **[[backpropagation]]**, which works in conjunction with an optimization algorithm like **[[Gradient Descent]]**
   - The process of training involves:
     - [[Forward Propagation]]: Input data flows through the network to produce a prediction.
     - **[[Loss Function]]**: The difference between the predicted output and the actual output (error) is calculated using a loss function (e.g., mean squared error for regression or cross-entropy loss for classification).
     - **[[Backpropagation]]**: The error is propagated backward through the network, updating the weights and biases to reduce the error in future iterations.

6. **Optimization**:
   - The optimization process (often gradient descent) updates the network's weights to minimize the loss function. This step ensures the model improves with training and generalizes well to new, unseen data.

### Types of Neural Networks:

1. **Feedforward Neural Network (FNN)**:
   - The simplest type of neural network where connections between neurons do not form a cycle. Data flows in one direction, from input to output.

2. **Convolutional Neural Network (CNN)**:
   - Primarily used in image recognition and processing tasks. CNNs use convolutional layers to automatically detect spatial patterns in images, like edges and textures.

3. **Recurrent Neural Network (RNN)**: [[Recurrent Neural networks]]
   - Suitable for sequence-based tasks like time series forecasting and natural language processing. RNNs maintain information about previous inputs through feedback loops, making them effective for tasks where past information is important.

4. **Generative Adversarial Networks (GANs)**:
   - Composed of two neural networks, a generator, and a discriminator, that compete against each other. GANs are used for tasks like generating realistic images or videos.

5. **Transformer Networks**: [[Transformer Network]]
   - Widely used in natural language processing [[NLP]] (e.g., GPT models), transformers excel at handling sequence-based data and are particularly known for their self-attention mechanisms, which allow them to process long-range dependencies in data.

### Advantages of Neural Networks:
- **Flexibility**: Can model complex, non-linear relationships.
- **Adaptability**: Can be applied to a wide range of problems like image recognition, speech processing, and game playing.
- **Automatic Feature Extraction**: Neural networks, especially CNNs, can automatically learn important features from raw data without manual intervention.
### Challenges:
- **Data-hungry**: Neural networks typically require large datasets to perform well.
- **Computationally Intensive**: Training deep networks can require substantial computational resources.
- **Black Box Nature**: The internal decision-making process is often difficult to interpret, although research into interpretability is addressing this.
### My Notes

Number of starting nodes depends on input parameter, similar for output.

The width and the depth of the net are called [[hyperparameter]].

Non linear functions at nodes are called [[Activation Function]]. Common activation functions:
sigmoid, TanH, RELu,softmax. But how to choose them?

Methods to get parameters (weights biases) for NN using training data to reduce the errors in predictions: 

	[[Forward propagation]] is the process of pushing inputs through the net NN. At the end of each [[epoch]], the obtained outputs are
	compared to targets to form the errors.
	
	[[Backpropagation]] of errors is an algorithm for neural networks using gradient descent. It consists of calculating
	the contribution of each parameter to the errors. We backpropagate the errors through the net and update the
	parameters (weights and biases) accordingly.
## To explore

- **[[Multilayer Perceptrons]] (MLP)**: A basic fully connected network with multiple layers.
- [[Convolutional Neural Networks]]: Designed for image data.
- **Recurrent Neural Networks ([[Recurrent Neural networks|RNN]])**: Designed for sequence data (like time series or text).