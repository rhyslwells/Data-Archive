---
title: 
tags:
  - NLP
  - language_models
aliases:
  - SLM
category: paper
resources: https://arxiv.org/pdf/2409.06857
---
[[LLM|LLMs]] dominate many general-purpose NLP tasks, small [[Language Models]] have their own place in specialized tasks, where they excel due to computational efficiency, [[interpretability]], and task-specific fine-tuning. 

SLMs remain highly relevant for [[Edge Machine Learning Models]] and edge computing, ==domain-specific tasks==, and applications requiring [[interpretability]], making them a crucial tool in the NLP landscape.

### Use Cases for Small Language Models (SLMs)

- [[Contrastive Decoding]]: Improve the quality of generated content by filtering out low-quality outputs, by having a SLM guide and critique a LLM or other way ([[inference]])
	- Mitigate hallucinations
	- Augmented Reasoning
- [[Knowledge Distillation]]: Transfer the knowledge from a larger model to a smaller one, retaining performance but reducing computational requirements (see [[BERT]] Teacher model).
- [[Data Synthesis:]] Generate or augment datasets in scenarios with limited data.
- [[Model Cascading]]: Use a combination of smaller models and larger models in a cascading architecture, where simpler tasks are handled by SLMs and more complex ones by LLMs. Model cascading and routing allow SMs to handle simpler tasks, reducing computational overhead. Or the other way first do a general search with a LLM then refine to domain specific small model which is more [[interpretability|interpretable]] and specific.
- Domain specific & Limited Data Availability: SMs, however, can be ==effectively fine-tuned== on smaller, ==domain-specific datasets== and outperform general LLMs in tasks with limited data availability.
- [[RAG]] (Retrieval Augmented Generation): Lightweight ==retrievers== (SMs) can support LLMs in finding relevant external information.

### Advantages of SLMs

- Require less computational power and are faster in [[inference]] compared to LLMs.
- [[Interpretability]]
- Accessible for those without resources in power and data



