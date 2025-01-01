Momentum is an optimization technique used to accelerate the [[gradient descent]] algorithm by incorporating the concept of inertia. It helps in reducing oscillations and speeding up convergence, especially in scenarios where the [[cost function]] has a complex landscape.
#### Key Features of Momentum:

- **Inertia Effect:** Momentum uses the past gradients to smooth out the updates, which helps in navigating the parameter space more effectively. This is akin to a ball rolling down a hill, where the momentum helps it move faster and overcome small obstacles.
  
- **Parameter Update Rule:** The update rule for momentum involves maintaining a velocity vector that accumulates the gradients. The parameters are then updated using this velocity, which is a combination of the current gradient and the previous velocity.

- [[Hyperparameter]]
  - **[[Learning Rate]] (\(\alpha\)):** Controls the size of the steps taken towards the minimum.
  - **Momentum Coefficient (\(\beta\)):** Determines the contribution of the previous gradients to the current update. A typical value is 0.9.

- **Implementation Challenges:**
  - **Parameter Initialization:** Proper initialization of parameters is crucial to avoid poor convergence.
  - **Learning Rate Tuning:** Starting with a small learning rate and adjusting as necessary can help achieve optimal results.
  - **Early Stopping:** Using early stopping can prevent [[overfitting]] and unnecessary computations.

Momentum is particularly useful in scenarios where the cost function has ravines or elongated curvatures, as it helps in dampening oscillations and achieving faster convergence.

