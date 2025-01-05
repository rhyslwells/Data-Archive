# Deep Q-Learning

[[Reinforcement learning]]

Target Network?- when does this occur/when is it needed.
The target can be changed per iteration. Use soft update to change the target slowly.

Experience Relay?
What issue does this aim to resolve, give an example where this causes an issue.
When an agent interacts with the environment, the states, actions, and rewards the agent experiences are sequential by nature. 
If the agent tries to learn from these consecutive experiences it can run into problems due to the strong correlations between them. 
To avoid this, we employ a technique known as Experience Replay to generate uncorrelated experiences for training our agent. 
Experience replay consists of storing the agent's experiences (i.e the states, actions, and rewards the agent receives) in 
a memory buffer and then sampling a random mini-batch of experiences from the buffer to do the learning. The
 experience tuples $(S_t, A_t, R_t, S_{t+1})$ will be added to the memory buffer at each time step as the agent interacts with 
 the environment. By using experience replay we avoid problematic correlations, oscillations and instabilities. In addition, 
 experience replay also allows the agent to potentially use the same experience in multiple weight updates, which increases data 
 efficiency.