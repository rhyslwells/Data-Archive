---
tags:
  - NLP
---


Two forms [[Extraction]] and [[Abstraction]]

[[Abstraction]] method tries to generate a summary based on the text including new words. (complex)

[[Extraction]]: selecting certain words or sentences from the text and creating summary using them.

The basic idea behind unsupervised summarization is the following:
- split text into sentences;
- tokenize sentences into separate words;
- ==assign scores== to sentences based on importance;
- select several top sentences and display them in original order;

The main point, obviously, is assigning scores to sentences. Here are some of the ways to do this:
- calculate similarity between each pair of sentences and select sentences which are most similar to most sentences;
- calculate word frequences, select most frequent words and select sentences which have most of these words;
## Scores between similar sentences

similar to most sentence

## Scores of sentences with frequent words

