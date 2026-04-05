---
aliases: []
category: ML
date modified: 25-03-2026
tags:
  - explainability
---
[[Interpretability]] is indirect due to the hundreds of underlying trees that prevent direct inspection. Common interpretation tools include:
- [[Feature importance]]
- [[SHapley Additive exPlanations|SHAP]] values
- [[Partial Dependence Plot]]
## Model Properties

**Low [[Variance]] Model**: Random forests achieve low variance through averaging, making predictions stable when data slightly changes. This property makes them common for production pipelines.
## Extrapolation Limitations

Random forests cannot extrapolate outside the training range. Predictions become the average value in the nearest region.

**Example**: 
- Training data: $x \in [0,10]$
- Prediction at $x=20$ typically returns values close to the maximum training region
## Function Approximation

Random forests approximate functions through local partitioning of feature space, creating piecewise regions:

$$f(x) = \begin{cases} 3.2 & x_1 < 1.2 \\ 4.7 & x_1 \ge 1.2 \end{cases}$$

The forest smooths discontinuities through averaging.
## Training Procedure

Random forests follow a deterministic training procedure:
1. Draw bootstrap samples
2. Grow decision trees
3. At each split, choose a random subset of features
4. Optimize each split with: $\min \text{MSE}$

No search over mathematical forms occurs.

## Symbolic Approximation via Model Distillation

### Why Approximate with [[Symbolic Regression]]

Random forests provide strong predictive accuracy and [[Generalisation|robustness]] to noise. [[Symbolic Regression]] provides interpretable functional structure and compact mathematical representation. Combining them produces a high-accuracy model with a simplified analytical description.

### Distillation Pipeline

**Step 1** — Train the random forest:
$$f_{RF}(x)$$

**Step 2** (why do this step?) — Generate synthetic training data:
Sample inputs from the feature space: $X^* = \{x_1^*, x_2^*, ..., x_m^*\}$

Compute labels using the forest: $y_i^* = f_{RF}(x_i^*)$

New dataset: $D^* = (X^*, y^*)$ ==represents the response surface learned by the forest==.

**Step 3** — Run symbolic regression:
Train symbolic regression on $(X^*, y^*)$ to obtain:
$$f_{SR}(x) \approx f_{RF}(x)$$

### Benefits of Distillation

- ==**Model compression**==: A forest with hundreds of trees becomes a single formula
  - Example: [[Random forest]] (500 trees) → Symbolic formula (8 terms)
- **Interpretability**: Exposes relationships such as polynomial growth, logarithmic scaling, interaction terms
- **Analytical manipulation**: Compute derivatives $\frac{\partial y}{\partial x_i}$, integrals, asymptotic behaviour

### Limitations

- **Approximation error**: Symbolic regression cannot always perfectly reproduce the forest surface; complex forests may require large formulas
- **Feature interactions**: Forests can capture extremely complex interaction boundaries that symbolic regression may simplify
- **Stability**: Symbolic approximations may vary depending on sampling strategy and search randomness
## Comparing Symbolic Formula to Forest Predictions

### Prediction Agreement

The most direct comparison measures [[Model Evaluation by Prediction Difference]]:

$$MSE = \frac{1}{n}\sum (y_{RF} - y_{SR})^2$$
$$MAE = \frac{1}{n}\sum |y_{RF} - y_{SR}|$$

These measure how closely the symbolic formula reproduces the forest.

### Functional Similarity

Functional distance between models:
$$\Delta = \mathbb{E}_x[|f_{RF}(x) - f_{SR}(x)|]$$

Small $\Delta$ indicates the symbolic model is a good surrogate.

### Behavioural Diagnostics

- **Partial dependence comparison**: Compare $PD_{RF}(x_j)$ vs $PD_{SR}(x_j)$ to verify the symbolic formula reproduces the same trend for individual features
- **Interaction analysis**: Verify that complex interactions like $x_1 \times x_2$ captured by the forest are approximated in the symbolic formula

### Out-of-Sample [[Validation]]

Evaluate both models on validation data:

| Model | $R^2$ |
|-------|-------|
| Random forest | 0.92 |
| Symbolic regression | 0.84 |

The symbolic model typically sacrifices some predictive accuracy for interpretability.

### Complexity Comparison

Compare model sizes:
- Random forest: 400 trees, depth ≈ 10, ~10000 decision nodes
- Symbolic formula: $y = 2.1x_1 + 0.3x_2^2 - 0.8\log(x_3)$

Symbolic models are dramatically smaller.

### [[Residuals Analysis]]

Evaluate residuals: $r(x) = f_{RF}(x) - f_{SR}(x)$

Typical pattern: symbolic model captures global trend, forest captures local irregularities.