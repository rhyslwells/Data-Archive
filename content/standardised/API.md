---
title: 
tags:
  - data_integration
aliases: 
category:
---

Resources:
[Link](https://www.youtube.com/watch?v=yBZO5Rb4ibo)
# Summary

APIs, or Application Programming Interfaces, are integral to the seamless operation of software systems. They enable different software components to ==communicate== and interact, thereby enhancing functionality and user experience. For instance, using your Facebook or Google account to sign up for a new app simplifies the process by allowing these platforms to share necessary information. Used to communicate with a server.

 Key Takeaways
- APIs are essential for enabling communication between different software systems.
- They simplify tasks by providing structured requests and responses.
- Understanding and using APIs does not require in-depth knowledge of the underlying systems.
- Good API design and documentation are critical for effective implementation and code reuse.
#### What is an API?

An API  allows one system (client) to ==request specific actions from another system== (server). This interaction is made possible through a predefined set of rules and ==protocols==. For instance, a weather app querying a weather API to fetch the current weather conditions involves sending a structured request and receiving a response.
#### Types of API Connections

1. **Web APIs**: These facilitate communication between web clients (browsers or apps) and servers. For example, online shopping apps use APIs to process transactions on remote servers.
2. **Database APIs**: These allow applications to interact with databases, ensuring data is accessed and manipulated efficiently.
3. **Device APIs**: When apps like Instagram or WhatsApp request access to your phone's camera or microphone, they use device APIs.
#### API Principles

1. **Controlled Access**: APIs provide access to certain parts of a system while keeping the core functionalities secure.
2. **System Independence**: APIs function independently of changes in the underlying system.
3. **Simplicity**: APIs are designed to be ==user-friendly== and come with comprehensive documentation to guide developers.
#### Importance of API Documentation

Good API documentation is crucial. It provides instructions on how to structure requests and handle responses, making it easier for developers to integrate and use APIs effectively. As highlighted by David Parnas, effective reuse of code and APIs depends on both good design and thorough documentation.

#### REST API
- REST stands for Representational State Transfer.
- It is a ==standardized== software architecture style used for API communication between a client and a server.

**Benefits of REST APIs:**
1. **Simplicity and Standardization:**
   - Data formatting and request structuring are standardized and widely adopted.
2. **Scalability and Statelessness:**
   - Easily modifiable as service complexity grows without tracking data states across client and server.
3. **High Performance:**
   - Supports ==caching==, maintaining high performance even as complexity increases.

**Main Building Blocks:**
1. **==Request==:**
   - Actions (==[[CRUD]]==): Create (POST), Read (GET), Update (PUT), Delete (DELETE).
   - Components: Operation (==HTTP method==), Endpoint, Parameters/Body, Headers.
2. **Response:**
   - Typically in [[JSON]] format.

**REST API Example:**
ice cream shop inteacting with cloud database.
- Endpoint example: "icecream.com/api/flavors"
  - "api" indicates the API portion.
  - "flavors" refers to the ==resource== being accessed or modified.

**Real-world Examples:**
1. **Get Flavors:**
   - Operation: ==GET==
   - Endpoint: "/api/flavors"
   - Response: Array of flavor resources.
2. **Update Flavor:**
   - Operation: ==PUT==
   - Endpoint: "/api/flavors/1"
   - Body: New flavor data.
   - Response: Confirmation of update.
3. **Create New Flavor:**
   - Operation: ==POST==
   - Endpoint: "/api/flavors"
   - Body: New flavor data.
   - Response: Confirmation of creation.