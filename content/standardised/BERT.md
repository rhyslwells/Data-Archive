---
title: 
tags:
  - NLP
  - language_models
aliases: 
category:
---
BERT (==Bidirectional Encoder Representations from [[Transformer]]==) is used in [[NLP]]processing, developed by [[Google]]. 

Introduced in the paper "[[BERT Pretraining of Deep Bidirectional Transformers for Language Understanding]]" in 2018. 

It is forward & backward looking in the context.

BERT is a stack of encoders -learning context.

Input [[Vector Embedding|embedding]]:
- [[Positional Encoding]]: passes location info to encoder
- Sentence embeddings: differences between sentences
- Token embeddings

Training of BERT:
- Masked Language modelling (hiding words)
- Next Sentence Prediction

Fine tuning ([[Transfer Learning]]) BERT model:
- New output layer dependent
 
Resources:
- [What is BERT and how does it work? | A Quick Review](https://www.youtube.com/watch?v=6ahxPTLZxU8&list=PLcWfeUsAys2my8yUlOa6jEWB1-QbkNSUl&index=12)

### What is BERT?

- BERT is based on the [[Transformer]] architecture and utilizes a bidirectional approach, meaning it considers the ==context of a word based on both its left and right surroundings in a sentence.== This allows BERT to capture nuanced meanings and relationships between words more effectively than unidirectional models

- Pre-training and Fine-tuning/[[Transfer Learning]] techniques. It learns to predict masked words in sentences (Masked Language Model) and to determine if one sentence follows another (Next Sentence Prediction).
### What is BERT Used For?

1. Text Classification: Assigning categories or labels to text documents, such as sentiment analysis or topic classification.

2. Named Entity Recognition ([[Named Entity Recognition|NER]]): Identifying and classifying entities (e.g., names, organizations, locations) within text.

3. Question Answering: Providing answers to questions based on a given context or passage of text.

4. Text [[Summarisation]]: Generating concise summaries of longer documents while retaining key information.

5. Language Translation: Assisting in translating text from one language to another.

6. [[Sentence Similarity]] :Measuring the similarity between sentences, which can be useful for tasks like paraphrase detection or duplicate question identification.

