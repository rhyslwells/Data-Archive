---
aliases:
- TFIDF
category: LANG
date modified: 27-09-2025
tags:
- code_snippet
- NLP
- preprocessing
---
TF-IDF is a statistical technique used in text analysis to determine the importance of a word in a document relative to a collection of documents (corpus). It balances two ideas:

- Term Frequency (TF): Captures how often a term occurs in a document.
- Inverse Document Frequency (IDF): Discounts terms that appear in many documents.

High TF-IDF scores indicate terms that are frequent in a document but rare in the corpus, making them useful for distinguishing between documents in tasks such as information retrieval, document classification, and recommendation.

TF-IDF combines local and global term [[Statistics]]:
- TF gives high scores to frequent terms in a document
- IDF reduces the weight of common terms across documents
- TF-IDF identifies terms that are both frequent and distinctive

Can be used to give an initial snapshot of a notes themes and topic.
### Equations

#### Term Frequency

$TF(t, d)$ measures how often a term $t$ appears in a document $d$, normalized by the total number of terms in $d$:

$$
TF(t, d) = \frac{f_{t,d}}{\sum_k f_{k,d}}
$$

Where:
- $f_{t,d}$ is the raw count of term $t$ in document $d$  
- $\sum_k f_{k,d}$ is the total number of terms in $d$ (i.e. the document length)

#### Inverse Document Frequency

IDF assigns lower weights to frequent terms:

$$
IDF(t, D) = \log \left( \frac{N}{1 + |\{d \in D : t \in d\}|} \right)
$$

Where:
- $N$ is the number of documents in the corpus $D$  
- $|\{d \in D : t \in d\}|$ is the number of documents containing term $t$  
- Adding 1 to the denominator avoids division by zero

#### TF-IDF Score

The final score is:

$$
TF\text{-}IDF(t, d, D) = TF(t, d) \times IDF(t, D)
$$

### Related Notes

- [[Bag of Words]]
- [[Tokenisation]]
- [[Clustering]]
- [[Search]]
- [[Recommender systems]]
- [[nltk]]
- [[TF-IDF Implementation]] <-

### Exploratory Ideas
- Can track TF-IDF over time (e.g., note evolution)
- Can cluster or classify the documents using TF-IDF?

