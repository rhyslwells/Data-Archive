---
aliases: 
category: 
date modified: 27-07-2025
tags:
  - NLP
---
https://www.youtube.com/shorts/Muvjex0nkes

[[Self Attention]]: Take every word pays attention to every other word to capture context by:
1. take input word vectors,
2. break words into Q,K,V vectors,
3. compute attention matrix
4. generate final word vectors.

[[Multi-head attention]]: perform self attention in parallel.
1. take word vectors,
2. break words into Q,K,V vectors,
	1. Break each Q,K,V vector into the number of heads parts
3. compute attention matrix for each head
4. generate final word vectors for each head
5. Combine back together

These have better understanding of the context.