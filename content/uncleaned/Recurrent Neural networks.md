---
title: 
tags:
  - deep_learning
  - ml
  - time_series
aliases:
  - RNN
  - RNNs
---
[[Transformer Network|Transformer]]'s have replaced traditional RNN.

[LSTM](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)

[[Use of RNNs in energy sector]]

RRS have loops

![[Pasted image 20241015205137.png|100]]

Recurrent neural networks, or RNNs, are designed for processing sequential data, such as text or time series. They have connections that form loops, allowing information to persist and be passed from one step in the sequence to the next. RNNs maintain an internal state or memory that captures information from previous time steps, enabling them to learn patterns and dependencies across time. They are widely used for natural language processing tasks like machine translation, speech recognition, and text generation.

**Recurrent Neural Networks (RNNs)** are a class of neural networks specifically designed to ==handle sequential data== by ==maintaining a memory of previous inputs== throught the use of ==hidden states==. They are commonly used in tasks where the order of data is important, such as time series prediction, speech recognition, and natural language processing (NLP). 

Unlike [[Feed Forward Neural Network]] RNNs have connections that loop back, allowing them to process sequences of inputs with the ability to retain information from previous steps.

They are powerful for tasks where context and order matter, but they have limitations with long sequences due to issues like [[vanishing and exploding gradients problem]]. Variants like [[LSTM]] and [[GRU]] address some of these challenges, making them more effective in practice.
### Key Concepts of RNNs:

1. **Sequential Data Handling**:
   - RNNs are built to handle sequences by maintaining a **hidden state** that serves as memory. This allows them to model temporal dependencies in data, making them useful for tasks where the current output depends not only on the current input but also on previous inputs.
   - Each step in the sequence has an input and a hidden state passed from the previous time step.

2. **Architecture**:
   - At each time step, the network processes an input, combines it with the hidden state from the previous step, and produces an output as well as an updated hidden state.
   - The hidden state is a key aspect of RNNs and carries forward information that can be influenced by all previous inputs, theoretically giving RNNs the ability to remember long-term dependencies.

   The basic equations governing RNNs are:
   - Hidden state: $h_t = \tanh(W_{xh} \cdot x_t + W_{hh} \cdot h_{t-1} + b_h)$
   - Output: $y_t = W_{hy} \cdot h_t + b_y$
   
   Where:
   - $x_t$ is the input at time step $t$
   - $h_t$ is the hidden state at time $t$
   - $W_{xh}$, $W_{hh}$, and $W_{hy}$ are weight matrices
   - $b_h$ and $b_y$ are bias terms

3. **Recurrent Connections**:
   - RNNs process data sequentially, where the output of a neuron in the current time step depends on the previous time step through recurrent connections. This is what allows the network to maintain a **memory** of past inputs and propagate information over time.
   - This internal recurrence enables RNNs to model sequences, but it also makes training challenging due to issues like **vanishing and exploding gradients**.

4. **[[Backpropagation]] Through Time (BPTT)**:
   - RNNs are trained using a variant of backpropagation called **Backpropagation Through Time (BPTT)**. In BPTT, the network unrolls the sequence over time, treating each time step as a layer of a deep network.
   - Gradients are computed for each time step, and weights are updated based on the cumulative error across the entire sequence. This process allows the network to learn long-term dependencies.
   - However, long sequences can lead to **vanishing gradients**, where the gradients become too small to effectively update the network’s weights, making it hard for RNNs to learn long-range dependencies.

5. **Variants of RNNs**:
   - **[[LSTM]] (Long Short-Term Memory)**: A more advanced RNN architecture designed to solve the problem of vanishing gradients. LSTMs introduce **gates** (input gate, forget gate, output gate) to control the flow of information and selectively remember or forget information over long sequences.
   - **[[GRU]] (Gated Recurrent Unit)**: A simpler variant of LSTM that also includes gates to control the memory but with fewer parameters. It’s often more efficient and easier to train than LSTMs while still retaining good performance on sequence tasks.

### Workflow of an RNN:

Let’s consider an RNN applied to a sentence for **sentiment analysis**:
- **Input**: The network takes in one word (or token) at a time, processing it step by step.
- **Hidden State Update**: After each word, the RNN updates its hidden state based on the current word and the hidden state from the previous step, allowing it to “remember” information from earlier in the sentence.
- **Output**: At each time step, the RNN produces an intermediate output (which can be ignored or used depending on the task) and a final output at the end of the sequence (e.g., a sentiment score).

For example, if the sentence is "The movie was great," the RNN will process each word in sequence, updating its hidden state as it moves through the sentence, and finally produce a sentiment score indicating positive sentiment.

### Strengths of RNNs:
1. **Sequence Modeling**: RNNs are well-suited for modeling sequential data like time-series, speech, and text because they have a form of memory through hidden states.
2. **Context Awareness**: RNNs can incorporate past information into current decisions, making them valuable for tasks like language modeling, where the meaning of a word can depend on the context provided by previous words.

### Weaknesses of RNNs:
1. **Vanishing and Exploding Gradients**: The sequential nature of RNNs often leads to issues with gradients becoming too small (vanishing) or too large (exploding) during training, making it hard to learn long-term dependencies.
2. **Sequential Processing**: RNNs process input one time step at a time, which means they can be slow to train compared to models like transformers, which can handle entire sequences in parallel.
3. **Difficulty Handling Long Dependencies**: While theoretically, RNNs should capture long-term dependencies, in practice, they often struggle with very long sequences, which is why LSTMs and GRUs are preferred for such tasks.

### Example Code (RNN in Python with PyTorch):

```python
import torch
import torch.nn as nn

class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleRNN, self).__init__()
        self.hidden_size = hidden_size
        # RNN Layer
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        # Output Layer
        self.fc = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        h0 = torch.zeros(1, x.size(0), self.hidden_size).to(x.device)  # Initial hidden state
        out, _ = self.rnn(x, h0)  # Forward pass through RNN
        out = self.fc(out[:, -1, :])  # Taking the output of the last time step
        return out

# Example usage
input_size = 10  # Number of features
hidden_size = 20  # Number of hidden neurons
output_size = 2  # Binary classification

model = SimpleRNN(input_size, hidden_size, output_size)
input_data = torch.randn(32, 5, input_size)  # Batch of 32 sequences, each with 5 time steps
output = model(input_data)
print(output.shape)  # Expected output shape: (32, 2)
```

### Applications of RNNs:
- **Natural Language Processing (NLP)**: Used in tasks like machine translation, text generation, and sentiment analysis.
- **Time Series Forecasting**: Applied in stock price prediction, weather forecasting, etc.
- **Speech Recognition**: Used to recognize spoken words and phrases in speech-to-text models.

# Notes

https://karpathy.github.io/2015/05/21/rnn-effectiveness/

**Inductive Reasoning, Memories and Attention.** Another extremely exciting direction of research is oriented towards addressing the limitations of vanilla recurrent networks. One problem is that RNNs are not inductive: They memorize sequences extremely well, but they don’t necessarily always show convincing signs of generalizing in the _correct_ way (I’ll provide pointers in a bit that make this more concrete). A second issue is they unnecessarily couple their representation size to the amount of computation per step. For instance, if you double the size of the hidden state vector you’d quadruple the amount of FLOPS at each step due to the matrix multiplication. Ideally, we’d like to maintain a huge representation/memory (e.g. containing all of Wikipedia or many intermediate state variables), while maintaining the ability to keep computation per time step fixed.










