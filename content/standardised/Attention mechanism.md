---
title: 
tags:
  - ml
importance: 9
engagement: 9
recency_of_interest: 2024-09-29
aliases: []
---
>[!intuition]
> Think of attention like human reading behavior: when reading a complex sentence, we don't process all the words equally at every moment. Instead, we might "attend" more to certain words based on the context of what we’ve read so far and what we're trying to understand. This is similar to what the attention mechanism does in neural networks.

>[!Summary]
>The **attention mechanism** is a key concept in modern [[ML]] particularly in natural language processing ([[NLP]]/[[LLM]]) and sequence-based models like neural machine translation (NMT). It was introduced to address the limitations of earlier models, like [[Recurrent Neural networks|RNN]] and [[LSTM]] network), in handling long sequences and capturing important dependencies within data.
>The attention mechanism improves a model's ability to focus on important parts of the input data, helping it manage long-range dependencies, which is especially useful in tasks like machine translation, text generation, and various NLP tasks.

### Core Idea of Attention

The  [[Transformer|Transformer]] architecture, introduced by Vaswani et al. in 2017 ("[[Attention Is All You Need]]"), is the most popular use of the attention mechanism. The key innovation of Transformers is the ==**self-attention mechanism**==, which ==allows each token in a sequence to attend to all other tokens==, making the model more efficient and scalable for parallel processing. ==Transformers replaced traditional RNN-based== models and have become the foundation of models like [[BERT]], GPT, and T5.

The attention mechanism allows a model to focus on different parts of an input sequence when making predictions, rather than relying on a fixed-size hidden state to encode all information. This selective "focus" can greatly enhance the model's ability to handle long-range dependencies.

For example, in machine translation, while translating a sentence from one language to another, different words in the input sentence might hold varying degrees of relevance to the word currently being translated. Attention helps the model dynamically weigh the importance of different words at each step of the translation.

In its simplest form, attention assigns **weights** to each input token based on its relevance to the current output token being generated. These weights are typically calculated using a **score function** and then normalized (usually through a softmax) to produce a distribution over the input sequence. The weighted sum of the input tokens is then passed as context for generating the output token.

### Key Components of Attention and Formula

I see! Here's the text with the math terms wrapped in as requested:

1. **Query**: Represents the current word or position that requires attention: $Q$
2. **Key**: Represents each word in the input sequence: $K$
3. **Value**: Represents the actual content or information in the input sequence:  $V$
4. **Attention Scores**: The attention mechanism computes the relevance between the query and each key by computing a similarity score (such as dot-product or other scoring methods).
5. **Softmax**: These scores are then passed through a softmax function to form a probability distribution, which gives us the **attention weights**.
6. **Context Vector**: A weighted sum of the values ($V$), using the attention weights, is computed. This context vector is what the model uses to generate the output token.

Given a query matrix, key matrix, and value matrix, attention is calculated as:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

Where:
- $Q$,$K$, and $V$are matrices of query, key, and value vectors.
- $d_k$ is the dimension of the keys.
- The softmax is applied row-wise to produce attention weights.

### Applications of Attention

- **Machine Translation**: Aligns source and target words in a more dynamic and context-dependent way.
- **Text Summarization**: Helps to identify the most relevant parts of a document.
- **Speech Recognition**: Enhances the model’s ability to focus on important features over long audio sequences.
- **Vision**: Self-attention is now used in computer vision tasks (Vision Transformers or ViTs) to model dependencies between different parts of an image.

### Types of Attention Mechanisms
1. **Additive Attention**: Introduced in the original attention paper by Bahdanau et al. (2014), this method uses a feed-forward neural network to compute the relevance between the query and each key.
   
2. **Dot-Product (Multiplicative) Attention**: Introduced in the Transformer paper by Vaswani et al. (2017), this method computes the relevance using a simple dot product between the query and key vectors. It is computationally efficient and widely used.

3. **Scaled Dot-Product Attention**: A variant of dot-product attention, used in the Transformer architecture, where the dot product is divided by the square root of the dimension of the key vectors to avoid excessively large gradients.

4. **Self-Attention**: In this mechanism, the model applies attention to itself. This means each word in the input sequence attends to all other words in the sequence, including itself. Self-attention is used in models like Transformers to capture dependencies within a sentence.

### Self attention vs multi-head attention

https://www.youtube.com/shorts/Muvjex0nkes

Take every word pays attention to every other word to capture contetxt by:

1. take input word vectors,
2. break words into Q,K,V vectors,
3. compute attention matrix
4. generate final word vectors.
these vectors

Multi-head attention: perform self attention in parallel.

1. take word vectors,
2. break words into Q,K,V vectors,
	1. Break each Q,K,V vector into the number of heads parts
3. compute attention matrix for each head
4. generate final word vectors for each head
5. Combine back together

These have better understanding of the context.

[[Multi-head attention]]

- This allows the model to weigh the importance of different words in a sequence when making predictions. It captures relationships between words, even if they are far apart in the sequence.
   - The model computes attention scores for each pair of words to determine how much focus one word should place on another in a sequence.