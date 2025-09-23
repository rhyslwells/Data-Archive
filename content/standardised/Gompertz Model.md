---
aliases: []
category:
date modified: 22-09-2025
tags: []
---
## Gompertz Model

**Equation:**  

$$
y(t) = K \cdot e^{-e^{-g(t-t_0)}}
$$

- **K:** Saturation level  
- **g:** Growth rate coefficient  
- **$t_0$:** Timing parameter (controls where curve inflects)

**Characteristics:**

- Asymmetric S-curve: **slow start, fast middle growth, then gradual approach to K**  
- Often fits biological or human adoption data better than logistic  
- Early growth is slower, late growth is smoother

**Use Cases:**

- When growth starts slowly and accelerates later  
- Customer adoption with cautious early adopters and gradual ramp-up

Related:
- [[Customer Growth Modeling]]