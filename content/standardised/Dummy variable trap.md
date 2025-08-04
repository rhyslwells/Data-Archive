---
aliases: 
category: 
date modified: 27-07-2025
tags:
  - ml
  - modeling
  - preprocessing
---
### Key Takeaways:

- The dummy variable trap occurs due to [[multicollinearity]], where ==one dummy variable can be perfectly predicted from others.==
- Dropping one dummy variable avoids this issue and ensures that the model has a reference category against which the other categories are compared.
- This approach leads to a well-conditioned model and allows for more interpretable regression coefficients.
### Dummy Variable Trap

The dummy variable trap refers to a scenario in which there is multicollinearity in your dataset when you create dummy variables for categorical features. Specifically, it occurs when one of the dummy variables in a set of dummy variables can be perfectly predicted by a linear combination of the others.

This situation arises when you create dummy variables for a categorical feature with $n$ categories, leading to $n$ binary columns. However, if you include all $n$ dummy variables in your regression model, ==the model will face redundancy because knowing the values of $n-1$ dummy variables will already give you the value of the last one (since all the categories must add up to 1 for each observation)==. This results in perfect multicollinearity.

### Why Do We Need to Drop One of the Dummy Variables?

In a regression model, multicollinearity can cause problems because it makes the estimation of coefficients unstable, leading to unreliable statistical inferences. Specifically, the model can't determine which of the correlated variables is truly responsible for explaining the variation in the target variable.
### Example:

Suppose you have a categorical feature `town` with three categories: `West Windsor`, `Robbinsville`, and `Princeton`. When you apply [[one-hot encoding]], you create three dummy variables:

|town|West Windsor|Robbinsville|Princeton|
|---|---|---|---|
|West Windsor|1|0|0|
|Robbinsville|0|1|0|
|Princeton|0|0|1|

Now, if you include all three dummy variables in a linear regression model, the columns `West Windsor`, `Robbinsville`, and `Princeton` will be perfectly correlated. For example, if the values of `West Windsor` and `Robbinsville` are both 0, then `Princeton` must be 1, and vice versa.

This creates multicollinearity because you can predict one dummy variable perfectly by knowing the others. Hence, you need to drop one of the dummy variables—usually, you drop one category, which becomes the reference group.

If you drop the `West Windsor` dummy column, your table would look like this:

|town|Robbinsville|Princeton|
|---|---|---|
|West Windsor|0|0|
|Robbinsville|1|0|
|Princeton|0|1|

Now, your model will use the `West Windsor` category as the baseline. The coefficients of `Robbinsville` and `Princeton` in the regression model will indicate how much higher or lower their prices are compared to `West Windsor`.