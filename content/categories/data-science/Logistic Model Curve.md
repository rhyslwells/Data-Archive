---
aliases: []
category: DS
date modified: 27-09-2025
tags: []
---
## Logistic Model Curve

**Equation:**  

$$
y(t) = \frac{K}{1 + e^{-r(t-t_0)}}
$$

- **K:** Carrying capacity (maximum possible value)  
- **r:** Growth rate  
- **$t_0$:** Inflection point (time at which growth is fastest)

**Characteristics:**

- Symmetric S-curve around the inflection point  
- Growth slows as it approaches K due to saturation  
- Easy to interpret: **K directly gives maximum potential size**

**Use Cases:**

- When saturation is **symmetric** around the midpoint  
- Customer adoption where growth initially accelerates, then decelerates evenly

Related:
- [[Customer Growth Modeling]]