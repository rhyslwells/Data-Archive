[[Part of speech tagging]] : assigning a specific part-of-speech category (such as noun, verb, adjective, etc.) to each word in a text

Part-of-speech tagging involves assigning a specific part-of-speech category (such as noun, verb, adjective, etc.) to each word in a text
```python
from nltk import pos_tag
pos_tag(temp[:20])
```
will get outputs such as [('history', 'NN'), ('poland', 'NN'), ('roots', 'NNS'), ('early', 'JJ').