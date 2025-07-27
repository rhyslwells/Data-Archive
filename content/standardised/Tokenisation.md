---
aliases: []
category: LANG
date modified: 27-07-2025
tags: [code_snippet, NLP, preprocessing]
---
Tokenisation is a core step in natural language processing ([[NLP]]) where raw text is split into smaller units known as tokens. These tokens can be words, sentences, or subwords, depending on the level of analysis. Tokenisation prepares text for downstream tasks like embedding, classification, or parsing.

There are different kinds: [[spaCy]] or [[Hugging Face]] tokenisers.

### Types of Tokenisation

#### 1. Word Tokenisation

Splits text into individual words and retains punctuation.

```python
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text_original)
print(tokens)
```

#### 2. Sentence Tokenisation

Segments text into full sentences.

```python
from nltk.tokenize import sent_tokenize
sentences = sent_tokenize(text_original)
print(sentences)
```

#### 3. Custom Tokenisation with Cleaning

For cleaner preprocessing (e.g. lowercasing, removing non-alphanumerics and stopwords):

```python
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

temp = text_original.lower()
temp = re.sub(r"[^a-zA-Z0-9]", " ", temp)      # keep only letters and numbers
temp = re.sub(r"[[0-9]+\]", "", temp)         # remove bracketed numbers
tokens = word_tokenize(temp)
tokens_clean = [t for t in tokens if t not in stopwords.words("english")]
print(tokens_clean)
```

### Special Tokens in [[Transformer]] Models

Modern models like [[BERT]] use special tokens during tokenisation to preserve input structure:
* [CLS]: Marks the start of the input sequence; used for classification tasks.
* [SEP]: Separates different segments (e.g. question from context in QA tasks).

### Related:
- [[nltk]]