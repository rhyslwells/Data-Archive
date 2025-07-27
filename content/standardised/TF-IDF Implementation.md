---
aliases: []
category:
date modified: 27-07-2025
tags: []
---
## TF-IDF Implementation 

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