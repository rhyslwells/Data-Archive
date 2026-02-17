---
aliases: [null]
category: CS
date modified: 11-02-2026
tags: [javascript, programming, runtime, web]
---
JavaScript is a high-level, interpreted programming language primarily used to implement dynamic behaviour in software systems, most notably in web applications. It enables executable logic to run within a host environment, such as a web browser or a server runtime like Node.js.

At its core, JavaScript provides:

* A dynamic type system
* First-class functions
* Prototype-based object orientation
* An event-driven execution model
* Asynchronous programming via [[callbacks]], promises, and $async/await$

## Execution Environment

JavaScript does not run independently. It executes inside a host environment that provides APIs:

* **Browser runtime** → Access to the DOM, events, networking, storage.
* **Node.js runtime** → Access to the file system, OS interfaces, networking stack.

The JavaScript engine (e.g., V8, SpiderMonkey) parses and executes the language. The host environment supplies additional capabilities.

## Core Characteristics

### 1. Interpreted / JIT-compiled

Modern engines use Just-In-Time (JIT) compilation to convert JavaScript into optimized machine code at runtime.

### 2. Single-threaded with Event Loop

JavaScript typically runs on a single thread using an event loop model. Long-running operations are handled asynchronously to avoid blocking execution.

### 3. Prototype-Based Object Model

Objects inherit directly from other objects rather than from classical class hierarchies (although $class$ syntax exists as syntactic abstraction).

### 4. Dynamic Typing

Types are resolved at runtime. Variables can change type during execution.

## Minimal Example

```javascript
function greet(name) {
  return `Hello, ${name}`;
}

console.log(greet("Rhys"));
```

This illustrates:

* Function declaration
* String interpolation
* Runtime execution in a host environment

## Where It Fits in the Stack

In [[web architecture]]:

* **HTML** → Structure
* **CSS** → Presentation
* **JavaScript** → Behaviour and logic

In backend systems:

* JavaScript (via Node.js) handles APIs, services, data processing, and real-time systems.

## Conceptual Summary

JavaScript is a general-purpose scripting language designed to execute within a runtime environment to control behaviour, respond to events, manipulate state, and coordinate asynchronous operations. It is foundational to modern web development and increasingly common in full-stack and server-side systems.

## Related

[[React]]