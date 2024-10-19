---
title: 
tags:
  - NLP
aliases: 
category:
---
In the context of natural language processing (NLP), the Bag of Words (BoW) model is a simple and commonly used ==method for text representation==. It converts text data into numerical form by treating each ==document as a collection of individual words, disregarding grammar and word order==. Here's how it works:

1. Vocabulary Creation: A vocabulary is created from the entire corpus, which is a list of all unique words appearing in the documents.

2. Vector Representation: Each document is represented as a vector, where each element corresponds to a word in the vocabulary. The value of each element is typically the count of occurrences of the word in the document.

3. Simplicity and Limitations: While BoW is easy to implement and useful for tasks like text classification, it has limitations. It ignores word order and context, and can result in large, sparse vectors for large vocabularies.

Despite its simplicity, BoW can be effective for certain NLP tasks, especially when combined with other techniques like [[TF-IDF]] to weigh the importance of words.

Takes key terms of a text in normalised ==unordered== form.

`CountVectorizer` from scikit-learn to convert a collection of text documents into a matrix of token counts.

```python
#Need normalize_document
from sklearn.feature_extraction.text import CountVectorizer

# Using CountVectorizer with the custom tokenizer
bow = CountVectorizer(tokenizer=normalize_document)
bow.fit(corpus)  # Fitting text to this model
print(bow.get_feature_names_out())  # Key terms
```

Represent each sentence by a vector of length determined by get_feature_names_out. representing the tokens contained.