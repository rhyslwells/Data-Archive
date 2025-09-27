---
aliases: []
category: ML
date modified: 27-09-2025
tags:
- customer_growth
- forecasting
- growth_models
- ml
- time_series
---
Both **Logistic** and **Gompertz models** are commonly used to model **growth that saturates** over time, such as: Customer adoption, Product uptake, Population growth

They are **S-shaped (sigmoidal) curves** that capture initial exponential growth followed by slowing as a **saturation point** is approached.

- [[Logistic Model Curve]]
- [[Gompertz Model]]

Summary
- Both models are **sigmoidal growth models** suitable for customer growth or population dynamics  
- The **key difference** is symmetry vs asymmetry of growth  
- **K** (carrying capacity) is the critical parameter to define saturation  
- Early data can help estimate growth rate and K, guiding which model to choose
## Saturation Effects

- Both models incorporate a **carrying capacity (K)** that represents the maximum attainable size  
- **Saturation occurs** as growth slows when approaching K  
- Choosing K is critical: it sets the **upper bound** of your forecast  
- If K is unknown, it can be **estimated from early growth trends** or inferred from historical analogues

## Choosing Between Logistic and Gompertz

| Aspect | Logistic | Gompertz |
|--------|---------|----------|
| Curve symmetry | Symmetric | Asymmetric |
| Early growth | Faster | Slower, more gradual |
| Inflection point | At 50% of K | Before 50% of K |
| Use case | Uniform adoption | Cautious early adoption / biological growth |
| Interpretability | Simple | Slightly more flexible |

**Rule of Thumb:**  
- Pick **Logistic** if growth is roughly symmetric and you expect early acceleration.  
- Pick **Gompertz** if early growth is slow and adoption accelerates later.  

