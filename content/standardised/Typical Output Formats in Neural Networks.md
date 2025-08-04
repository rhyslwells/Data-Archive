---
aliases: 
category: ML
date modified: 1-08-2025
tags:
  - deep_learning
  - algorithm
  - exploration
---
The output format of a [[Neural network]] is largely determined by the specific task it is designed to perform.
## Classification

### [[Binary Classification]]

 Single Output Node: This involves a single output node with a value between 0 and 1, representing the probability of the input belonging to the positive class.

Example: A spam classifier might output a value close to 1 for a spam email and a value close to 0 for a legitimate email.

### Multiclass [[Classification]]

 Multiple Output Nodes: Each class has its own output node, with values typically between 0 and 1, representing the probability of the input belonging to that class. These probabilities often sum to 1.

Example: An image classifier for different types of animals (cat, dog, bird) might output a vector like [0.2, 0.7, 0.1], indicating a 70% probability of the image being a dog.

## [[Regression]]

Single Output Node: This involves a single output node representing a continuous value.

Example: A neural network predicting house prices would output a single value representing the predicted price.

## Sequence to Sequence Tasks

 Sequence of Outputs: The output is often represented as a list or a tensor.
 
Example: A neural machine translation model would output a sequence of words or subword units in the target language.

Example Applications
- **Machine Translation:** Converts a sentence from one language to another.
- **Text Summarization:** Generates a concise summary from a longer text.
- **Speech Recognition:** Transcribes spoken language into written text.
## Generative Tasks (e.g., Image Generation, Music Composition)

Data in the Same Format as the Input: The output is typically in the same format as the input data.
 
Example: An image generation model might output a tensor representing a generated image.

See [[Generative AI]]
## Key Considerations

[[Activation Function]]: The choice of activation function in the output layer can significantly influence the output format. 

Loss Functions: The [[loss function]] used during training also guides the output format. For example, binary crossentropy is commonly used for binary classification, while mean squared error is often used for regression.