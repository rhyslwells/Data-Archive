---
title: 
tags:
  - NLP
  - language_models
aliases: 
category:
---
BERT (==Bidirectional Encoder Representations from Transformers==) is a state-of-the-art natural language processing ([[NLP]]) model developed by [[Google]]. It was introduced in the paper "[[BERT Pretraining of Deep Bidirectional Transformers for Language Understanding]]" in 2018. 

It is forward & backward looking in the context.

BERT has significantly advanced the field of NLP by improving the performance of various tasks and setting new benchmarks on multiple NLP datasets. Its ability to understand context and relationships in language has made it a foundational model for many subsequent developments in the field.

### What is BERT?

- Architecture: BERT is based on the [[Transformer]] architecture and utilizes a bidirectional approach, meaning it considers the ==context of a word based on both its left and right surroundings in a sentence.== This allows BERT to capture nuanced meanings and relationships between words more effectively than previous models that processed text in a unidirectional manner.

- Pre-training and Fine-tuning: BERT is ==pre-trained== on a large corpus of text using unsupervised learning techniques. It learns to predict masked words in sentences (Masked Language Model) and to determine if one sentence follows another (Next Sentence Prediction). After pre-training, BERT can be fine-tuned on specific tasks with labeled data, making it highly adaptable.

### What is BERT Used For?

BERT is used for a variety of [[NLP]] tasks, including:

1. Text Classification: Assigning categories or labels to text documents, such as sentiment analysis or topic classification.

2. Named Entity Recognition ([[Named Entity Recognition|NER]]): Identifying and classifying entities (e.g., names, organizations, locations) within text.

3. Question Answering: Providing answers to questions based on a given context or passage of text.

4. Text [[Summarisation]]: Generating concise summaries of longer documents while retaining key information.

5. Language Translation: Assisting in translating text from one language to another.

6. [[Sentence Similarity]] :Measuring the similarity between sentences, which can be useful for tasks like paraphrase detection or duplicate question identification.

