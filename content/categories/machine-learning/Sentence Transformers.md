---
aliases: []
category: ML
date modified: 27-09-2025
tags:
- deep_learning
- NLP
---
Sentence [[Transformer|Transformers]] are models built on top of transformer architectures like [[BERT]], fine-tuned to generate semantic sentence embeddings. Unlike BERT, which produces token-level outputs pooled into sentence representations, Sentence Transformers are trained to directly capture meaningful sentence-level semantics through supervised training on sentence pairs.

Why Use Sentence Transformers Instead of BERT?
- Standard BERT embeddings are not optimized for measuring [[Semantic Relationships|semantic similarity]]. They rely on simple pooling methods (e.g. mean pooling), which treat all tokens equally and often fail to reflect sentence meaning accurately.

Sentence Transformers overcome this by:
* Using a twin (siamese) architecture where sentence pairs are passed through a shared encoder.
* Being fine-tuned on tasks like semantic similarity, paraphrase detection, and natural language [[inference]], enabling them to learn relational meaning between sentences.
* Producing embeddings that are directly comparable using metrics like [[Cosine Similarity]].

As a result, Sentence Transformers perform significantly better on:
* Semantic search
* [[Vector Embedding|Embedding]] texts for semantic search and ranking
* Clustering or grouping short texts
* Comparing the similarity of sentence or query pairs

 Key Questions to Explore
* When is fine-tuning necessary, and how does it impact embedding quality?
* Which model variants (e.g. `all-MiniLM`, `mpnet`) are best for your task?
* [ ] When is Sentence -BERT preferable over base BERT or other transformer models?

Related:
- [[Sentence Transformer Workflow]]
