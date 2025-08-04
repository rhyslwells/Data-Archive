---
aliases: [LDA]
category: 
date modified: 1-08-2025
tags: [explainability, NLP]
---
Latent Dirichlet Allocation (LDA) is a generative probabilistic model used in Natural Language Processing (NLP) and machine learning for topic modeling. It assumes that documents are mixtures of topics, and topics are mixtures of words. The goal of LDA is to uncover the latent topics in a collection of text documents by identifying groups of words that frequently appear together in the same documents.

Libraries like gensim in Python are highlighted as being particularly suitable for topic modeling

### Key Concepts:
- Topic: A distribution over a fixed vocabulary of words. A topic might represent a certain theme, like "sports" or "politics."
- Document: A mixture of topics. A document is modeled as a combination of topics with different proportions.
- Words: Each word in the document is associated with a topic based on the topic proportions of that document.

### How LDA Works:
1. Assume each document has a mixture of topics: Each document is made up of a certain proportion of topics. For example, a document could be 70% about "sports" and 30% about "politics."
2. Assume each topic is a distribution of words: Each topic has a specific distribution over words. For example, the "sports" topic might have a high probability for words like "football," "game," and "score."
3. Infer the topics from the documents: LDA tries to discover these hidden topics from the words in the documents, without knowing the topics in advance.

### Why Use LDA?
- Topic Discovery: It helps discover hidden themes in a large corpus of text data.
- [[Dimensionality Reduction]]: LDA reduces the complexity of the text data by modeling it with a smaller number of topics instead of many individual words.

Related terms:
- [[topic modeling]]
- [[Semantic Relationships]]
- [[NLP]]
- [[Unsupervised Learning]]

## Example:

Imagine you have a set of three simple documents:

1. Document 1: "Football is a great sport"
2. Document 2: "Basketball is also fun to play"
3. Document 3: "Soccer and football are similar sports"

LDA might identify two topics:
- Topic 1: Words related to "sports" (e.g., "football," "basketball," "soccer").
- Topic 2: Words related to "competition" or "play" (e.g., "game," "score," "fun").

The algorithm would assign a mixture of these topics to each document based on the words in the documents.

### Example Code:

Here’s a simple implementation of LDA using `sklearn` in Python:

```python
import numpy as np
import pandas as pd
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

# Sample documents
docs = [
    "Football is a great sport",
    "Basketball is also fun to play",
    "Soccer and football are similar sports"
]

# Step 1: Convert the documents into a document-term matrix (DTM)
vectorizer = CountVectorizer(stop_words='english')
dtm = vectorizer.fit_transform(docs)

# Step 2: Apply LDA to discover topics
lda = LatentDirichletAllocation(n_components=2, random_state=42)
lda.fit(dtm)

# Step 3: Display topics
terms = vectorizer.get_feature_names_out()

for index, topic in enumerate(lda.components_):
    print(f"Topic #{index + 1}:")
    print([terms[i] for i in topic.argsort()[-5:]])  # Print the top 5 words in the topic
    print()

# Example Output:
# Topic #1:
# ['football', 'sports', 'game', 'score', 'play']
# Topic #2:
# ['basketball', 'soccer', 'sport', 'fun', 'great']
```

### Output Explanation:
- Topic might have words like football, sports, game, because these terms appear frequently in the documents related to sports.
- Topic could have terms like basketball, soccer, fun, because these are associated with the activities discussed in the documents.

### How to Interpret:
- Document 1 ("Football is a great sport"): LDA might classify this document as being 60% about Topic (sports-related) and 40% about Topic (competitive play).
- Document 2 ("Basketball is also fun to play"): LDA might classify this document as being 80% about Topic (competitive play) and 20% about Topic (sports-related).
