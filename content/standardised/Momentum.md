Momentum is an [[Model Optimisation|Optimisation]]  technique used to accelerate the [[Gradient Descent]] algorithm by incorporating the concept of inertia. It helps in reducing oscillations and speeding up convergence, especially in scenarios where the [[cost function]] has a complex landscape (surface). Momentum helps in dampening oscillations and achieving faster convergence. Momentum is a technique that helps accelerate gradient descent by adding a fraction of the previous update to the current update. Formula:
  $$
  v_{t+1} = \beta v_t + (1 - \beta) \nabla_{\theta} J(\theta)
  $$
  $$
  \theta_{t+1} = \theta_t - \alpha v_{t+1}
  $$
  Where:
  - $v_t$ is the velocity (the accumulated gradient).
  - $\beta$ is the momentum factor.
  - $\nabla_{\theta} J(\theta)$ is the gradient of the cost function with respect to the parameters $\theta$.
  - $\alpha$ is the learning rate.

In [[ML_Tools]] see: [[Momentum.py]]
## Key Features of Momentum

**Inertia Effect:** Momentum uses the past gradients to smooth out the updates, which helps in navigating the parameter space more effectively.

**Parameter Update Rule:** The update rule for momentum involves maintaining a velocity vector that accumulates the gradients. The parameters are then updated using this velocity, which is a combination of the current gradient and the previous velocity.

[[Hyperparameter]]
  - **[[Learning Rate]] ($\alpha$):** Controls the size of the steps taken towards the minimum.
  - **Momentum Coefficient ($\beta$):** Determines the contribution of the previous gradients to the current update. A typical value is 0.9.


