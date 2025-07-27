---
aliases: []
category:
date modified: 27-07-2025
tags: [NLP]
---
In [[NLP|Natural Language Processing]] (NLP), OOV words refers to:

> OOV words are terms not seen during training or not present in a model’s vocabulary. They pose challenges for text understanding, especially in traditional NLP approaches. Modern tokenization strategies (e.g., subwords) greatly reduce—but do not entirely eliminate—the issue.
### Modern NLP Models

Modern transformer-based models (e.g., BERT, GPT) almost eliminate the concept of OOV by using subword [[Tokenisation]]:
- Any word, even if unseen, can be broken into known subword units.
- However, this still has semantic implications: e.g., rare words may be split into unintuitive or ambiguous fragments.

### Context and Meaning

Many NLP models (e.g., classical models like [[Bag of words]], or early word embeddings like [[Word2vec]]) rely on a fixed vocabulary that was built from a training corpus. Any word not seen during training is considered out-of-vocabulary.
### Why OOV Words Matter

1. Loss of information: If a model cannot represent or process a word (e.g., "microservices" or a new slang term), it cannot reason about its meaning.
2. Performance degradation: In text classification, machine translation, or entity recognition tasks, frequent OOV words reduce the model’s accuracy.
3. Domain adaptation challenges: OOV words often appear in domain-specific or noisy data (e.g., medical, legal, user-generated content).
### Strategies to Handle OOV Words

| Strategy                   | Description                                                                        | Common Usage                         |
| -------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------ |
| UNK token                  | Map all unknown words to a special token like `<UNK>`                              | Basic [[Recurrent Neural Networks|RNN]] models, early NLP          |
| Subword tokenization       | Break OOV words into smaller known parts (e.g., BPE, ==WordPiece==, SentencePiece) | Used in BERT, GPT, RoBERTa           |
| Character-level models     | Process input character-by-character, avoiding fixed vocabulary                    | Useful in noisy or multilingual text |
| Dynamic vocabulary updates | Re-train or extend embeddings on new corpora                                       | Custom applications                  |
### Example

Assume a vocabulary contains:

```python
["cat", "dog", "runs", "the", "fast"]
```

Now, the sentence:

```text
"The cheetah runs fast"
```

 “cheetah” is not in the vocabulary → it's an OOV word.
 
 A model may:

   - Replace it with `<UNK>`: `"the <UNK> runs fast"`
   - Use subwords: `"the chee ##tah runs fast"` (WordPiece-style)



