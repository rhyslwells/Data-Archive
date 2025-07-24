---
tags:
  - ml_process
  - engineering
  - software
category: DE
---
## What Is Multiprocessing?

Multiprocessing is a form of *parallelism* that allows a program to execute multiple tasks simultaneously by using multiple CPU cores. Unlike [[Multithreading]] (which shares the same memory space), multiprocessing involves separate memory spaces, each with its own Python interpreter. This avoids Python’s [[Global Interpreter Lock]] (GIL), making it well-suited for CPU-bound tasks.

Related:
[[Multiprocessing vs Multithreading]]
## Why Multiprocessing in Python?

Python's GIL prevents true multithreading in CPython when performing CPU-bound operations. Multiprocessing sidesteps this by creating independent processes, thus taking advantage of multiple CPU cores.

Python provides this functionality via the `multiprocessing` module in the standard library.
## How Is It Done in Python?

### 1. Basic Usage: `multiprocessing.Process`

```python
from multiprocessing import Process

def task():
    print("Running in a separate process")

p = Process(target=task)
p.start()
p.join()
```

Each `Process` runs in its own memory space and executes independently.

### 2. Using `multiprocessing.Pool` (simplified parallel mapping)

```python
from multiprocessing import Pool

def square(x):
    return x * x

with Pool(processes=4) as pool:
    results = pool.map(square, [1, 2, 3, 4, 5])
    print(results)  # Output: [1, 4, 9, 16, 25]
```

`Pool` is useful when you want to apply a function to a collection of data in parallel.

### 3. Using `multiprocessing.Queue` and `multiprocessing.Pipe` for Interprocess Communication (IPC)

```python
from multiprocessing import Process, Queue

def f(q):
    q.put('Hello from process')

q = Queue()
p = Process(target=f, args=(q,))
p.start()
print(q.get())  # prints 'Hello from process'
p.join()
```

### 4. Shared Memory via `Value` or `Array`

```python
from multiprocessing import Process, Value

def f(n):
    n.value += 1

num = Value('i', 0)
p = Process(target=f, args=(num,))
p.start()
p.join()
print(num.value)  # 1
```

## Use Cases of Multiprocessing

### 1. CPU-Bound Tasks

Tasks that require intensive computation:
* Image or video processing
* Mathematical simulations
* Data transformations or encodings
* Cryptographic computations

### 2. [[Batch Processing]] of Independent Jobs
* Applying a model to independent chunks of data
* OCR on many files (e.g., with EasyOCR)

### 3. Pipeline Stages in Data Processing

Different processes handling different stages:
* Process 1: Reading data
* Process 2: Transformation
* Process 3: Writing to disk or DB

This can be coordinated using `Queue`s or `Pipe`s.

## When Not to Use It

* When the task is I/O-bound → prefer `asyncio` or `multithreading`.
* When overhead from starting processes outweighs benefits (e.g., tiny jobs).
* When memory sharing is important — inter-process communication is more complex than threads.
## Related Tools and Libraries

* `joblib`: High-level interface, useful in [[scikit-learn]].
* `concurrent.futures.ProcessPoolExecutor`: Modern interface for multiprocessing.
* `ray`, `dask`, `loky`: Advanced distributed and parallel processing.
