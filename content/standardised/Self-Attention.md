---
aliases: []
category: LANG
date modified: 27-07-2025
tags: []
---
In this mechanism, the model applies attention to itself. This means each word in the input sequence attends to all other words in the sequence, including itself. Self-attention is used in models like [[Transformer]] to capture dependencies within a sentence.

[[Self-Attention]]
* Each token in a sequence considers all others when computing its representation.
* This enables rich, context-aware embeddings, even for long inputs.
* Unlike [[Recurrent Neural Networks]], Transformers allow parallel processing, making them more efficient and scalable.

Self-attention is the core of models like [[BERT]]& [[GPT]]
