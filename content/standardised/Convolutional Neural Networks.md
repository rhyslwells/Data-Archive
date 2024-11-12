---
title: 
tags: 
aliases: 
category: CNN
---
Convolutional networks, or CNNs, are specialized [[Deep Learning]] architectures designed for processing data with grid-like structures, such as images. 

They use convolutional layers with learnable filters to extract spatial features from the input data. The convolutional operation involves sliding these filters across the input, performing element-wise multiplications and summations to create feature maps. 

CNNs are particularly effective for image classification, object detection, and image segmentation tasks.

Pooling:

The idea of pooling in convolutional neural networks is to do two things:
- Reduce the number of parameters in your network (pooling is also called “down-sampling” for this reason)
- To make feature detection ([[Feature Extraction]]) more robust by making it more impervious to scale and orientation changes
- shrink multiple data to single points.

![[Pasted image 20241006124829.png|500]]

![[Pasted image 20241006124735.png|500]]
