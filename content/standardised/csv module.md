---
aliases: []
category: 
date modified: 27-07-2025
tags: []
---
[[Python]]

| Feature                    | `csv` (standard lib)              | `pandas.to_csv()`                          |
| -------------------------- | --------------------------------- | ------------------------------------------ |
| Library                    | Built-in (`import csv`)           | External (`pandas`, requires install)      |
| Input/Output               | Lists, dicts                      | `DataFrame`                                |
| Header row                 | Manual (`writer.writerow([...])`) | Automatic from column names                |
| Data formatting            | Manual                            | Handles types like datetime, NaNs, etc.    |
| Performance (large data)   | Very fast for simple use cases    | Optimized for large tables                 |
| Compression (gzip, bz2...) | Not supported natively            | Built-in support via `compression=`        |
| Index export               | N/A                               | Optional (`index=False`)                   |
| Multi-index export         | Not supported                     | Supported                                  |
| Handling of nulls          | Manual                            | Automatic (e.g., NaN becomes empty string) |
| Type preservation          | Manual                            | Preserves types (to the extent CSV allows) |
| Append mode                | Easy (`open(..., 'a')`)           | Possible but requires care                 |

---

## 🔹 Example Comparison

### 1. **Using `csv`**

```python
import csv

data = [
    ['name', 'age'],
    ['Alice', 30],
    ['Bob', 25]
]

with open('people.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
```

You are responsible for formatting rows as lists (or dicts with `DictWriter`).

---

### 2. **Using `pandas.to_csv()`**

```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'age': [30, 25]
})

df.to_csv('people.csv', index=False)
```

No manual row handling — `pandas` handles headers, data alignment, and types.

---

## 🔸 When to Use Each

### Use `csv` if:

* You’re not using pandas.
* You need lightweight scripts with zero dependencies.
* You're working with custom file formats (e.g., pipe-delimited, legacy systems).
* You're writing line-by-line or in memory-constrained environments.

### Use `pandas.to_csv()` if:

* You're already working with DataFrames.
* You want fast, bulk export of structured tabular data.
* You need features like compression, encoding control, or null handling.
