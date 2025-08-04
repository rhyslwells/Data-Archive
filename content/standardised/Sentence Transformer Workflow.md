---
aliases: 
category: 
date modified: 27-07-2025
tags:
  - process
  - NLP
---
### Sentence Transformer Workflow 

#### Step 1: Input Sentence Pair

* Input consists of two sentences: A and B.
* Both are processed independently using the same [[BERT]] model (a twin/siamese network).

#### Step 2: [[Vector Embedding|Embedding]] Extraction

* Sentences A and B are passed separately through BERT.
* Each yields a fixed-size embedding vector: $a = \text{Embed}(A), b = \text{Embed}(B)$.

#### Step 3: Compute Difference and Combine

* Compute absolute difference: |a - b|.
* Form a combined vector: $\[a; b; |a - b|].

#### Step 4: Feedforward Neural Network ([[Feed Forward Neural Network|FFNN]])

* Pass the combined vector through a two-layer FFNN.
* Output is a set of raw logits (real-valued scores for each class).

#### Step 5: [[Classification]] via Softmax

* Apply softmax to logits to get class probabilities.
* The class with the highest probability is selected.