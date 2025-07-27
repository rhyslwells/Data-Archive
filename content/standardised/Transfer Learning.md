---
aliases: []
category:
date modified: 27-07-2025
tags: [model_algorithm]
title: 
---
Transfer learning is a technique in machine learning that ==leverages knowledge gained from one setting (source domain) to improve performance on a different but related setting (target domain).== 

The core idea is to train a model on a large dataset in the source domain, learning rich feature representations that capture general patterns and relationships in the data.== These learned representations can then be transferred to the target domain, where they can be fine-tuned with a smaller dataset to achieve good performance on the target task.

Transfer learning makes sense when:
- It makes sense to do when there is lots of examples for basic layers and training, and there are few of the specialised data set.
- Task A and B have the same input x.
- You have a lot more data for Task A than Task B.
- Low level features from A could be helpful for learning B.
- When labelled data is scarce.

We can use pretrained models (i.e. from [[Hugging Face]], [[Keras]] applications, [[PyTorch]] pretrained models, model zoo).

Examples of Transfer Learning
- **Image Recognition:** A model trained on a large dataset of labelled images (e.g., ImageNet) can learn features like edges, shapes, and textures that are useful for recognising a wide variety of objects. These features can then be transferred to a different image recognition task with a smaller dataset, such as classifying medical images or identifying different species of plants.
	- Pretraining - training on image recognition. Fine-training - retraining on radiology. 
	  
- **Natural Language Processing:** A language model trained on a massive text corpus can learn word embeddings that capture semantic relationships between words. These embeddings can then be transferred to tasks like sentiment analysis or machine translation, where they can improve performance, even with limited labelled data in the target language.

Types of Transfer Learning
- **Unsupervised Pretraining for [[Supervised Learning]]:** The sources describe how unsupervised pretraining with models like denoising autoencoders can be used to learn useful representations that can be transferred to supervised learning tasks.
- **Cross-Domain Transfer Learning:** This involves transferring knowledge between domains with different input distributions but the same task. 
- **[[Performance Drift]]:** This is a form of transfer learning where the data distribution changes gradually over time. The model needs to adapt to these changes to maintain good performance.

Benefits of Transfer Learning
- **Improved Generalisation:** By leveraging knowledge from a larger dataset, transfer learning can help models generalise better to new data, especially when the target dataset is small.
- **Reduced Data Requirements:** Transfer learning can significantly ==reduce the amount of labelled data needed to train a model in the target domain.== This is particularly beneficial for tasks where labelled data is expensive or time-consuming to obtain.
- **Faster Training:** Fine-tuning a pretrained model on a smaller dataset is typically faster than training a model from scratch.
### Follow up questions

- Why might fine-tuning a pre-trained model like GPT yield better results than training from scratch
### Practical Implementation

In [[ML_Tools]] see: [[transfer_learning.py]]

### Links
- [Video Overview](https://www.youtube.com/watch?v=yofjFQddwHE&list=PLkDaE6sCZn6E7jZ9sN_xHwSHOdjUxUW_b&index=19)
- [Deep Learning Video](https://www.youtube.com/watch?v=DyPW-994t7w&list=PLcWfeUsAys2nPgh-gYRlexc6xvscdvHqX&index=15)

