---
title: 
tags:
  - ml
  - classifer
aliases:
  - SVM
category:
---

"Optimal fat hyperplanes"
![[Pasted image 20240128193726.png|500]]

Soft margins are a measure of how the borders mix, softer more mixing

![[Pasted image 20240128193838.png|500]]

Allows for miscalculations ([[outliers]]) allowing bias/variance tradeoff.

Soft margins are observations at the edges of data clusters.

## Q&A's

SVM are a generalisation of;; support vector classifiers (SVC), which place a hyperplane between datasets.

To get to higher dimension use a {{[[kernel classifier function]]}} using a Kernel Trick. Two types are {{Polynomial and Radial (exponential)}}.
<!--SR:!2000-01-01,1,250!2024-04-08,4,270-->

SVM are used over SVC when there is;; no clear linear way to split the data.

How SVM work:
?
1) Starts in low dimension
2) Moves to a higher dimension
3) Places thresholds (hyperplanes) to divide groups of data using SVC.

Support Vector Machines
(SVMs): SVMs find the optimal hyperplane that separates examples from different classes.

**What is a Support Vector Machine, and what is its main idea?**;; SVM is a supervised machine learning algorithm that aims to find high-dimensional planes dividing a dataset into clusters. It does so by maximizing the margin between classes, with support vectors being the points closest to the planes.

**What is the technique called kernelling that is used by Support Vector Machine?**;; SVM uses a kernelling to map the dataset into a higher dimension, making it easier to identify clusters that may not be apparent in lower dimensions.
<!--SR:!2024-04-08,4,270-->

**What is a Support Vector Machine particularly advantages and disadvantages?**;; SVM is good at classifying high-dimensional data with many features and disadvantages such as poor performance with large datasets due to computational costs and the need to carefully choose the kernel.