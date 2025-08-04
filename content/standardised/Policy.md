---
aliases: [policies]
category: DS
date modified: 1-08-2025
tags: ["#question", question]
---
In [[reinforcement learning]] (RL), a **policy** is a strategy or a rule that defines the actions an agent takes in a given state to achieve its goals. It essentially ==maps states of the environment to actions that the agent should take when in those states.==

Policies are used in RL as they determine the behavior of the agent. 

The goal of many RL algorithms is to find an optimal policy that maximizes the cumulative reward the agent receives over time. This involves balancing exploration (trying new actions) and exploitation (using known actions that yield high rewards).

### Key Concepts

**On-Policy vs. Off-Policy**:
  - **On-Policy**: The agent learns the value of the policy it is currently following. An example is the [[SARSA]] algorithm, which updates its policy based on the actual actions taken by the agent.
  - **Off-Policy**: The agent learns the value of the optimal policy, regardless of the actions it actually takes. [[Q-Learning]] is an example of an off-policy algorithm, as it updates its policy based on the best possible action in the next state, not necessarily the action taken.

**Conservatism**:
  - Some policies, like those in SARSA, are more conservative in their updates. This means they are more cautious and adapt to uncertainties in the environment, making them suitable for environments where [[Agent Exploration]] and [[exploitation]] need to be balanced carefully.

### Example of a Policy

Consider a simple grid world where an agent can move up, down, left, or right to reach a goal. A policy in this context could be a set of rules that tells the agent to always move towards the goal if it is visible, or to explore randomly if the goal is not visible.

For instance, in a 3x3 grid where the goal is at position (2, 2), a simple policy might be:

- If the agent is at (0, 0), move right.
- If the agent is at (0, 1), move right.
- If the agent is at (0, 2), move down.
- Continue this pattern until the agent reaches the goal at (2, 2).

This policy can be represented as a table or a function that maps each state (grid position) to an action (move direction).

|State (Position)|Action|
|---|---|
|(0, 0)|Move Right|
|(0, 1)|Move Right|
|(0, 2)|Move Down|
|(1, 0)|Move Right|
|(1, 1)|Move Right|
|(1, 2)|Move Down|
|(2, 0)|Move Right|
|(2, 1)|Move Right|
|(2, 2)|Goal Reached|
