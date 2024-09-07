---
tags:
  - NLP
---


Short term frequency inverse document frequency 

Improves on [[Bag of words]]

Reflects how important each word is to a document in a corpus. which takes into account both the frequency of a term in a document and the rarity of the term in the entire corpus

High values mean more important



**TF-IDF** equation:
- term frequency
$tf_{i,j} = \frac{n_{i,j}}{\sum_k n_{k,j}}$
- inverse document frequency
$idf(w) = \mbox{log} \frac{N}{df_i}$
- term frequency–inverse document frequency
$w_{i,j} = tf_{i,j} \times \mbox{log}\frac{N}{df_i}$
where:
- $i$ - index of term
- $j$ - index of document
- $k$ - number of terms in document
- $N$ - corpus length (number of documents)
- $df_i$ - number of documents containing term i

## Implementation

```python
from sklearn.feature_extraction.text import CountVectorizer
bow = CountVectorizer(tokenizer=normalize_document)
bow.fit(corpus)
corpus_vectorized = bow.transform(corpus)

from sklearn.feature_extraction.text import TfidfTransformer
tf_idf_transformer = TfidfTransformer()
tf_idf_transformer.fit(corpus_vectorized)

#frequencies per token.
#for term, freq in zip(bow.get_feature_names_out(), #tf_idf_transformer.idf_):
#    print(term.rjust(10), " : ", freq)
    
#can do per document in corpus
tfidf_docs = tf_idf_transformer.transform(corpus_vectorized)

for doc_id in range(len(corpus)):
    print("Document id.{}: {}".format(doc_id, corpus[doc_id]))
    print("Tokens: {}".format(normalize_document(corpus[doc_id])))
    print("\n -- TF IDF Values for words in dictionary:")
    
    # Filter out terms with TF-IDF frequency of 0
    non_zero_terms = [(term, freq) for term, freq in zip(bow.get_feature_names_out(), tfidf_docs[doc_id].T.toarray()) if freq != 0]

    for term, freq in non_zero_terms:
        print(term.rjust(10), " : ", freq)
    
    print("\n ------------------")


```

## Why are we interested in this method?

TF-IDF helps in capturing the uniqueness of terms within each document, which can be useful in tasks like document clustering [[Clustering classification]], information retrieval[[Search]], and content recommendation.[[Recommender systems]]