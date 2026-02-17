---
aliases:
  - 
category: DEVOPS
date modified: 27-09-2025
tags:
  - javascript
  - runtime
  - programming
---
**Node.js** is a **[[JavaScript]] runtime environment** that executes JavaScript **outside the browser**. It allows JavaScript to be used for server-side and general-purpose programming.
### Core idea

Node.js embeds the **V8 JavaScript engine** (the same engine used by Chrome) and combines it with a set of system-level APIs. This makes it possible to run JavaScript files directly on an operating system:

```bash
node app.js
```

### Key architectural characteristics

1. **Event-driven, non-blocking I/O**
   Node.js uses an asynchronous execution model built around an event loop. I/O operations (network, filesystem) are handled without blocking the main thread, which is well-suited to high-[[concurrency]] workloads.

2. **Single-threaded execution model**
   JavaScript code runs on a single main thread. Concurrency is achieved through asynchronous callbacks, promises, and an internal thread pool for certain operations.

3. **Standard library for system access**
   Node.js exposes APIs for:

   * HTTP servers
   * File system access
   * Process and environment management
   * Networking

### Practical use cases

* Web APIs and backend services
* Data pipelines and automation scripts
* CLI tools and build systems
* Real-time systems (e.g. WebSockets)

### Relationship to [[npm]]

* Node.js is the runtime that executes JavaScript.
* **[[npm]]** is the package manager that installs libraries used by Node.js programs.
* Together, they form the core tooling for server-side JavaScript.

### Conceptual comparison

* Browser JavaScript: sandboxed, DOM-focused, no direct file or network socket access.
* Node.js JavaScript: system-level access, long-running processes, server execution.

If useful, I can map Node.js concepts to [[Python]] equivalents (e.g. Node.js vs CPython + `asyncio`) or explain the event loop in terms of task queues and microtasks.
