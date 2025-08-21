BM25 (Best Match 25)

BM25 is a **ranking function** widely used in search engines (e.g., Elasticsearch, Whoosh, Lucene). It’s an extension of **TF-IDF** with improvements for handling term frequency and document length.

### Formula:

For a document \$D\$ and query \$Q\$, the BM25 score is:

$$
\text{BM25}(D, Q) = \sum_{t \in Q} IDF(t) \cdot \frac{f(t,D) \cdot (k_1 + 1)}{f(t,D) + k_1 \cdot (1 - b + b \cdot \frac{|D|}{\text{avgdl}})}
$$

Where:

* \$f(t,D)\$ = term frequency of term \$t\$ in document \$D\$
* \$|D|\$ = length of document \$D\$ (number of words)
* \$\text{avgdl}\$ = average document length across all docs
* \$k\_1\$ (usually \~1.2–2.0) controls **term frequency saturation** (diminishing returns after many repetitions).
* \$b\$ (usually \~0.75) controls **length normalization** (longer documents don’t get unfair advantage).
* \$IDF(t)\$ = inverse document frequency:

  $$
  IDF(t) = \log \frac{N - n_t + 0.5}{n_t + 0.5}
  $$

  where \$N\$ is total number of docs, \$n\_t\$ is number of docs containing \$t\$.

### Intuition:

* **Term Frequency**: More occurrences of a query term increase relevance, but with diminishing returns.
* **Inverse Document Frequency**: Rare terms are more discriminative, so they’re weighted higher.
* **Document Length Normalization**: A term in a shorter document is more meaningful than in a very long one.

### Example (simplified):

Suppose query = "data science".

* Doc1: "data science is growing fast"
* Doc2: "big data in business and industry"

BM25 will:
* Give high score to Doc1 since it contains both "data" and "science".
* Score Doc2 lower because it lacks "science".
* Adjust for length: if Doc2 were extremely long, the contribution of "data" would be dampened.