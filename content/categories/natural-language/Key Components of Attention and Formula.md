---
aliases: []
category: LANG
date modified: 27-09-2025
tags:
- math
- NLP
---
### Key Components of Attention and Formula

1. Query: Represents the current word or position that requires attention: $Q$
2. Key: Represents each word in the input sequence: $K$
3. Value: Represents the actual content or information in the input sequence: $V$
4. Attention Scores: The attention mechanism computes the relevance between the query and each key by computing a similarity score (such as dot-product or other scoring methods).
5. Softmax: These scores are then passed through a softmax function to form a probability distribution, which gives us the attention weights.
6. Context Vector: A weighted sum of the values ($V$), using the attention weights, is computed. This context vector is what the model uses to generate the output token.

Given a query matrix, key matrix, and value matrix, attention is calculated as:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

Where:
- $Q$,$K$, and $V$are matrices of query, key, and value vectors.
- $d_k$ is the dimension of the keys.
- The softmax is applied row-wise to produce attention weights.