---
title: Natural Language Processing
tags:
  - NLP
aliases:
  - Natural Language Processing
category: Machine Learning
---

## Overview

Natural Language Processing (NLP) involves the interaction between computers and humans using natural language. It encompasses various techniques and models to process and analyze large amounts of natural language data.

## Key Concepts

### [[Feature Preprocessing]]
- **[[Normalisation of Text]]**: The process of converting text into a standard format, which may include lowercasing, removing punctuation, and stemming or [[lemmatization]].
- **[[Part of speech tagging]]**: Assigning a specific part-of-speech category (such as noun, verb, adjective, etc.) to each word in a text.

### Models
- **[[Bag of words]]**: Represents text data by counting the occurrence of each word in a document, ignoring grammar and word order. It takes key terms of a text in normalized **unordered** form.
- **[[TF-IDF]]**: Stands for Term Frequency-Inverse Document Frequency. It improves on Bag of Words by considering the importance of a word in a document relative to its frequency across multiple documents.
- **Vectorization**: Converting text into numerical vectors. Techniques like Bag of Words, TF-IDF, or [[Word Embedding]] (e.g., Word2Vec, GloVe) are used to represent text data numerically.

### Analysis
- **[[One Hot Encoding]]**: Converts categorical data into a binary vector representation, indicating the presence or absence of a word from a list in the given text.

### Methods
- **[[Ngrams]]**: Creates tokens from groupings of words, not just single words. Useful for capturing context and meaning in text data.
- **[[Grammar method]]**: Involves analyzing the grammatical structure of sentences to extract meaning and relationships between words.

### Actions
- **[[Summarisation]]**: The process of distilling the most important information from a text to produce a concise version.

## Tools and Libraries

### General Imports

```python
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer

porter_stemmer = PorterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()
```

- **[[nltk]]**: A leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources.
  - **punkt**: An unsupervised trainable model for tokenizing text into sentences and words.
  - **stopwords**: Commonly used words (such as "the", "is", "in") that are often removed from text data because they do not carry significant meaning.
  - **wordnet**: A lexical database for the English language that groups words into sets of synonyms and provides short definitions and usage examples.
  - **re**: Regular expressions for pattern matching and text manipulation.
