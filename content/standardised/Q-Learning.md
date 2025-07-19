---
tags:
  - regressor
  - ml_process
aliases: 
category: ML
phase: Model Building
topic: Q-Learning
filename: q_learning_algorithm
---
Q-learning is a value-based, model-free [[Reinforcement learning]] algorithm where the agent learns the optimal [[policy]] by updating Q-values based on the rewards received. It is particularly useful in discrete environments like grids.

Uses a Q-Table which is populated by Q-values which are the maximum expected future reward for the given state and action. We improve the Q-Table in an iterative approach

Resources:
- [Q-Learning Explained - Reinforcement Learning Tutorial](https://www.youtube.com/watch?v=kEGAMppyWkQ&list=PLcWfeUsAys2my8yUlOa6jEWB1-QbkNSUl&index=9)

**Q-learning update rule:**

The left hand side gets updated ([[Bellman Equations]])
$$
Q_{new}(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ r_{t+1} + \gamma \max_{a'} Q(s_{t+1}, a') - Q(s_t, a_t) \right]
$$

**Explanation:**

- **$Q(s_t, a_t)$**: The Q-value of the current state $s_t$ and action $a_t$.
- **$\alpha$**: The learning rate, determining how much new information overrides old information.
- **$r_{t+1}$**: The reward received after taking action $a_t$ from state $s_t$.
- **$\gamma$**: The discount factor, balancing immediate and future rewards.
- **$\max_{a'} Q(s_{t+1}, a')$**: The maximum Q-value for the next state $s_{t+1}$ across all possible actions $a'$.

![[Pasted image 20250220133556.png]]

**Notes**:

- Q-learning is well-suited for environments where the state and action spaces are discrete and manageable in size.
- The algorithm is designed to converge to the optimal policy, even in non-deterministic environments, as long as each state-action pair is sufficiently explored.
- [[Exploration vs. Exploitation]]

