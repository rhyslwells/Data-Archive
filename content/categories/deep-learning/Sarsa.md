---
aliases: []
category: DL
date modified: 27-09-2025
tags:
- deep_learning
---
SARSA stands for State-Action-Reward-State-Action

SARSA is another value-based [[Reinforcement learning]] algorithm, differing from Q-learning in that it updates the Q-values based on the action actually taken by the policy.

**SARSA update rule:**

$$
Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ r_{t+1} + \gamma Q(s_{t+1}, a_{t+1}) - Q(s_t, a_t) \right]
$$

**Explanation:**

- **$Q(s_t, a_t)$**: The Q-value of the current state $s_t$ and action $a_t$.
- **$\alpha$**: The learning rate, determining how much new information overrides old information.
- **$r_{t+1}$**: The reward received after taking action $a_t$ from state $s_t$.
- **$\gamma$**: The discount factor, balancing immediate and future rewards.
- **$Q(s_{t+1}, a_{t+1})$**: The Q-value for the next state $s_{t+1}$ and the action $a_{t+1}$ actually taken according to the policy.

**Notes**:

- SARSA’s on-policy nature ensures that it learns a policy that aligns with its exploration strategy, leading to more stable behavior in environments with randomness or noise.
- The learning process may be slower compared to Q-learning, but it can be more robust in environments where the agent’s behavior is expected to align closely with the policy it follows.
