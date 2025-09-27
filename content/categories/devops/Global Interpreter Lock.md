---
aliases:
- GIL
category: DEVOPS
date modified: 27-09-2025
tags:
- python
- system
---
In CPython, the Global Interpreter Lock allows only one thread to execute Python bytecode at a time. 

This makes [[Multithreading]] inefficient for CPU-bound tasks, but still useful for I/O-bound tasks. 

[[Multiprocessing]] avoids this limitation entirely by running each process with its own interpreter and GIL.