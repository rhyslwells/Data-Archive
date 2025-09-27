---
aliases: []
category: CS
date modified: 27-09-2025
tags:
- algorithm
---
### [[Recursive Algorithm]]

### Backtracking

Backtracking is a method for solving problems incrementally, by trying partial solutions and then abandoning them if they are not valid.

Example: Graph coloring with the 4-color theorem.

### Divide and Conquer

Divide and conquer is a strategy that involves breaking a problem into smaller subproblems of the same type, solving these subproblems recursively, and then combining their solutions to solve the original problem.

Example: Merge sort, where the array is split in half, and each smaller part is sorted.

Note: Subproblems do not generally overlap.

### Dynamic Programming

Dynamic programming is used for optimization problems and involves storing past results to find new results efficiently.

- [[Memoization]]: This technique "remembers" past results to avoid redundant calculations.
- It is characterized by overlapping substructure and overlapping subproblems.

Examples: Fibonacci numbers, Towers of Hanoi, etc.

### Greedy Algorithms

A greedy algorithm builds up a solution piece by piece, always choosing the next piece that offers the most immediate benefit without regard for future consequences. The hope is that by choosing a local optimum at each step, a global optimum will be reached.

Examples: Dijkstra's shortest path algorithm, Knapsack problem.

### Branch and Bound

Branch and bound algorithms are typically used for optimization problems and are similar to backtracking.

- As the algorithm progresses, a tree of subproblems is formed, with the original problem as the "root problem."
- A method is used to construct upper and lower bounds for a given problem.
- At each node, bounding methods are applied:
    - If the bounds match, it is deemed a feasible solution for that subproblem.
    - If the bounds do not match, the problem represented by that node is partitioned into two subproblems, which become child nodes.
- The process continues, using the best known feasible solution to trim sections of the tree until all nodes have been solved or trimmed.

Example: Traveling salesman problem.

### Brute Force

Brute force algorithms try all possible solutions until they find an optimized or satisfactory answer. Heuristics can be used to assist in this process.

### Randomized Algorithms

Randomized algorithms use random numbers to influence their behaviour.

Example: [[K-means]] clustering initialization.