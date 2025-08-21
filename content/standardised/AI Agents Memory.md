---
aliases: 
category: LANG
date modified: 1-08-2025
tags:
  - evaluation
  - NLP
  - optimisation
  - language_models
---
How to give memory to long-running AI agents. That is how do we enable agents to **maintain**, **retrieve**, and **update** salient conversation memories over extended conversations.

Context:
* LLMs tend to forget information within and across sessions due to fixed context windows.
* Forgetting over sessions can cause user frustration.
* Large contexts increase both **cost** and **latency**.
* Memory systems should not depend solely on the size of the input prompt.

### Challenges

* **Context overflow**: exceeding the token window.
* **Irrelevant history**: retaining unused or low-value information.
* **Memory management**: removing stale or outdated memories without losing critical data.

### Use Cases

* Personalised learning assistants.
* Customer support bots.
* Financial advisory agents.
### Architecture Overview

1. **Store** memories in a database.
2. **Retrieve** relevant memories via semantic \[\[similarity search]].
3. **Update** process: add, update, delete, or NOOP (no operation).
4. Optional **graph memory** layer

Metrics to evaluate:
  * Memory quality.
  * F1 score.
  * BLEU-1 score.
  * Token consumption analysis.

Key Takeaways
* Persistent long-term memory improves **performance**, reduces **cost**, and increases **speed**.
* Reasoning is essential during the memory update phase to maintain accuracy and coherence.

### Example Engineering Questions

#### Architecture & Scale

* What are the biggest engineering challenges in maintaining long-term memory at scale, especially with respect to latency, consistency, and cost?
* How should **mem0** be integrated into production with a self-hosted setup (e.g., Docker with MCP)?
* Which API calls are required for summarisation and retrieval, and at which stages?

#### Cost & Retrieval

* How can cost be controlled while maintaining contextual memory?
* What trade-offs exist between retrieval speed and memory depth?
* Does marking graph relationships as invalid (instead of deleting them) cause memory bloat and higher cost?

#### Memory Quality & Versioning

* How is memory versioned as the agent or model changes?
* Are there mechanisms for detecting **memory drift** or **bias accumulation**?

#### API Behaviour & Retrieval Logic

* How many API calls are required for create/update and retrieval?
* Does retrieval fetch top-N similar memories (e.g., top 10 via \[\[cosine similarity]])?
* Can the number of historical messages retrieved for fact generation be configured?
* Differences between open-source and enterprise versions of mem0, especially in fact generation.

#### Candidate Facts & Domain Adaptation

* Difference between *candidate facts* and *summary*.
* Must developers define candidate facts per domain?
* How are nodes selected?
* Should mem0 or mem0g be chosen per domain, or can mem0g be applied universally?

#### Evaluation

* Evaluation metrics considered: F1 score, BLEU-1, memory quality.
* How does Mem0 quantitatively evaluate long-term memory effectiveness in retrieval accuracy, relevance, and downstream task performance over time?
* For fine-tuning memory quality for specific applications, what parameters can be adjusted?

### Resources
Paper: Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory
Related: [[LLM Memory]]