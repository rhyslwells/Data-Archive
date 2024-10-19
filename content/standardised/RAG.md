---
title: 
tags: 
resources: https://www.youtube.com/watch?v=T-D1OfcDW1M
---
Rag is a framework the help [[LLM]] be more up to date.

RAG grounds the Gen AI in external data.

>[!Summary]
> Given a question sometimes the answer given is wrong, issue with [[LLM]] is no source of data and is out of date.  **RAG** is a specific architecture used in natural language processing ([[NLP]]), where a **retrieval mechanism** is combined with a **generative model** ([[Generative]]) (often a [[Transformer]] like GPT). RAG systems are designed to ==enhance the ability of a generative model to answer questions or generate content by incorporating factual knowledge retrieved from external data sources== (such as documents, databases, or knowledge repositories). RAG is the connection of [[LLM]]'s with external databases. 

>[!Example]
> **Example of a RAG System**:
> - A user asks: *"What is the capital of France?"*
> - The **retrieval module** fetches a relevant document (e.g., from Wikipedia) that contains the information about France’s capital.
> - The **generation module** synthesizes the response: "The capital of France is Paris."

### [[LLM]] Challenges
- Responses are sometimes no sources and out of date.
- LLM's are trained on some store of data (static).  We want this store to be updated.
### Key characteristics of RAG:

![[Pasted image 20240928194559.png|500]]

Based on a [[prompting]].

1. **Retrieval Component**:
   - This module fetches relevant documents (and up to date) or information from an external corpus based on the query or input. It may use traditional search methods like dense vector retrieval (e.g., using embeddings) or keyword-based retrieval.
   - Retriever should be good enough to give the most truthful information based on the store
   
2. **Generative Component**:
   - After retrieving relevant documents, the [[Generative]] model (such as GPT or [[BERT]]-based models) synthesizes the final response, integrating both the input query and the retrieved information to generate more accurate and contextually informed outputs.
   
3. **Augmentation with External Knowledge**:
   - Instead of solely relying on pre-trained internal knowledge (as in traditional language models), RAG setups use the external knowledge source for augmenting generation, thus improving factual accuracy and reducing the risk of hallucinations (incorrect or fabricated responses).

Model should be able to saay "I dont know" instead of [[hallucinating]]

### Resources



[[RAG]]
Problems
1. LLMs struggle with memorization > "LLMs may struggle with
tasks that require domain-specific expertise or up-to-date
information.
2. LLMs struggle with generating factually inaccurate content
(hallucinations)
Solution
· A lightweight retriever (SM) to extract relevant document
fragments from external knowledge bases, document collections,
or other tools

 Differnet RaG techinwuqs:
 Spare retrievers, BM25, dense retrtivers. Use Bert for similarity matching:

![[Pasted image 20241017165540.png]]