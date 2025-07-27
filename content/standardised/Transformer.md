---
aliases: [Transformers]
category:
date modified: 27-07-2025
tags: [deep_learning, NLP]
title: 
---
A transformer in machine learning (ML) refers to a deep learning model architecture designed to process sequential data, such as natural language processing ([[NLP]]). It was introduced in the paper "[[Attention Is All You Need]]" and has since become a cornerstone in NLP tasks.

Transformers excel at handling sequence-based data and are particularly known for their self-attention mechanisms [[Attention mechanism]], which allow them to process long-range dependencies in data.

### Key Concepts of a Transformer

1. Architecture Overview:
    - A transformer model consists of an encoder and a decoder, although some models use only the encoder (like [[BERT]] only consists of encoders) or only the decoder (like GPT3). Each of these components is made up of layers that include mechanisms for attention and [[Feed Forward Neural Network]].
    - Encoder learns the context, decoder does the task.

2. Self-[[Attention Mechanism]]:
    - The core innovation of transformers is the self-attention mechanism, which allows the model to weigh the importance of different words in a sentence relative to each other. This is crucial for understanding context and relationships in language. See [[Attention mechanism]].
    - Scaled Dot-Product Attention: For each word in a sentence, the model computes attention scores with every other word. These scores are used to create a weighted representation of the input, emphasizing relevant words and de-emphasizing less relevant ones.

3. [[Multi-head attention]]
    - Instead of having a single attention mechanism, transformers use multiple attention heads. Each head learns different aspects of the relationships between words, allowing the model to capture various linguistic features.

4. Positional Encoding:
    - Since transformers do not inherently understand the order of words (unlike [[Recurrent Neural Networks|RNNs]]), they use positional encoding to inject information about the position of each word in the sequence.

5. Feed-Forward Neural Network:
    - After the attention mechanism, the output is passed through a feed-forward neural network, which is applied independently to each position.
      
6. Layer Normalization and Residual Connections:
    - Transformers use layer normalization and residual connections to stabilize training and help with gradient flow, making it easier to train deep networks.

7. Training and Applications:
    - Transformers are trained on large corpora of text data using [[Unsupervised Learning|unsupervised]] or semi-supervised learning techniques. They are used for a variety of NLP tasks, including translation, summarization, and question answering.

### Additional Concepts

- Encoder-Decoder Structure:
    - The encoder processes the input sequence to build a representation (maintaining [[Semantic Relationships]]), while the decoder takes this representation and generates the output sequence (next word prediction).

- Parallelization:
    - Unlike Recurrent Neural Networks ([[Recurrent Neural Networks]]), transformers do not require sequential processing, making them more efficient, especially when training large datasets.

Follow-up questions:
- [[Transformers vs RNNs]]
