---
aliases:
- null
category: LANG
date modified: 27-09-2025
tags:
- GenAI
---
### Objective:

 How do LLMs work and operate.  
 Enabling [[LLM]]'s at scale:
 Explore recent AI and [[Generative AI]] language models 


### Steps

Math on words: Turn words into coordinates.
Statistics on words: Given context what is the probability of whats next.
Vectors on words. [[Cosine Similarity]]
How train: Use [[Markov chain]] for prediction of the next [[Tokenisation]]


Tokeniser: map from token to number

1. Pre-training: tokenise input using [[NLP]] techqinues
2. [[LLM]] looks at context: nearby tokens, in order to predict

different implmentationg for differnet languages. Differnet tokenisers or translating after.

Journey to scale:

1. Demos, POC (plan to scale): understand limitations
2. Beyond experiments and before production: 
3. Enterprise level: translate terms so they can use governess techniques.

Building:

![[Pasted image 20240524130607.png]]

### [[Software Development Life Cycle]]

For GenAI: Building an applicaiton with GenAi features

1. Plan: use case: prompts : archtecture: cloud or on site
2. Build: vector database
3. Test: Quality and responsible ai. 

### [[call summarisation]]

take transcript - > summariser -> summarise

Source: human labeled transcripts to check summariser. 

![[Pasted image 20240524131311.png|500]]

[[Ngrams]] analysis - when specific words realy matter


### [[RAG]]

Use relvant data to make response better:

![[Pasted image 20240524131603.png]]

## [[GAN]]

For image models.

Examples: midjourney,stable diffusion,dall-e 3

image model techniques:
- text to image
- image to image
## Notes: 

Use [[LLM]]'s to get short info, then cluster.
Going round training data : called a Epochs










