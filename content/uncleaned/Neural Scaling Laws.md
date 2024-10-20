---
media_link: https://www.youtube.com/watch?v=5eqRuVp65eY
tags:
  - drafting
---
Even scaled model cannot cross tthe [[compute efficent frontier]]

![[Pasted image 20241017072233.png|500]]

[[validation loss]]

Neural scaling laws. That is error rates scale with compute,model size and dataset size, independant of model aritechture. Can we drive to 0?
 
Same laws apear in video and image models.

LLMs are auto progressive models.

Theorical results guiding experiemental - saving compute time.

#### How [[LLM|LLMs]] work

![[Pasted image 20241017072732.png|500]]

During training we know next value, hence we have a [[Loss function]] to help learning.

L1 - loss functions

[[Cross entropy]]-loss function (uses negative log of probability).  Why is cross enropy used over L1?

unabigious next words. [[Entropy of natural language]] due to this will LLMs cannot drive [[Cross entropy loss]] to zero.

### Manifolds?

Example [[MNIST]] data set images of number, has high dimesnional dataset space.

![[Pasted image 20241017073743.png|500]]

[16:03](https://www.youtube.com/watch?t=963&v=5eqRuVp65eY)
Simlar concepts group together.

density of manifold 
average distance between point. or size of neightbourhoods s

![[Pasted image 20241017074030.png|500]]

$S=L D^{-1/d}$

### Manifold hypothesis (data points in high dim space) and scaling laws 

Knowing the manifold will help scaling. This is called

[[Resolution limited scaling]]

$$LOSS < D^{-4/d}$$

[[Cross entropy loss]] should scale wrt manifold.

[19:24](https://www.youtube.com/watch?t=1164&v=5eqRuVp65eY)

[[intrinsic dimension of natural language]]








