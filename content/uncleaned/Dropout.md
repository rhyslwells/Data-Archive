Regularisation technique for [[Neural network]]

- **Dropout:** A neural network regularization method that drops units at random during training to prevent over-reliance on specific neurons.

[[Dropout]] 
    is another form of [[Regularisation]] for neural networks, where randomly selected neurons are ignored (dropped out) during training to reduce overfitting.

[[Dropout]]
DRopout in [[Neural network]]

Randomly drops units during training to improve generalization. Dropout helps prevent overfitting by ensuring that the network does not rely too heavily on any single neuron.

```python
from tensorflow.keras.layers import Dropout
Dropout(0.5)
```