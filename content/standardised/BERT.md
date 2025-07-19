---
title: 
tags:
  - NLP
  - language_models
  - deep_learning
aliases: 
category: LANG
---
### Overview

* [[BERT]] (Bidirectional Encoder Representations from [[Transformer]]) is a [[transformer]]-based model developed by [[Google]] in 2018.
* It is built on the [[Transformer]] architecture and uses a **bidirectional** context representation—capturing the meaning of words based on both their left and right context.
* Introduced in the paper: "[[BERT Pretraining of Deep Bidirectional Transformers for Language Understanding]]".

### Pretraining and [[Transfer Learning]]

* Pre-trained on large corpora using two main objectives:
  * **Masked Language Modeling (MLM)**: Predict randomly masked words.
  * **Next Sentence Prediction (NSP)**: Predict whether one sentence follows another.
* Enables [[Transfer Learning]] through task-specific fine-tuning.

### Input [[Vector Embedding|Embeddings]]

* [[Token Embedding]]: Representation of each word or token.
* Sentence Embeddings: Capture relationships between entire sentences.
* [[Positional Encoding]]: Adds information about the position of words to handle order.

### Fine-Tuning BERT

Fine-tuning modifies the final layer to fit downstream tasks like:
  * Text classification
  * [[Named Entity Recognition|NER]]
  * Question answering
  * Retains pre-trained layers; only the top task-specific layers are changed.

### Variants

* **BERT-base**: 12 layers, 110M parameters.
* **BERT-large**: 24 layers, 340M parameters.
* Optimized alternatives for specific tasks:
	* [[Sentence Similarity]]: Use [[Sentence-BERT]] instead of BERT for better performance on semantic similarity.
### Applications of BERT

1. **Text Classification** – Sentiment analysis, topic classification.
2. **[[Named Entity Recognition|NER]]** – Extraction of entities like names, places, etc.
3. **Question Answering** – Find answers based on a passage.
4. **Text [[Summarisation]]** – Create concise summaries of documents.
5. **Language Translation** – Assist with machine translation.
6. **[[Sentence Similarity]]** – Evaluate semantic similarity between sentences.
### Resources
* [What is BERT and how does it work? | A Quick Review](https://www.youtube.com/watch?v=6ahxPTLZxU8&list=PLcWfeUsAys2my8yUlOa6jEWB1-QbkNSUl&index=12)
### Exploratory Questions

* What does [[BERT]] learn about **syntax** vs **semantics**?
* How do [[Attention mechanism]] heads contribute to sentence meaning?
* What are the limitations of BERT for [[Sentence Similarity]] and sentence clustering?
