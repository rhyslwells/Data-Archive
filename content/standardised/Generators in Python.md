---
aliases: []
category:
date modified: 27-07-2025
tags: [data_pipeline, ml_process, python]
---
#### **Why use generators for processing large data?** 

**Generators** are [[Python]] constructs that yield values lazily, which means they don’t load everything into [[LLM Memory]]. This is ideal for **[[Data Streaming]] large datasets**, such as:

* Reading files line by line
* Processing massive CSV or JSONL logs
* Streaming from APIs or sockets
* Working with NLP corpora or web-scraped text

**Benefits:**
* Memory efficiency
* Composability of operations (via generator chains)
* Useful in I/O-heavy or parallelized workflows

**Example:**

```python
def read_lines(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            yield line.strip()

for line in read_lines("large_file.txt"):
    process(line)  # custom processing function
```

**Exploratory Questions:**
* Can we apply the same strategy for batched ML inference pipelines?
* When should we materialize a generator vs. keep it lazy?
* What limitations arise when [[debugging]] generators?

