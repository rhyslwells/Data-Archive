---
aliases: 
category: 
date modified: 27-07-2025
tags:
  - explainability
  - ml
---
[link](https://www.youtube.com/watch?v=UEtvV1D6B3s&list=PLkDaE6sCZn6E7jZ9sN_xHwSHOdjUxUW_b&index=2)

When training ML model need Orthogonalization in order to Determine what to tune, and observe the effect it has.

Each button does one thing.

Example: Car with Accelerator and angle of steering wheel. 

Assumptions (controls for tuning):
- model works well with cost functions
	- Try [[Adam Optimizer]], bigger network
- work on training set
	- [[Regularisation]]
	- Try bigger training set
- works on test set of data
	- Try bigger training set.
- works well in real life.
	- Change training set
	- Change cost function.

Avoid early stopping as effects network size, and training set size.

Related links:
- [[Optimising Neural Networks]]
- [[DS & ML Portal]]