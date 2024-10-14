---
title: 
tags:
  - deep_learning
  - NLP
  - ml
aliases:
  - Transformer
  - Transformers
---
A **transformer** in machine learning (ML) refers to a deep learning model architecture designed to process sequential data, such as natural language. It was introduced in the paper [[Attention Is All You Need]] and has since become a cornerstone in **Natural Language Processing ([[NLP]])** tasks.

[[Transformers vs RNNs]]

### Key Concepts of a Transformer:

1. **Self-Attention Mechanism**:  see [[Attention mechanism]]

2. **Positional Encoding**:
   - Since transformers process input all at once (not sequentially like [[Recurrent Neural networks|RNNs]]), they need a way to understand the order of the tokens in a sequence. ==Positional encodings are added to input embeddings to give the model this positional information.==

3. **Encoder-Decoder Structure**:
   - The **encoder** processes the input sequence to build a representation, while the **decoder** takes this representation and generates the output sequence. This setup is particularly useful for tasks like translation.

4. **Parallelization**:
   - Unlike Recurrent Neural Networks (RNNs), transformers do ==not require sequential processing,== making them more efficient, especially when training large datasets.
### Example:

**NLP**: Transformers are widely used in NLP for tasks like translation, text generation, summarization, and question answering. For instance, models like [[BERT]], GPT, and T5 are all based on the transformer architecture.

In **language translation**, a transformer takes an input sentence in one language and processes it through the encoder to generate an internal representation. The decoder then uses this representation to produce a translated sentence in another language.


