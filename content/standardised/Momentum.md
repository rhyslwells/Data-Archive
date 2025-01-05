Momentum is an optimization technique used to accelerate the [[Gradient Descent]] algorithm by incorporating the concept of inertia. It helps in reducing oscillations and speeding up convergence, especially in scenarios where the [[cost function]] has a complex landscape.
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

[[Momentum]]

### 1. Momentum in Gradient Descent:

Momentum is a technique that helps accelerate gradient descent by adding a fraction of the previous update to the current update. It helps smooth out oscillations and can lead to faster convergence. Momentum is typically controlled by a hyperparameter $\beta$ (often close to 1).

#### Steps to Implement Momentum:

- Formula: vt+1=βvt+(1−β)∇θJ(θ)v_{t+1} = \beta v_t + (1 - \beta) \nabla_{\theta} J(\theta)vt+1​=βvt​+(1−β)∇θ​J(θ) θt+1=θt−αvt+1\theta_{t+1} = \theta_t - \alpha v_{t+1}θt+1​=θt​−αvt+1​ Where:
    - $v_t$ is the velocity (the accumulated gradient).
    - $\beta$ is the momentum factor (commonly set to 0.9 or 0.99).
    - $\nabla_{\theta} J(\theta)$ is the gradient of the cost function with respect to the parameters $\theta$.
    - $\alpha$ is the learning rate.

#### To explore it:

- Implement momentum in your custom gradient descent function.
- Experiment with different values of $\beta$ (e.g., 0.9, 0.99) and observe the changes in the convergence speed.
- Compare the results with standard gradient descent by plotting the cost function over iterations.