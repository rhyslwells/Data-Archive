---
aliases: []
category: LANG
date modified: 27-09-2025
tags:
- NLP
- python
---
Word2Vec is a technique for generating vector representations of words. Developed by researchers at Google, it uses a shallow [[Neural network]] to produce [[Vector Embedding|word embedding]] that capture [[Semantic Relationships]] and [[syntactic relationships]]. Word2Vec has two main architectures:

In [[ML_Tools]] see: [[Word2Vec.py]]

1. CBOW (Continuous [[Bag of words]]):
    - Predicts a target word given its context (neighboring words).
    - Efficient for smaller datasets.
      
2. Skip-Gram:
    - Predicts the context words given a target word.
    - Performs better on larger datasets.

Word2Vec generates dense, continuous vector representations where words with similar meanings are close to each other in the embedding space. For example:

- `vector("king") - vector("man") + vector("woman") ≈ vector("queen")`

Uses Negative [[Resampling]].