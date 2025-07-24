---
tags: 
category: 
aliases:
  - GIL
---

In CPython, the Global Interpreter Lock allows only one thread to execute Python bytecode at a time. 

This makes [[Multithreading]] inefficient for CPU-bound tasks, but still useful for I/O-bound tasks. 

[[Multiprocessing]] avoids this limitation entirely by running each process with its own interpreter and GIL.