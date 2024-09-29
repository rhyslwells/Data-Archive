Reinforcement Learning (RL) is a type of machine learning where an agent interacts with an environment and learns to make decisions that maximize cumulative rewards. The key components of an RL system include:

- **Agent**: An entity that interacts with the environment and learns to optimize its actions based on rewards. In the hunter-prey project, both the hunter and prey act as agents.
- **Environment**: The setting in which the agents operate. In the hunter-prey project, this is a 2D grid where agents interact.
- **State ($s$)**: The current situation in the environment, often defined by the positions and attributes relevant to the agent's decision-making.
- **Action ($a$)**: The available moves or decisions an agent can take.
- **Reward ($r$)**: A scalar value received after taking an action, representing feedback from the environment.
- **[[Policy]] ($\pi$)**: A strategy that the agent follows, mapping states to actions.
- **Q-Value ($Q(s, a)$)**: The expected cumulative reward for taking a particular action in a given state and following the policy thereafter. The Q-values guide the agent in making decisions that maximize long-term rewards.
- **Markov Decision Process (MDP)**: A formal framework for decision-making where outcomes depend solely on the current state (Markov property).

## Exploration vs. Exploitation

One of the major challenges in reinforcement learning is balancing exploration (trying new actions) and exploitation (choosing the best-known actions). The epsilon-greedy strategy is commonly used, where a small probability (epsilon) allows for exploration while primarily exploiting the best-known actions.

[[Core Algorithms in Reinforcement Learning]]