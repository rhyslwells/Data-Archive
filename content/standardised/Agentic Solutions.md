---
tags:
  - drafting
aliases: 
category:
---
Agentic solutions leverage multiple autonomous agents (usually [[Small Language Models|SLM]]) to achieve goals collaboratively. These systems distribute tasks across agents that operate individually or collectively to solve complex problems.
## **Agent Interactions**

### How do Agents Interact?

- **Horizontal Collaboration:** Agents with local goals coordinate to achieve a shared objective.
- **Hierarchical Collaboration:** Primary agents oversee specialized agents to manage complex tasks effectively.

## **Types of Agentic Solutions**

### Chat Experiences:

**Reactive Solutions (Ask Approach):**  
    Systems like chatbots and retrieval-augmented generation (RAG) tools respond to user queries.
    
**Autonomous Solutions (Do Approach):**  
    Agents perform tasks proactively, e.g., drafting documents or scheduling meetings.
## **Understanding Agents**

### Core Components:

1. **Tools:** Resources such as APIs, databases, or GitHub.
2. **Strategy:** Techniques like self-criticism, chain of thought (CoT), and planning to improve reasoning.
3. **States:** Memory, context tracking, and microservices for modularity.
4. **Goals:** Specific objectives defined for each agent.

## **Agent Planning and Interaction**

1. **Planning:** Agents plan operations, such as managing workflows in a support center.
2. **Agent Collaboration:** Agents align their individual goals with shared objectives to enhance system performance.

## **Compounding Systems**

### Multi-Agent Systems:

These systems reduce reliance on extensive prompt engineering by compartmentalizing tasks across specialized agents.  
**Example:** A writer agent drafts content, while a reviewer agent ensures quality, both operating within defined scopes.

## **Business Process Integration**

### Workflow:

1. Identify a business problem.
2. Define personas (agents) required.
3. Develop an agentic workflow.

### Agentic Architectures:

1. **Vertical:** Hierarchical structures for task delegation.
2. **Horizontal:** Collaborative structures with high feedback loops.
3. **Mixed:** Combines vertical delegation with horizontal collaboration.

**Vertical Example:** A primary agent delegates tasks to lower-level agents for execution.

## **The Orleans Framework**

A framework for building distributed applications in .NET.

- **Grains:** Individual agents performing specific tasks.
- **Silos:** Distributed nodes managing grains.
- **Clusters:** Collections of silos for scalability.

## **Problem Solving with Agents**

### Defining Roles:

Agents can model specific business functions. Role clarity enhances the effectiveness of these systems.

## **Benefits of Using Agents**

1. **Performance Gains:** Task parallelization enhances throughput.
2. **Developer Abstraction:** Modular design simplifies system understanding and debugging.
3. **Workflow Integration:** Aligns AI agents with organizational processes.

## **Example Use Cases**

1. **IT Helpdesk Agent:** Automates troubleshooting and network access requests.
2. **Device Refresh Agent:** Manages hardware upgrades and approvals.
3. **Lead Generation Agent:** Identifies and researches potential leads.
4. **Budget Management Agent:** Reviews financial data and aids in planning.
5. **Customer Support Agent:** Triage support issues for faster resolution.
6. **Project Tracker Agent:** Tracks project milestones and budget compliance.



