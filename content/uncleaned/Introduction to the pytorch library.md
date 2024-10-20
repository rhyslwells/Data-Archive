---
title: 
tags:
  - "#question"
importance: 
engagement: 
recency_of_interest: 2024-10-05
---
# Basics of [[PyTorch]]

### Tensors arrays 

PyTorch uses tensors, which are similar to NumPy arrays, but with GPU acceleration.

```python
import torch
# Creating a tensor
x = torch.tensor([2.0, 3.0, 4.0])
# Tensor operations
y = x + 2
z = x * 3
print(y)  # Output: tensor([4., 5., 6.])
print(z)  # Output: tensor([ 6.,  9., 12.])
```

### Automatic Differentiation  
PyTorch can compute gradients automatically with `autograd`.

```python
# Create tensor with gradient tracking (input value)
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True) #`requires_grad=True`, which tells PyTorch to track all operations performed on this tensor. T

# Perform some operations
y = x ** 2 #formula
z = y.sum() #14

# Compute gradients
z.backward() #backpropagation (the chain rule of calculus). Since `z` is a scalar, PyTorch can compute the gradients of `z` with respect to each element in `x`.

# Print gradients (dy/dx)
print(x.grad)  # Output: tensor([2., 4., 6.])
```

The gradient is calculated by the chain rule:
- For $y = x^2$, the derivative of $y$ with respect to $x$ is $\frac{dy}{dx} = 2x$.
- ==Since `z` is the sum of the elements of `y`, the gradient of `z` with respect to each element in `x` is $\frac{dz}{dx_i} = 2x_i$ for each element in `x`.==

==z is a formula but calculates the derivative wrt x, so the derivative of y with x.==

So, the gradients for each element in `x` are:
$\frac{dz}{dx} = [2 \times 1.0, 2 \times 2.0, 2 \times 3.0] = [2.0, 4.0, 6.0]$

The gradients are stored in `x.grad`. After calling `z.backward()`, `x.grad` contains the derivative of `z` with respect to each element of `x`, which is `[2.0, 4.0, 6.0]`

Gradient Computation (Summary):
- The gradient $\frac{dz}{dx}$ represents how much the output `z` changes for a small change in `x`. In our case, if we slightly increase `x_1`, `x_2`, or `x_3`, the change in `z` can be predicted using these gradients.
- This gradient information is used to update weights in neural networks during training. For example, in optimization algorithms like ([[Stochastic Gradient Descent]]), these gradients are used to adjust model parameters in the direction that minimizes the loss function.
###### Confusion: total derivative is not the partial derivates

The confusion here comes from the distinction between **partial derivatives** (for each element in a tensor) and **total derivatives**. Let me clarify this.

In the context of:

```python
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = x ** 2
z = y.sum()
z.backward()
```

- `x` is a tensor: $ x = [1.0, 2.0, 3.0] $
- `y = x^2` computes element-wise squares: $ y = [1.0^2, 2.0^2, 3.0^2] = [1.0, 4.0, 9.0] $
- `z = y.sum()` adds the elements in `y`: $ z = 1.0 + 4.0 + 9.0 = 14.0 $

Now, you're asking about the derivative of `z` with respect to `x`, specifically whether **`dz/dx` should be the sum of the derivatives** and equal to 4.

**Derivative with Respect to Each Element (Partial Derivative)**

When you calculate the gradient of `z` with respect to `x`, you're computing the **partial derivatives** of `z` with respect to each element in `x`. The function `z` depends on each element of `x` individually.

For each element $x_i $ in `x`, we are calculating:

$\frac{\partial z}{\partial x_i} = \frac{\partial (x_1^2 + x_2^2 + x_3^2)}{\partial x_i} = 2x_i$

This gives:

$\frac{\partial z}{\partial x} = [2x_1, 2x_2, 2x_3] = [2 \times 1.0, 2 \times 2.0, 2 \times 3.0] = [2.0, 4.0, 6.0]$

These are the gradients stored in `x.grad` after calling `z.backward()`.

**Total Derivative vs Partial Derivatives**

If we are talking about **partial derivatives**, we get a gradient for each individual component of `x`:

- $ \frac{\partial z}{\partial x_1} = 2.0$
- $ \frac{\partial z}{\partial x_2} = 4.0$
- $ \frac{\partial z}{\partial x_3} = 6.0$

These partial derivatives form the gradient vector: `[2.0, 4.0, 6.0]`.

**Why Is It Not Just 4?**

If you're thinking of the total derivative, that would be different from what we are calculating here. **The sum of the derivatives of `z` with respect to all components of `x`** is:

$
\sum_{i=1}^{3} \frac{\partial z}{\partial x_i} = 2 + 4 + 6 = 12
$

However, this total derivative is not what we are computing here. **We are computing the partial derivatives for each element of `x` separately**, which results in the gradient vector `[2.0, 4.0, 6.0]`.

In Summary:
- **Gradient (`x.grad`)**: A vector of partial derivatives of `z` with respect to each element in `x`, giving us `[2.0, 4.0, 6.0]`.
- **Sum of Gradients**: The sum of the elements of the gradient vector is `12`, but that’s not the gradient of `z` with respect to `x` as a whole—it's just a summation of the partial derivatives.
### Basic [[Neural network|Neural Network]] Implementation 

A simple feedforward network using PyTorch.

```python
import torch
import torch.nn as nn

# Define a simple neural network
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc = nn.Linear(2, 1)

    def forward(self, x):
    #- **`forward()` method**: This defines the forward pass, i.e., how the input data is transformed as it moves through the network. In this case, the input `x` is passed through the linear layer.
        return self.fc(x)

# Create the network
net = SimpleNet()

# Create input tensor
x = torch.tensor([[1.0, 2.0]])

# Forward pass
output = net(x)

print(output)  # Output: a tensor from the linear layer
```

**Input Tensor and Forward Pass**
```python
x = torch.tensor([[1.0, 2.0]])
output = net(x)
```
- **`torch.tensor([[1.0, 2.0]])`**: This defines a 2D input tensor with two features, which corresponds to the two input nodes in the network.
- **`net(x)`**: This performs a **forward pass**, feeding the input tensor `x` into the network. The linear layer applies the learned weights and bias to compute the output.

**Output**
The output of the network is a tensor from the linear layer, which corresponds to the result of the operation $y = w_1 \cdot x_1 + w_2 \cdot x_2 + b$, where:
- $w_1$ and $w_2$ are the learned weights for each input feature.
- $b$ is the learned bias.

[[Use Cases for a Simple Neural Network Like]]

### Training a Simple Model  
An example of training a linear model with

- [[Gradient Descent]]:
- [[Loss function]]: [[Ordinary Least Squares]]
- [[Stochastic Gradient Descent|SGD]]:

Training of [[Linear Regression]] model. This model find best w,b in $y=wx+b$.

```python
import torch
import torch.optim as optim

# Data
x = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = torch.tensor([[2.0], [4.0], [6.0], [8.0]])

# Model
model = nn.Linear(1, 1) #**`nn.Linear(1, 1)`** defines a simple linear model with **one input feature** and **one output**. This model has two parameters:

# Loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01) # stochastic gradient descent

# Training loop
for epoch in range(100):
    # Forward pass #- **Forward pass**: For each epoch, the model makes predictions (`y_pred`) by passing the input `x` through the linear model.
    y_pred = model(x)
    loss = criterion(y_pred, y)# - **Loss calculation**: The loss is computed by comparing `y_pred` with the true values `y` using the MSE loss function.

    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward() #- **Backward pass**: The gradients of the loss with respect to the model’s parameters are computed using `loss.backward()`. This step calculates how much each parameter needs to be adjusted to reduce the loss.
    optimizer.step() #- **Optimization step**: The optimizer (`SGD`) updates the model’s parameters (`w` and `b`) based on the computed gradients.

    if epoch % 20 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item()}')

# Output the trained model's parameters
print(list(model.parameters()))
```

### Moving Tensors to GPU  

Summary:
- speed up training e.g. of [[Neural network|Neural Network]]
- use [[Parallelism]] for simultaneous calculations
- GPU can do larger batches of computations, better on the memory, better for [[Gradient Descent]] estimations
- 

PyTorch makes it easy to move computations to a GPU.

```python
# Check for GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Create a tensor and move it to the GPU
x = torch.tensor([1.0, 2.0, 3.0]).to(device)

print(x)  # Output: tensor([1., 2., 3.], device='cuda:0') (if GPU is available)
```

Both the **model** and the **data** are moved to the GPU (`device='cuda'`). All computations, including the forward pass, loss calculation, backward pass, and optimizer step, happen on the GPU.

```python
import torch
import torch.nn as nn
import torch.optim as optim

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define a simple neural network
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = x.view(-1, 28 * 28)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Initialize the model, loss function, and optimizer
model = SimpleNN().to(device)  # Move model to GPU
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Dummy input data and labels (move them to GPU)
inputs = torch.randn(64, 1, 28, 28).to(device)  # 64 images of 28x28 pixels
labels = torch.randint(0, 10, (64,)).to(device)  # Random labels for 64 images

# Forward pass (computation happens on the GPU)
outputs = model(inputs)
loss = criterion(outputs, labels)

# Backward pass and optimization
optimizer.zero_grad()
loss.backward()  # Compute gradients on the GPU
optimizer.step()  # Update model weights

print("Training step completed on:", device)
```