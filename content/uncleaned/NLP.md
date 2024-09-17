
- [ ] Make a project [[Alice in Wonderland]]

## Notes:

A word is in a document which is in a corpus.

[[Feature Preprocessing]]:

	[[Normalisation of text]]
	[[Part of speech tagging]] : assigning a specific part-of-speech category (such as noun, verb, adjective, etc.) to each word in a text

Models:
	[[Bag of words]]: takes key terms of a text in normalised ==unordered== form.
	[[TF-IDF]] : Improves on [[Bag of words]] with Word importance measure.

Analysis:
	[[One Hot Encoding]]: Gives True or False for the word vector, if word from a list appears in the given text.

Methods:
	[[Ngrams]]: Creates tokens from groupings of words not just single words.
	[[Grammar method]]

Actions:
	[[Summarisation]]
	[[Word cloud]]
## Imports

[[NLP]] general imports

```python
import re

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer

porter_stemmer = PorterStemmer()
wodnet_lemmatizer = WordNetLemmatizer()

```

[[nltk]]

punkt: is an unsupervised trainable model

stopwords: words which, due to their high frequency in text, often don’t offer significant insights on their own.

wordnet: database of the English language that relates words to each other in terms of synonyms, hypernyms, hyponym

re : is regular expressions, for pattern matching

