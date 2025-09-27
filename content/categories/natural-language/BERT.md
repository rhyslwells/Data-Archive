---
aliases: []
category: LANG
date modified: 27-09-2025
tags:
- deep_learning
- language_models
- NLP
---
### Overview
* [[BERT]] (Bidirectional Encoder Representations from [[Transformer]]) is a [[Transformer]]-based model developed by [[Google]] in 2018 (transformers are often better than traditional [[NLP]] methods.
* It is built on the [[Transformer]] architecture and uses a bidirectional context representation—capturing the meaning of words based on both their left and right context.
* Introduced in the paper: "[[BERT Pretraining of Deep Bidirectional Transformers for Language Understanding]]".

### Pretraining and [[Transfer Learning]]

Pre-trained on large corpora using two main objectives:
  * Masked Language Modeling (MLM): Predict randomly masked words.
  * Next Sentence Prediction (NSP): Predict whether one sentence follows another.
Enables [[Transfer Learning]] through task-specific fine-tuning.
### Input [[Vector Embedding|Embeddings]]

* [[Tokenisation]]: Representation of each word or token. Then embeds these tokens as [[Vector Embedding]].
* Sentence Embeddings/ [[Sentence Transformers]]: Capture relationships between entire sentences.
* [[Positional Encoding]]: Adds information about the position of words to handle order.

### Applications of BERT
1. Text Classification – Sentiment analysis, topic classification.
2. [[Named Entity Recognition|NER]] – Extraction of entities like names, places, etc.
3. Question Answering – Find answers based on a passage.
4. Text [[Summarisation]] – Create concise summaries of documents.
5. Language Translation – Assist with machine translation.
6. [[Sentence Similarity]] – Evaluate semantic similarity between sentences.

### Limitations of BERT with Large Datasets

BERT generates contextual embeddings for each word in a sentence, which are typically pooled—using methods like mean pooling—to form a single sentence embedding (see [[Sentence Transformers]]). However, such pooling treats all words equally, regardless of their importance to the sentence’s overall meaning. This limits BERT’s ability to capture fine-grained semantic relationships.

While fine-tuning BERT on sentence pairs can help produce embeddings that better reflect relational meaning, this process is computationally intensive and does not scale well to large datasets.
### Resources
* [What is BERT and how does it work? | A Quick Review](https://www.youtube.com/watch?v=6ahxPTLZxU8&list=PLcWfeUsAys2my8yUlOa6jEWB1-QbkNSUl&index=12)
### Exploratory Questions

* [ ] What does [[BERT]] learn about syntax vs semantics? ⏬
* [ ] How do [[Attention mechanism]] heads contribute to sentence meaning?
* [ ] What are the limitations of BERT for [[Sentence Similarity]] and sentence clustering?

### Variants
* BERT-base: 12 layers, 110M parameters.
* BERT-large: 24 layers, 340M parameters.
* Optimized alternatives for specific tasks:
	* [[Sentence Similarity]]: Use [[Sentence-BERT]] instead of BERT for better performance on semantic similarity.

### Related
- [[Word2vec]]