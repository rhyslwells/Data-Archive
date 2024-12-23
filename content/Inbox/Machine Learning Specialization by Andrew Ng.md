

## [[Vectorisation]]

[[Numpy]]

[[gpu]]

numpy dot is better than for loop and summing.

![[Pasted image 20241217204829.png]]

Why does it run faster?

Sequentially versus simultaneously in parallel.. 

https://www.youtube.com/watch?v=uvTL1N02f04&list=PLkDaE6sCZn6FNC6YRfRQc_FbeQrF8BwGI&index=24

## [[Vector Database]]

most data is unstructured.

Need to assign tags or 

A vector database indexes
and stores vector embeddings
forfast cetrieval
and Similarity search.

[[Vector Embedding]]

similar items are nearby.

How to query these vectors?

Have index for vectors. There are different indexing methods.

[[semantic search]]

use cases

1. long-term memory for LLMs
2. semantic search: search based on
the meaning or context
3. similarity search for text, images,
audio, or video data

Options:
pincone,weaviate,chroma, redis,qdrant,milvus,vespa.



## Gradio (Hugging face?)

https://www.youtube.com/watch?v=eE7CamOE-PA&list=PLcWfeUsAys2my8yUlOa6jEWB1-QbkNSUl&index=2

To publicly show ml projects.

https://www.gradio.app/

an option to show online what iv been working on.

Share and hosting.

Hugging face spaces to host it for free.

# [[Recurrent Neural Networks|RNN]]

[Video link](https://www.youtube.com/watch?v=TLLqsEyt8NI&list=PLcWfeUsAys2nPgh-gYRlexc6xvscdvHqX&index=9)

Resources: https://stanford.edu/~shervine/teaching/cs-230/cheatsheet-recurrent-neural-networks

Used in [[NLP]]

RNNS operate on sequence data 

"RNNs are a special class of neural networks that operate on
sequence data and allow previous outputs to be used as inputs
while having hidden states."

Example: "The color of the sky is ___"

We remember the previous context.

This cannot be done with [[Neural network]]

Input =x
hidden layer
step =v
![[Pasted image 20241219073017.png]]

RNNS are flexible: 
- one to many : one input : usic gen
- many to one - sentiment 

RNNS learn through [[Backpropagation]] through time. 

can lead to [[vanishing and exploding gradients problem]]

more time steps the less data we keep from the past.

![[Pasted image 20241219073440.png]]

Solutions: [[LSTM]] and [[GRU]]: use gates: but are costly in comp.

use [[PyTorch]] or [[Tensorflow]]



# [[Metrics]] [[evaluation metrics]]

[[Precision or Recall]] used for [[binary classifications]]


![[Pasted image 20241222091831.png]]

What if there is more than one class?

PR Curve - [[Precision]] and [[Recall]] curve.

[[Cross Entropy]] - binary, categorical, sparse. In keras. It calculates the distance,or difference between distrubtuinosn.

Regression evalsuation metrics:

Mean absolute error.
Mean square error - greater error values are exagerated.
Root mean square error - easier to interpreate, back to the same scale.
[[R squared]] - how well the model fits, how much the real value vary from the predicted values.

[[cosine simialrity]]  - similar to [[Cross Entropy]] -, it calcs diff  be

