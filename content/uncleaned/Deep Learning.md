---
tags:
  - learning
  - deep_learning
  - ml
  - drafting
---
# Slides on deep leanring

- They use [[Activation Function]]
- They use [[Neural network|Neural Network]]
- [[Back propagation algorithms]] works by determining the [[loss function]]/loss (or error) at the output and then propagating it back into the network. The weights are updated to minimize the error resulting from each neuron.
- [[Regularisation]] techniques are used to remove/ignore nodes in the network and reduce [[overfitting]].

Deep learning applications require:
- Labelled data
- DL frameworks:
	- [[PyTorch]]
	- [[Tensorflow]]

[[Convolutional Neural Networks]]

[[What is the role of gradient-based optimization in training deep learning models. ]]

[[Explain different gradient descent algorithms, their advantages, and limitations.]]

Learns own rules to get to the objective.

<!--SR:!2000-01-01,1,250!2024-04-22,11,270--> 

What is the key thing at deep learning is about;; Neural networks
<!--SR:!2024-04-12,1,232-->
How can a [[Neural network|neural network]] be described;; Linear algebra with non linear actions on nodes with multiple layers to make predictions, with an input and output layer.
Deep learning is a subset;; of machine learning.
<!--SR:!2024-04-25,14,290-->
Machine learning focuses;; on regression, nearest neighbours and decision trees with small datasets.
Deep learning focuses on;; neural networks with large datasets.
In deep learning features are;; handled automatically during the training process.
In machine learning features are;; carefully selected  or they creates new ones for the task at hand.
What is Deep Learning used for?;; Used in image and speech recognition, natural language processing, autonomous vehicles, recommendation systems.

What is a Node in a [[Neural network|Neural Network]]?;; Nodes in a [[Neural network|neural network]] are basic computational units that receive inputs, perform a weighted sum of those inputs, and apply an activation function to produce an output. 



How are weights initialized in a [[Neural network|neural network]]?;; Initializing all weights randomly: the weights are assigned randomly by initializing them very close to 0. It gives better accuracy to the model since every neuron performs different computations.

What is an [[Activation Function]]?;; It is a non-linearity function at  a node for example  ReLU (Rectified Linear Unit), Sigmoid, and Tanh.




What is [[Backpropagation]] and whats it used for?;; Used for training and involves iteratively adjusting the network's weights and biases to minimize the difference between the predicted output and the actual target values [[Optimisation function]].

What are some types of [[Neural network]]?;; Convolutional Neural Networks (CNNs), [[Recurrent Neural networks]]

[[Convolutional Neural Networks]] (CNNs) are used for;; used for image and video analysis, object recognition, and computer vision tasks.

[[Recurrent Neural networks]] are used for?;; ideal for sequence data, like natural language processing, time series analysis, and speech recognition.




What is a Large Language Model ([[LLM]])?;;  is a type of language model for language understanding and generation. They can perform tasks like text generation, machine translation, summary writing, image generation from texts, machine coding, chat-bots, or Conversational AI.



How do Large Language Models ([[LLMs]]) work?
?
Large Language Models (LLMs)** are a type of artificial intelligence model that is designed to understand and generate human language. 
LLMs represent words as long lists of numbers, known as *word vectors*.
LLMs are built on a [[Neural network|neural network]] architecture known as the [[Transformer Network]].
This architecture enables the model to identify relationships between words in a sentence, irrespective of their position in the sequence.
LLMs are trained using a technique known as [[transfer learning]], where a pre-trained model is adapted to a specific task. 











