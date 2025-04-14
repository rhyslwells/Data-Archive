---
tags:
  - NLP
  - preprocessing
  - code_snippet
aliases:
  - TFIDF
category: LANG
---
TF-IDF is a statistical technique used in text analysis to determine the importance of a word in a document relative to a collection of documents (corpus). It balances two ideas:

- Term Frequency (TF): Captures how often a term occurs in a document.
- Inverse Document Frequency (IDF): Discounts terms that appear in many documents.

High TF-IDF scores indicate terms that are frequent in a document but rare in the corpus, making them useful for distinguishing between documents in tasks such as information retrieval, document classification, and recommendation.

TF-IDF combines local and global term [[Statistics]]:
- TF gives high scores to frequent terms in a document
- IDF reduces the weight of common terms across documents
- TF-IDF identifies terms that are both frequent and distinctive

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

- [[Bag of words]]
- [[Tokenisation]]
- [[Clustering]]
- [[Search]]
- [[Recommender systems]]
- [[nltk]]

### Exploratory Ideas
- Can track TF-IDF over time (e.g., note evolution)
- Can cluster or classify the documents using TF-IDF?
## Implementations 

### Python Script (scikit-learn version)

```python
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

# Step 1: Tokenize and vectorize using Bag of Words
bow = CountVectorizer(tokenizer=normalize_document)
X_counts = bow.fit_transform(corpus)

# Step 2: Apply TF-IDF transformation
tfidf_transformer = TfidfTransformer()
X_tfidf = tfidf_transformer.fit_transform(X_counts)

# Optional: View TF-IDF scores per document
for doc_id in range(len(corpus)):
    print(f"Document {doc_id}: {corpus[doc_id]}")
    print("TF-IDF values:")
    tfidf_vector = X_tfidf[doc_id].T.toarray()
    for term, score in zip(bow.get_feature_names_out(), tfidf_vector):
        if score > 0:
            print(f"{term.rjust(10)} : {score[0]:.4f}")
```

### Python Script (custom TF-IDF implementation)

```python
import math
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.util import bigrams, trigrams

stop_words = stopwords.words('english')
tokenizer = RegexpTokenizer(r'\w+')

def tokenize(text):
    tokens = tokenizer.tokenize(text.lower())
    tokens = [t for t in tokens if len(t) > 2 and t not in stop_words]
    return tokens + [' '.join(b) for b in bigrams(tokens)] + [' '.join(t) for t in trigrams(tokens)]

def tf(term, doc_tokens):
    return doc_tokens.count(term) / len(doc_tokens)

def idf(term, docs_tokens):
    doc_count = sum(1 for doc in docs_tokens if term in doc)
    return math.log(len(docs_tokens) / (1 + doc_count))

def compute_tfidf(docs):
    docs_tokens = [tokenize(doc) for doc in docs]
    all_terms = set(term for doc in docs_tokens for term in doc)
    tfidf_scores = []
    for tokens in docs_tokens:
        tfidf = {}
        for term in all_terms:
            if term in tokens:
                tfidf[term] = tf(term, tokens) * idf(term, docs_tokens)
        tfidf_scores.append(tfidf)
    return tfidf_scores
```



