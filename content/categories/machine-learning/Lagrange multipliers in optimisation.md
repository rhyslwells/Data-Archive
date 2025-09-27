---
aliases: []
category: ML
date modified: 27-09-2025
tags:
- math
- optimisation
---
Lagrange multipliers let us embed constraints into optimization problems, and many ML models (like SVMs and constrained likelihoods) rely on them.

Lagrange multipliers are a mathematical method for solving constrained optimization problems. In machine learning, they are used when we want to maximize or minimize a function subject to one or more constraints.
### General Idea

Suppose we want to minimize (or maximize): $f(x,y)$ subject to a constraint: $g(x,y) = c$. We introduce a new variable $\lambda$ (the Lagrange multiplier) and define the Lagrangian:

$\mathcal{L}(x,y,\lambda) = f(x,y) + \lambda \cdot (c - g(x,y))$

Then solve by setting derivatives = 0:

$\nabla{x,y,\lambda} \mathcal{L} = 0$

### Why It Matters in ML

Lagrange multipliers let us handle constraints directly in optimization problems common in machine learning. Examples:

[[Support Vector Machines|SVM]]
  * The optimization problem is: minimize margin loss subject to constraints on classification.
  * Lagrange multipliers are used to transform it into a dual problem, making the solution tractable.

[[Regularisation]]:
  * Can be seen as introducing constraints on weights (e.g., $|w|^2 \leq C$).
  * Lagrange multipliers turn this into a penalty term (like in ridge regression).

### Intuition
* Without constraints: move downhill on $f(x,y)$ until reaching the minimum.
* With constraints: must stay on the surface defined by $g(x,y) = c$.
* The Lagrange multiplier $\lambda$ balances the trade-off between optimizing $f$ and satisfying the constraint.




