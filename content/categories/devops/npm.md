---
aliases: []
category: DEVOPS
date modified: 11-02-2026
tags:
  - software
---
**npm** is the package manager for the [[JavaScript]] ecosystem, primarily used with **Node.js**.
### Core role

npm manages **dependencies** for JavaScript projects. It allows you to:

* Install third-party libraries
* Version and lock those libraries
* Publish and distribute your own packages
* Define and run project-specific commands

Conceptually, it plays the same role that `pip` plays in Python.

### Key components

#### 1. Package registry

A public registry containing millions of packages, each identified by a name and version. Packages typically expose reusable code, tooling, or frameworks.

#### 2. CLI tool

The `npm` command-line interface is installed automatically with Node.js.

Common commands:

* `npm init` — create a `package.json`
* `npm install <package>` — add a dependency
* `npm install` — install all declared dependencies
* `npm run <script>` — execute a project script

#### 3. `package.json`

A manifest file that defines:

* Project metadata
* Dependencies and version ranges
* Scripts (custom commands)
* Configuration hints for tools

Example:

```json
{
  "name": "example-project",
  "version": "1.0.0",
  "dependencies": {
    "lodash": "^4.17.21"
  },
  "scripts": {
    "build": "node build.js"
  }
}
```

#### 4. Lock file

`package-lock.json` records the **exact** dependency versions installed, ensuring reproducible builds across machines and environments.

### Dependency types

* **dependencies** — runtime requirements
* **devDependencies** — build, test, lint tooling
* **peerDependencies** — compatibility contracts (common in libraries)

Versioning follows **semantic versioning**: $MAJOR.MINOR.PATCH$.

### Typical use cases

* Frontend frameworks (React, Vue, Svelte)
* Backend services (Express, Fastify)
* Build tools (Vite, Webpack, ESLint, Prettier)
* Data tooling and CLIs

### Relation to alternatives

* **yarn** and **pnpm** are alternative package managers that use the same registry but differ in performance and dependency resolution strategy.
* npm remains the default and most widely supported.

### Mental model

Think of npm as:

> A reproducible dependency graph manager + task runner for JavaScript projects.

If useful, I can next:

* Contrast npm with `pip` in terms of dependency resolution
* Walk through a minimal Node.js project structure
* Explain lockfiles and semver edge cases in detail
