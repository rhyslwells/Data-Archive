---
aliases: []
category:
date modified: 27-07-2025
tags: []
---
https://github.com/rhyslwells/ML_Tools/blob/main/Explorations/Build/NLP/Vector_Embedding.py

### Explanation of the Script

1. **Vocabulary and Embedding Layer**:
    - Terms are mapped to indices using a dictionary.
    - The embedding layer learns continuous vector representations for these terms.
      
2. **Cosine Similarity**:
    - The cosine similarity function measures how similar two terms are in the embedding space. Higher values indicate closer relationships.
      
3. **Visualization**:
    - Embeddings are plotted in a 2D space to show semantic relationships. Terms with similar meanings (e.g., "king" and "queen") are expected to cluster together.
      
4. **t-SNE for Dimensionality Reduction**:
    - If the embedding dimension is higher than 2, t-SNE can reduce it to 2D for visualization while preserving semantic relationships.

### Outputs

1. **Cosine Similarities**:
    - Pairwise similarity scores between terms to quantify their semantic closeness.
      
2. **Visualization**:
    - A scatter plot showing the positions of terms in the embedding space.