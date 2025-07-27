---
aliases: []
category: CS
date modified: 27-07-2025
tags: [data_structure]
---
In [[algorithms]], a heap is a specialized [[binary tree]]-based data structure that satisfies the heap property: 

==each parent node is either greater than or equal to (max-heap) or less than or equal to (min-heap) its children.==

Locally ordered.
## Key Characteristics

| Feature        | Description                                                                     |
| -------------- | ------------------------------------------------------------------------------- |
| Structure  | Typically implemented as a binary heap stored in an array.              |
| Use Cases  | Priority queues, heapsort, scheduling, Dijkstra’s and Prim’s algorithms.        |
| Efficiency | `insert()` and `extract_min()` / `extract_max()` run in $O(\log n)$ time. |

## Why Use a Heap?

### Efficient Priority Queue

* Provides constant-time access to the highest- or lowest-priority element.
* Suitable when priorities change over time or are not known up front.
* Use cases: task schedulers, event-driven simulation, packet routing.

### Repeated Min/Max Extraction

* Ideal for problems that require frequent ==retrieval and removal of extremal elements while maintaining partial order==.
* Time complexity:
  * `insert()`: $O(\log n)$
  * `extract_min()` / `extract_max()`: $O(\log n)$
  * `peek_min()` / `peek_max()`: $O(1)$

## When to Use a Heap

Use a heap when your problem involves:
* Maintaining a dynamic priority queue.
* Fast access to the smallest or largest element.
* Efficient partial ordering without full sorting.
* Managing a sliding or streaming window of values (e.g. top-k, median).

## Python Example (Min-Heap)

```python
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

print(heapq.heappop(heap))  # Output: 1
```
