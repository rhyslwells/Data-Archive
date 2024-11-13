---
title: 
tags:
  - evaluation
  - language_models
importance: 7
engagement: 5
recency_of_interest: 2024-09-26
---
The [[LMSYS]] Chatbot Arena is a platform where various large language models ([[LLM]]s), including versions of GPT and other prominent models like LLaMA or Claude, are compared through side-by-side interactions. The performance of these models is evaluated using human feedback based on the quality of their generated responses.

The arena employs several techniques to rank and compare models:

1. **[[Elo Rating System]]**: Adapted from chess, this system rates models based on their relative performance in head-to-head competitions. When one model's response is preferred over another's, the winning model gains points while the losing model loses points. The rating difference helps determine the strength of models in future predictions. The system adjusts ratings gradually to avoid bias towards more recent results, ensuring stability over time.

2. [[Bradley-Terry Model]]: This model goes beyond simple win-loss records by taking into account the ==difficulty of the task== and the models' relative strengths. It helps fine-tune the ranking, especially when one model consistently performs better against tougher tasks.

In addition to these ranking systems, users can directly compare LLMs by giving them [[prompting]] to handle, such as writing articles, answering questions, or performing translations. Human voters then decide which model's output is better, or they can declare a tie if neither response is satisfactory.

These methods ensure continuous improvement of the rankings, providing a transparent and evolving leaderboard of the best generative models, including GPT versions

https://openlm.ai/chatbot-arena/

https://www.analyticsvidhya.com/blog/2024/05/from-gpt-4-to-llama-3-lmsys-chatbot-arena-ranks-top-llms/



