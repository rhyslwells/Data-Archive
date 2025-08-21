---
aliases: []
category: 
date modified: 1-08-2025
tags:
  - "#optimisation"
  - process
type:
---
Its the term given to the iterative process of building good features for a better model. Its the process that makes relevant features (using formulas and relations between others). 
 
We use it when we have a refined and optimised model.

What does it involve
- Create new features from existing ones (e.g., ratios, interactions).
- Transform features to better capture non-linear relationships.
- [[Dimensionality Reduction]] if necessary.

The main techniques of feature engineering:
- are selection (picking subset), 
- learning (picking the best), 
- extraction and combination(combining).

Example:
Predicting house prices. Raw features might be square footage, number of bedrooms, and location. Feature engineering could involve: Combining square footage and bedrooms into a "living space" feature.

**Example**:
- Decompose datetime information into separate features for date and time to capture their respective predictive powers.


![[C1_W2_Lab07_FeatureEngLecture.png]]

Interaction terms: [[Feature Engineering]]:
- Definition and Purpose: Interaction terms are new features created by combining existing ones to capture the interaction effects between them, improving model ==accuracy==.
- Common Methods: Multiplication (e.g., square footage * number of bedrooms) and division (e.g., price per square foot) are common ways to create interaction terms.
- Benefits: They help uncover ==complex patterns, tackle non-linearities==, and enhance the model's ability to learn how features influence each other.
- Application: Use domain knowledge to identify meaningful interactions and start with simple, pairwise interactions to avoid overfitting.