---
aliases: []
category:
date modified: 27-07-2025
tags: []
---

An epoch in machine learning is a single pass through the entire training dataset. The number of epochs, denoted as $N$, determines how many times the data is applied to the model.

Why Use Multiple Epochs?
- **Repetition for Learning:** The data is applied to the model $N$ times to improve learning and accuracy. For example, if $N = 10$, the model will see the entire dataset 10 times.

Example
```
Epoch 1/10
6250/6250 [==============================] - 6s 910us/step - loss: 0.1782
```

- **Epoch 1/10:** Indicates the model is currently on the first epoch out of a total of 10.
- **Batches:** For efficiency, the dataset is divided into smaller groups called 'batches'. In TensorFlow, the default batch size is 32. With 200,000 examples, this results in 6,250 batches.
- **Batch Execution:** The notation `6250/6250` shows the progress of batch execution within the current epoch.

