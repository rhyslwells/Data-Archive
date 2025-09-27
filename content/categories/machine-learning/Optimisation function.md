---
aliases: []
category: ML
date modified: 27-09-2025
tags:
- optimisation
- selection
---
Optimization functions adjust the [[Model Parameters]] to minimize the [[Loss function]], which measures how well the model performs. This is a fundamental step in training machine learning models.  

General Optimization Process:

The [[Optimisation function]] (e.g., LBFGS, Newton-CG) iteratively updates the [[Model Parameters]] by:  
1. Calculating the gradient of the loss function with respect to the parameters.  
2. Updating the parameters in the direction of the negative gradient (as described in [[Gradient Descent]]).  

This process is repeated until:  
- The cost function converges (i.e., the change in the loss function becomes negligible), or  
- The maximum number of iterations is reached.  

See [[Optimisation techniques]].