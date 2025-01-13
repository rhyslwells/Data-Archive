---
title: 
tags:
  - model_algorithm
aliases: 
category:
---
## Links
- [Video Overview](https://www.youtube.com/watch?v=yofjFQddwHE&list=PLkDaE6sCZn6E7jZ9sN_xHwSHOdjUxUW_b&index=19)
- [Deep Learning Video](https://www.youtube.com/watch?v=DyPW-994t7w&list=PLcWfeUsAys2nPgh-gYRlexc6xvscdvHqX&index=15)

## Overview 

Transfer learning is a  technique in machine learning that ==leverages knowledge gained from one setting (source domain) to improve performance on a different but related setting (target domain).== 

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

## Practical Implementation

For deep learning, to do we take out and replace a few end layers of the network. We can then train just the last layer of weights of a neural network. 

The number of layers to remove and then added from pretrained depends on the similarity between tasks. Higher layers in networks are able to recognise higher detail components. More specific. 


```python
import tensorflow_datasets as tfds
import tensorflow as tf
dataset, info = tfds.load("tf_flowers",
                          as_supervised=True,
                          with_info=True)
dataset_size = info.splits["train"].num_examples
class_names = info.features["label"].names
n_classes = info. features["label"].num_classes
test_set_raw, valid_set_raw, train_set_raw
            = tfds.load("tf_flowers",
                        split=["train[:10%]",
                               "train[10%:25%]",
                               "train[25%:]"],
                        as_supervised=True)
                        
def preprocess(image,label):
    resized_image = tf.image.resize(image, [224,224])
    final_image = tf.keras.applications.xception.preprocess_input(resized_image)
    return final_image, label


batch_size = 32
train_set = train_set_raw.shuffle(1000)
train_set = train_set.map(preprocess).batch(batch_size).prefetch(1)
valid_set = valid_set_raw.map(preprocess).batch(batch_size).prefetch(1)
test_set = test_set_raw.map(preprocess).batch(batch_size).prefetch(1)

base_model = tf.keras.applications.xception.Xception(weights="imagenet",
                                            include_top=False)

avg = tf.keras.layers.GlobalAveragePooling2D()(base_model.output)
output = tf.keras.layers.Dense(n_classes, activation="softmax")(avg)
model = tf.keras.Model(inputs=base_model.input, outputs=output)

  
#freezing previous layers
for layer in base_model.layers:
  layer.trainable = False

optimizer = tf.keras.optimizers.SGD(lr=0.2,
                                    momentum=0.9,
                                    decay=0.01)

model.compile(loss="sparse_categorical_crossentropy",
              optimizer=optimizer,
              metrics=["accuracy"])


history = model.fit(train_set,
                    epochs=5,
                    validation_data=valid_set)

 
for layer in base_model.layers:
  layer.trainable = True


# change runtime to gpu here.
optimizer = tf.keras.optimizers.SGD(lr=0.01,
                                    momentum=0.9,
                                    decay=0.001)

model.compile(loss="sparse_categorical_crossentropy",
              optimizer=optimizer,
              metrics=["accuracy"])

  
history = model.fit(train_set,
                    epochs=10,
                    validation_data=valid_set)

```
