---
aliases: []
category: 
date modified: 1-08-2025
tags: []
---
This guide provides practical insights into building and using [[Neural network]].

Refer to [[ML_Tools]] for more details: `Neural_Net_Build.py`

## Softmax Placement at the End

Numerical stability is crucial. One way to enhance stability is by grouping the softmax function with the loss function rather than placing it at the output layer.

### Building the Model

**Final Dense Layer**: 
  - Use a 'linear' activation function, which means no activation is applied. This setup allows the model to output raw logits.
  
**Model Compilation**: 
  - When compiling the model, specify `from_logits=True` in the loss function to indicate that the outputs are raw logits.
  ```python
  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
  ```
**Target Form**: 
  - The target format remains unchanged. For instance, with SparseCategoricalCrossentropy, the target is the expected class label (e.g., digits 0-9 in the MNIST dataset).
  - See [[SparseCategorialCrossentropy or CategoricalCrossEntropy]]

**Output Probabilities**: 
  - Since the model outputs logits, apply a softmax function to convert these logits into probabilities if needed for interpretation or further processing.

## TensorFlow History Loss (Cost)

Monitoring the cost, or loss, during training is essential for understanding how well the model is learning.

**Monitoring Progress**: 
  - Track the progress of gradient descent by observing the cost, referred to as `loss` in TensorFlow. Ideally, the loss should decrease as training progresses.
**Loss Display**: 
  - The loss is displayed at each [[epoch]] during the execution of `model.fit`, providing real-time feedback on training performance.
**History Variable**: 
  - The `.fit` method returns a `history` object containing various metrics, including the loss. This object is stored in the `history` variable for further analysis.

The `history` object can capture additional metrics such as accuracy, validation loss, and other performance indicators, depending on what was specified during model compilation and fitting. This information is valuable for evaluating the model's performance [[Model Evaluation]].

