---
aliases: []
category: 
date modified: 27-07-2025
tags: []
---
[[Kernelling]] is a technique where the [[Support Vector Machines|SVM]] uses a kernel function to map the dataset into a higher-dimensional space, making it easier to identify separable clusters that may not be apparent in the original low-dimensional space.

 Kernel Trick:
   - When the data cannot be separated by a straight line or plane in its original (low-dimensional) space, SVM uses a technique called kernelling to project the data into a higher dimension where it becomes easier to separate.
   - The Kernel Trick allows the transformation of data into a higher dimension without explicitly computing the transformation. There are different types of kernels, with common examples being:
     - Polynomial kernel
     - Radial Basis Function (RBF) or exponential kernel

