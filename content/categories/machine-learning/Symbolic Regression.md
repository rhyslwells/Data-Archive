---
aliases: []
category: ML
date modified: 28-03-2026
tags:
  - interpretability
  - ml
  - optimisation
---
Symbolic regression (SR) searches for an explicit functional form $y = f(X)$ by exploring a space of mathematical expressions. Both the structure of the model and its parameters are learned simultaneously.

**Example output**:
$y = 2.1x_1 + \log(x_2) - 0.5x_3^2$

Expressions are typically represented as trees:

* Internal nodes: operators ($+, -, \times, \div, \sin, \exp$)
* Leaves: variables and constants
## Core Mechanism

### Genetic Programming (GP)

SR is usually implemented via evolutionary search over expression trees.

* **Population**: a set of candidate formulas
* **Evaluation**: each formula is scored using a loss (e.g. MSE)
* **Selection**: better formulas are retained
* **Crossover**: subtrees are swapped between formulas
* **Mutation**: random structural or operator changes

The process iterates over generations.
## Objective Function and Parsimony

To control overfitting and expression growth, SR optimises:

$$
\text{Fitness} = \text{Error} + \alpha \cdot \text{Complexity}
$$

* Complexity measures tree size / operator cost
* $\alpha$ controls the simplicity–accuracy trade-off

The result is a **Pareto front**: a set of non-dominated models balancing error and complexity.
## Practical Workflow

Given feature matrix $X$ and target $y$:

1. Initialise random expression trees
2. Evaluate each candidate: $f_\theta(X)$ vs $y$
3. Evolve population via crossover and mutation
4. Extract Pareto-optimal equations

### Example (PySR)

```python
from pysr import PySRRegressor

model = PySRRegressor(
    niterations=100,
    binary_operators=["+", "-", "*", "/"],
    unary_operators=["sin", "exp", "inv(x) = 1/x"],
    complexity_of_operators={"sin": 2, "exp": 3},
)

model.fit(X, y)

model.equations_  # Pareto front
```

## Computational Profile

* **Time**: high (search over expression space)
* **Memory**: relatively low
* **Scaling**: worsens with feature count and operator set size

Suitable for long-running batch processes (e.g. headless execution on low-power systems).

## Behavioural Properties

### Extrapolation

Because the model is an explicit function, it can extrapolate beyond training data.

Example:
If $y = 2x$, then $x=100 \Rightarrow y=200$

This is useful in scientific and physical systems.

### Stability

SR is high variance:

* Small data changes can yield different expressions
* Multiple equivalent formulations may exist

Example:

* $y = 3x_1 + 2x_2$
* $y = 2.8x_1 + 2.1x_2 + 0.1x_1^2$

## Drift Analysis

Symbolic models allow structural inspection of drift.

### Structural Drift

Change in functional form:
$$
f_{t-1}(x) = 3x_1 + 0.5x_2 \rightarrow f_t(x) = 3x_1 + 0.5x_2 + \log(x_3)
$$

Indicates new relationships or variables.

### Parametric Drift

Same structure, different coefficients:
$$
f_{t-1}(x) = 3x_1 + 0.5x_2 \rightarrow f_t(x) = 2.6x_1 + 0.7x_2
$$

## Updating Strategies

Updating SR models is non-trivial:
* Global optimisation means structure may change entirely

Common approaches:
* Periodic retraining
* Warm-start using previous expressions
* Track stability across Pareto front over time
## Error Characteristics

SR explicitly trades accuracy for simplicity:

$$
\text{error} + \text{complexity}
$$

This biases toward compact, interpretable expressions rather than purely predictive models.
## Function Properties

Typical outputs are:

* Continuous
* Often differentiable
* Compact representations

Example:
$$
f(x) = x_1^2 + \sin(x_2)
$$
## Interpretability

Interpretability is intrinsic:

* Direct visibility of variable relationships
* Explicit nonlinear structure
* Clear scaling effects
## Advanced Uses

Feature Engineering: Extract sub-expressions as engineered features:

* e.g. $\sqrt{x_1^2 + x_2^2}$

Model Compression: Approximate black-box models:

* Train SR on $(X, \hat{y})$ from a complex model
* Produces an analytic surrogate

Dimensional Constraints: Enforce unit consistency in physical systems:
* Prevent invalid expressions (e.g. $m + s$)
* And limit complexity of output formulas

Invariant Discovery: Find conserved relationships by solving:
$$
f(X) \approx 0
$$
## Implementation Ecosystem

* **PySR** (state-of-the-art, Julia backend)
* **gplearn** (scikit-learn style, simpler)
## Notes

How does SR works:
* Population-based search over functions
* Operators used in symbolic regression: mutation, crossover, simplification, optimisation
* Island-based evolution can improve diversity
* Widely used in physics, control systems, and scientific modelling
## References

* PySR: [https://github.com/MilesCranmer/PySR](https://github.com/MilesCranmer/PySR)
* Cranmer et al. (2020): *Discovering Symbolic Models from Data*
* Koza (1992): *Genetic Programming*