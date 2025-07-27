---
aliases: []
category: 
date modified: 27-07-2025
tags: [deep_learning, NLP]
---
Positional encoding enables [[Transformer|transformers]] to capture sequence order, which is necessary for understanding grammar, sentiment, and meaning in natural language. Without it, the model would treat all token permutations as equivalent.

In models like [[BERT]], token embeddings represent *what* words are present in the input, but they do not contain information about the *order* of words. For example, the tokens:

> `["data", "science", "is", "great", "not", "so"]`

will have the same embeddings regardless of their position in a sentence.

To address this, positional embeddings are added to token embeddings. These provide the model with information about the position of each token in the sequence. Without this, the model cannot distinguish between *"not great"* and *"great not"*, which have different meanings.

In BERT:
* Each position in the input has its own learned positional embedding vector.
* The final input embedding is obtained by adding the token [[Vector Embedding|embedding]] and the corresponding position embedding element-wise.

### Embedding Example

| Token     | Token Embedding  | Positional Embedding | Final Embedding  |
| --------- | ---------------- | -------------------- | ---------------- |
| `[CLS]`   | [0.1, 0.2, 0.3] | [0.0, 0.0, 0.0]     | [0.1, 0.2, 0.3] |
| `data`    | [0.4, 0.5, 0.6] | [0.1, 0.1, 0.1]     | [0.5, 0.6, 0.7] |
| `science` | [0.7, 0.8, 0.9] | [0.2, 0.2, 0.2]     | [0.9, 1.0, 1.1] |
| `is`      | [0.3, 0.3, 0.4] | [0.3, 0.3, 0.3]     | [0.6, 0.6, 0.7] |
| `great`   | [0.5, 0.6, 0.7] | [0.4, 0.4, 0.4]     | [0.9, 1.0, 1.1] |
| `[SEP]`   | [0.0, 0.1, 0.2] | [0.5, 0.5, 0.5]     | [0.5, 0.6, 0.7] |

> Final embedding = Token embedding + Position embedding (element-wise)