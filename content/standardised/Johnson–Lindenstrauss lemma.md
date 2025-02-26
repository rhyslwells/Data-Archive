## Johnson–Lindenstrauss lemma

#math 

https://youtu.be/9-Jl0dxWQs8?list=PLZx_FHIHR8AwKD9csfl6Sl_pgCXX19eer&t=1125

THe number of vectors that can be fit into a spaces grows exponentially.

Useful for [[LLM]] in storing ideas. 

Plotting M>N almost orthogonal vectors in N-dim space

Optimisation process that nudges then towards being perpendicular between 89-91 degrees

```python
import torch
import matplotlib.pyplot as plt
from tqdm import tqdm

# List of vectors in some dimension, with many
# more vectors than there are dimensions
num_vectors = 10000
vector_len = 100
big_matrix = torch.randn(num_vectors, vector_len)
big_matrix /= big_matrix.norm(p=2, dim=1, keepdim=True)
big_matrix.requires_grad_(True)

# Set up an optimization loop to create nearly-perpendicular vectors
optimizer = torch.optim.Adam([big_matrix], lr=0.01)
num_steps = 250

losses = []

dot_diff_cutoff = 0.01
big_id = torch.eye(num_vectors, num_vectors)

for step_num in tqdm(range(num_steps)):
    optimizer.zero_grad()

    dot_products = big_matrix @ big_matrix.T
    # Punish deviation from orthogonality
    diff = dot_products - big_id
    loss = (diff.abs() - dot_diff_cutoff).relu().sum()

    # Extra incentive to keep rows normalized
    loss += num_vectors * diff.diag().pow(2).sum()

    loss.backward()
    optimizer.step()
    losses.append(loss.item())

# Plot loss curve
plt.plot(losses)
plt.grid(True)
plt.show()

# Compute angle distribution
dot_products = big_matrix @ big_matrix.T
norms = torch.sqrt(torch.diag(dot_products))
normed_dot_products = dot_products / torch.outer(norms, norms)
angles_degrees = torch.rad2deg(torch.acos(normed_dot_products.detach()))

# Use this to ignore self-orthogonality
self_orthogonality_mask = ~(torch.eye(num_vectors, num_vectors).bool())
plt.hist(angles_degrees[self_orthogonality_mask].numpy().ravel(), bins=1000, range=(0, 180))
plt.grid(True)
plt.show()

```