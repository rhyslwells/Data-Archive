---
aliases: 
category: 
date modified: 27-07-2025
tags:
  - security
---
### Secrets Management: Why Scan for Keys?

Purpose of Secret Keys:
  - Authenticate to APIs, databases, services (like AWS, GitHub, etc.).
- Risks:
  - Accidentally pushing keys into public repositories (e.g., GitHub) exposes you to massive risk.

Why scan?
  - Tools like `truffleHog`, `git-secrets`, or GitHub's own secret scanning detect leaked keys early.

### Bug Bounty Programs
  - Some companies reward researchers who find exposed bugs and report them responsibly.