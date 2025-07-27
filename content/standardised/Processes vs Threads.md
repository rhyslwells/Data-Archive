---
aliases: []
category: CS
date modified: 27-07-2025
tags: [software]
---
The distinction between a process and a thread is foundational in [[computer science]] and systems programming. 

==Each process has one or more threads, but threads cannot exist outside a process.==

| Term        | Description                                                                                                                |
| ----------- | -------------------------------------------------------------------------------------------------------------------------- |
| Process | An instance of a program in execution, with its own memory space, system resources, and execution context. |
| Thread  | A unit of execution within a process. All threads in a process share the same memory and resources.                |
Analogy:
* A process is like a house: self-contained, isolated, with its own address, rooms, and locks.
* A thread is like a person inside the house: they share the same environment, can talk freely (shared memory), but can interfere with each other.

In Practice
* Use processes when you want full isolation and need to bypass the GIL for CPU-bound tasks.
* Use threads when tasks are I/O-bound and sharing memory is beneficial.
## Core Differences

| Aspect            | Process                                                                         | Thread                                                                          |
| ----------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [[Memory]]        | Each process has separate memory (heap, stack, etc.).                           | Threads share process memory (global [[Heap Memory]]) but have separate stacks.        |
| Isolation         | Fully isolated from other processes.                                            | Not isolated: changes in memory affect all threads.                             |
| Communication     | Requires inter-process communication (IPC) mechanisms (pipes, queues, sockets). | Communication is simpler via shared memory, but prone to [[race conditions]].   |
| Crash Impact      | Crash in one process typically does not affect others.                          | Crash in one thread may take down the whole process.                            |
| Creation Overhead | Higher: requires setting up memory space, resources.                            | Lower: threads are more lightweight.                                            |
| Context Switching | More costly: involves ==switching between separate memory contexts.==           | Faster: threads switch within the ==same process context.==                     |
| Typical Use       | For [[parallelism]], running independent tasks.                                 | For [[concurrency]], especially when tasks ==need to share data or resources.== |


```python
from multiprocessing import Process
from threading import Thread
```
