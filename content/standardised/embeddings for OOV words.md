Can you find words in a [[Vector Embedding|word embedding]] that where not used to creates the embedding?

Yes, but with important caveats. If a word is not in the [[spaCy]] model’s vocabulary with a vector, then:

### ✅ What you can do

#### Option 1: Filter out words without vectors (what you're doing now)
This is the cleanest option:
```python
if token.has_vector:
    embeddings.append(token.vector)
    valid_words.append(word)
```

#### Option 2: Fallback to character-level embeddings (optional)
If you're using `en_core_web_lg`, spaCy sometimes provides approximate vectors for out-of-vocabulary (OOV) words using subword features. But with `en_core_web_md`, OOV words truly lack vector meaning.

#### Option 3: Use a different embedding model
Use FastText or transformer-based models (e.g., Sentence Transformers), which can produce [[embeddings for OOV words]] based on subword information or context.

Example with [[FastText]] (using gensim):
```python
from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format("cc.en.300.vec")  # or download from FastText
embedding = model.get_vector("unseenword")  # FastText will synthesize it
```

### 💡 Summary

| Approach                     | Handles OOV? | Notes |
|-----------------------------|--------------|-------|
| spaCy `en_core_web_md`      | ❌            | Skips words without vectors (recommended) |
| spaCy `en_core_web_lg`      | ⚠️ Sometimes  | May infer vectors using subword info |
| FastText / GloVe            | ✅            | Good for unseen words |
| Sentence Transformers (BERT)| ✅            | Contextualized, ideal for phrases/sentences |

#NLP #ml_process #ml_optimisation