---
aliases: []
category: LANG
date modified: 27-09-2025
tags:
- deep_learning
- NLP
---
Multi-head attention extends the standard [[Attention mechanism]] by enabling the model to attend to different parts of an input sequence simultaneously, capturing diverse relationships-both local and global.

#### Why Use Multi-Head Attention?

* Multiple Focus Areas: Each head attends to different parts of the sequence. Some capture short-range (syntactic) relationships, others long-range (semantic) dependencies.
* Diverse Representations: Each head operates in a distinct learned subspace, allowing the model to represent the same input in multiple ways.
* Richer Contextual Understanding: By aggregating these views, the model gains a more expressive and nuanced understanding of the input.

#### How It Works (Simplified Steps)

1. Linear Projections: Input tokens are projected into queries ($Q$), keys ($K$), and values ($V$) separately for each head.
2. Independent Attention: Each head computes attention scores and outputs a context vector.
3. Concatenation: Outputs from all heads are concatenated.
4. Final Projection: A linear transformation combines the multi-head output into a single vector.

#### Example Applications

In language translation, heads might focus on:
  * Aligning subject-verb structures
  * Resolving pronoun references
  * Handling grammatical reordering between source and target languages

In semantic tasks, they can disambiguate words (e.g., “bank” as riverbank or financial institution) by attending to context.
