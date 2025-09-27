---
aliases: []
category: DATA_ANALYSIS
date modified: 27-09-2025
tags:
- cleaning
- NLP
- preprocessing
- process
---
[[Preprocessing]] in [[Text Classification]] is the set of steps applied to raw text before feeding it into a machine learning or deep learning model. The goal is to normalize text, remove noise, and convert it into a numerical representation suitable for algorithms.

### Typical Preprocessing Steps

#### Text Cleaning

* Remove punctuation, special characters, numbers (optional).
* Lowercasing text: `"The Cat"` → `"the cat"`.
* Remove unwanted whitespace.

#### [[Tokenisation|Tokenization]]

* Split text into tokens (words, subwords, or characters).

  * Example: `"I love NLP"` → `["I", "love", "NLP"]`.

#### Stopword Removal

* Remove common words that add little meaning:

  * Example: `"is", "and", "the"`.

#### Normalization

* [[Stemming]]: Reduce words to their root form (e.g., `"running"` → `"run"`).
* [[lemmatization]]: Use vocabulary and grammar to reduce to base form (`"better"` → `"good"`).

#### Handling Categorical/Text Variants

* Remove URLs, HTML tags, mentions (`@username`), hashtags.

#### Handling Out-of-Vocabulary (OOV) & Rare Words

* Replace rare words with `<UNK>` token or use subword tokenization (e.g., BPE).

#### Encoding Text

Convert processed tokens into numerical format:
* [[Bag of words]] (BoW)
* [[TF-IDF]]
* Word Embeddings (Word2Vec, GloVe, FastText)
* Contextual embeddings (BERT, GPT tokenization).
