---
tags:
  - deep_learning
category:
---
GPU support for [[Deep Learning]] operations.
## Example 
Here is the performance comparison for 1 epoch,

| Epoch | CPU | GPU  |
|:------|:------|:------|
| 1 | 43 sec | 3 sec |
| 10 | 7 min 26 sec | 30 sec |

You can see that GPU is almost 15 times faster. We ran only one epoch for benchmarking but for actual training we have to run many epochs and also when data volume is big running deep learning without GPU can consume so much time. This is the reason why GPUs are becoming popular in the field of deep learning

