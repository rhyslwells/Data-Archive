---
aliases: []
category: CS
date modified: 27-07-2025
tags: []
---
The difference between [[multiprocessing]] and multithreading lies primarily in how [[concurrency]] is achieved, the resources used, and Python-specific constraints like the Global Interpreter Lock (GIL).

Related:
- [[Global Interpreter Lock]]

| Term                | Description                                                                     |
| ------------------- | ------------------------------------------------------------------------------- |
| [[Multiprocessing]] | Uses multiple processes, each with its own Python interpreter and memory space. |
| [[Multithreading]]  | Uses multiple threads within a single process, sharing the same memory space.   |

Key Differences:

| Aspect              | Multiprocessing                                                  | Multithreading                                                              |
| ------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Memory Space    | Each process has its own memory.                                 | Threads share the same memory space.                                        |
| CPU Utilization | Can use multiple CPU cores fully.                                | Limited by GIL in CPython (only one thread runs Python bytecode at a time). |
| Overhead        | Higher: more memory, process startup time.                           | Lower: threads are lightweight to spawn.                                        |
| Data Sharing    | Requires IPC (Inter-Process Communication) like Queues or Pipes. | Shared memory makes data sharing easier but riskier.                            |
| Best For        | CPU-bound tasks (e.g. image processing, computation).            | I/O-bound tasks (e.g. file/network access).                                 |
| Crash Safety    | One process crash doesn't affect others.                         | A crash in one thread can crash the whole process.                              |

Use Case Summary:

| Use Case                                                             | Recommendation            |
| -------------------------------------------------------------------- | ------------------------- |
| ==CPU-intensive== (e.g. matrix multiplication, image classification) | Multiprocessing           |
| ==I/O-intensive== (e.g. downloading files, database queries)         | Multithreading            |
| Parallelizing EasyOCR on multiple images                             | Multiprocessing           |
| Handling many simultaneous HTTP requests                             | Multithreading or AsyncIO |

