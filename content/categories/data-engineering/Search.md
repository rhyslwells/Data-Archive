---
aliases: []
category: DE
date modified: 27-09-2025
tags:
- exploration
- mlprocess
- NLP
---
Aims of any search:
1. Speed
2. Accuracy (Precision)
3. Ease of use 
4. Comprehensiveness
5. Freshness
## How Search Algorithms Work (in Information Retrieval)

When you type a query into a search engine (e.g., "machine learning applications in healthcare"), the system must:

**Index documents**
   * Before searching, all documents are processed into an **inverted index** (a mapping from terms → list of documents where they appear).
   * Example:
     * "data" → {doc1, doc3, doc7}
     * "learning" → {doc2, doc3, doc4}

**Retrieve candidate documents**
   * Using the inverted index, the system finds documents containing at least one of the query terms.

**Rank the documents**
   * The system applies a **ranking function** (scoring model) to order documents by relevance to the query.
   * Early methods: Boolean matching (exact matches).
   * More advanced: Vector Space Models ([[TF-IDF]], [[BM25 (Best Match 25)]]), Neural embeddings, Transformers ([[BERT]]).

**Return top results**
   * Usually top-10 or top-100 documents are returned.

In short:
* **Search algorithms**: retrieve and rank documents.
* **BM25**: a probabilistic ranking function that balances **term frequency**, **term rarity**, and **document length**.
