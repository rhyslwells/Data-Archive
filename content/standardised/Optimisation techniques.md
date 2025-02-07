Optimisation techniques
- [[Adam Optimizer]]
- RMSprop
- [[Stochastic Gradient Descent]]
- [[standardised/Optuna]]

[[Gradient Descent]]
- Iteratively updates parameters using the gradient of the [[Cost Function]] with respect to the parameters.  
- Requires careful tuning of the [[Learning Rate]] ($\alpha$), which controls the size of each update.  

Optimization Solvers in [[Sklearn]] : Scikit-learn solvers improve on Gradient Descent by leveraging advanced techniques:  
- Use second-order information, such as approximations to the Hessian matrix.  
- Achieve faster and more reliable convergence compared to Gradient Descent.  
- Automatically adapt step sizes [[Adaptive Learning Rates]], eliminating the need for manual tuning.

