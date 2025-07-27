---
aliases: []
category:
date modified: 27-07-2025
tags: [GenAI, ml_process]
---
LangChain is a [[Python]] framework designed to facilitate the development of applications powered by [[LLM]]s (Large [[Language Models]]). It enables developers to build end-to-end, composable workflows that involve LLM interaction, integration with data sources, memory, tools, and agentic decision-making.

Purpose: LangChain abstracts and orchestrates the logic needed to:
* Prompt LLMs effectively
* ==Chain together multiple LLM calls== or components
* Maintain [[LLM Memory]] of interactions
* Interact with external tools and APIs
* Build autonomous or semi-autonomous [[Agentic Solutions]]
* Enable retrieval and indexing over documents

Core Modules:

* [[Models]]: Interface layer to various LLM providers (e.g., OpenAI, Cohere).
* [[Prompts]]: Templates and logic for prompt creation and formatting.
* [[Chains]]: Composable sequences of LLM calls, enabling structured workflows.
* [[LLM Memory]]: Mechanisms to persist context across interactions.
* Indexes: Tools for embedding and retrieving documents using vector stores.
* [[Agents and Tools]]: Constructs for dynamic decision-making, allowing the LLM to choose tools (e.g., calculator, web search) at runtime.

Example Application:

* [[Pandas DataFrame Agent]]: An agent that enables natural language interaction with tabular data using [[pandas]] and LLM reasoning.

Use Cases:

* Chatbot that remembers prior inputs within a session
* [[Querying]] a CSV file with natural language
* Summarizing notes or documents interactively
* A lightweight research assistant that chooses between tools to answer a question