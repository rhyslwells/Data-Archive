---
tags:
  - software
  - infrastructure_as_code
---
A monolith, in the context of [[software architecture]], refers to a ==single, unified application where all components and functionalities are interconnected and interdependent==. In a monolithic architecture, the entire application is typically built as a ==single codebase==, and all functions and modules are tightly coupled.

While monolithic architectures can be simpler to develop and deploy initially, they can become cumbersome as the application grows in complexity. Many organizations eventually transition to [[microservices]] or other modular architectures to improve scalability, flexibility, and maintainability. However, monoliths can still be effective for smaller applications or teams with limited resources.

When we talk about a "function call-driven" monolith, we are referring to the way in which different parts of the application interact with each other. In such a system:

1. **Tightly Coupled Components**: All components of the application are part of a single codebase and often share the same resources, such as databases and libraries.

2. **Function Calls**: Communication between different parts of the application is primarily done through direct function or method calls. This means that one part of the application can directly invoke functions or methods in another part.

3. **Single Deployment Unit**: The entire application is deployed as a single unit. Any changes to one part of the application require redeploying the whole application.

4. **Shared Memory Space**: Since all components are part of the same application, they often share the same memory space, which can simplify data sharing but also lead to issues with scalability and fault isolation.

5. **Challenges with Scalability and Flexibility**: As the application grows, a monolithic architecture can become difficult to manage, scale, and update. Changes in one part of the system can have unintended consequences elsewhere, making it challenging to innovate quickly.

