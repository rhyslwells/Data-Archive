---
title: 
tags:
  - deep_learning
  - NLP
  - ml
  - time_series
  - ml_process
  - code_snippet
---

# Notes

Resources:[Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)

Ideas persist. Networks that remember

$x_t$ input, $h_t$ output

cell state $C_t$, conveyer belt

gates 

varients of lstm eg gated recurrent unit: update gate

![[Pasted image 20241015211424.png]]


# Summary

LSTM (Long Short-Term Memory) networks are a specialized type of **Recurrent Neural Network (RNN)** designed to overcome the [[vanishing and exploding gradients problem]] that affects traditional [[RNNs]]. 

LSTMs address this challenge through their unique architecture.

Used for tasks that require the retention of information over time, and problems involving ==sequential data.== 

The key strength of LSTMs is their ability to manage ==long-term dependencies== using their ==gating mechanisms==.
### Key Components of LSTM Networks:

1. **Memory Cell**:
   - The core of an LSTM network is the memory cell, which maintains information over long time intervals. This cell helps store, forget, or pass on information from previous time steps.

2. **==Gates==**:
   - **Input Gate**: Controls how much of the input should be allowed into the memory cell.
   - **Forget Gate**: Determines which information should be discarded from the memory cell.
   - **Output Gate**: Controls what part of the cell's memory should be output as the hidden state for the current time step.

These gates are regulated by ==sigmoid== activation, which output values between 0 and 1, acting like a filter to determine the amount of information that should pass through. This gate mechanism allows the LSTM network to maintain a balance between retaining relevant data and discarding unnecessary information over time.
### Example Workflow in Python using Keras:

In this example, we define a simple LSTM model in **[[Keras]]** for a time series forecasting task. The model processes sequences with 1000 time steps, and the LSTM layer has 50 units, followed by a fully connected (Dense) layer for the final prediction.

```python
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense

# Sample data: time series with 1000 timesteps and 1 feature
time_steps = 1000
features = 1
X_train = np.random.rand(1000, time_steps, features)
y_train = np.random.rand(1000)

# Define LSTM model
model = Sequential()
model.add(LSTM(50, activation='tanh', return_sequences=False, input_shape=(time_steps, features)))
model.add(Dense(1))  # Output layer for regression tasks

model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=64)
```




