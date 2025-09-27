---
aliases:
- null
category: LANG
date modified: 27-09-2025
tags:
- NLP
---
N-grams are used in NLP that allow for the analysis of text data by breaking it down into smaller, manageable sequences. 

An **N-gram** is a contiguous sequence of *n* items (or tokens) from a given sample of text or speech. In the context of natural language processing ([[NLP]]) and text analysis, these items are typically words or characters. 

N-grams are used to analyze and ==model the structure of language==, and they can help in various tasks such as [[Text Classification]].
### Types of N-grams
- **Unigram**: An N-gram where *n = 1*. It represents individual words or tokens. For example, in the sentence "I love AI", the unigrams are ["I", "love", "AI"].

- **Bigram**: An N-gram where *n = 2*. It represents pairs of consecutive words. For the same sentence, the bigrams would be ["I love", "love AI"].

- **Higher-order N-grams**: These can go beyond three words, such as 4-grams (quadgrams) or 5-grams, and so on.
### Code implementations:

This can be does through kwargs in CountVectorizer.