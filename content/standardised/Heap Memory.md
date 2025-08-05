---
aliases: 
category: CS
date modified: 27-07-2025
tags:
  - memory_management
---

In systems and programming, the heap is a region of a program’s memory used for ==dynamic memory allocation.==

Characteristics:

| Feature     | Description                                                                                         |
| ----------- | --------------------------------------------------------------------------------------------------- |
| Purpose     | Stores variables that are created at runtime and need to persist beyond the current function scope. |
| Managed By  | The programmer or runtime environment (e.g., [[garbage collector]] in Python or Java).              |
| Lifetime    | Data persists until manually deallocated (C/C++) or garbage-collected (Python, Java).               |
| Access      | Slower than [[stack memory]] due to indirect referencing and fragmentation.                         |
| Example Use | Objects, data structures (e.g., lists, trees), large arrays.                                        |

In Python:

```python
a = [1, 2, 3]  # List stored on the heap, reference stored in variable `a`
```

The actual list is allocated on the heap; `a` holds a reference to that memory.