---
aliases: []
category:
date modified: 27-07-2025
tags: [data_governance, data_security]
---

Related notes:
- [[Security Vulnerabilities]]
- [[SQL Injection]]
- [[Security Researcher]]
- [[Security mitigation]]
- [[Attack types]]
- [[Attack mitigation]]

Summary
```plaintext
- Attackers constantly evolve; defenses must be layered.
- Critical risks: passwords, injection attacks, secret leaks.
- Secure-by-default coding (e.g., React) is a good first step.
- Security is not one-time: continuous monitoring and response is essential.
```

Flow
1) Assume You Are Under Attack
2) Design Multiple Defense Layers (Defense in Depth)
3) Secure Inputs (Escape, Sanitize, Validate)
4) Restrict Privileges (Least Privilege Principle)
5) Monitor for Compromise (IoCs)
6) Respond and Recover Quickly

### Mindset: Always Assume You Are Under Attack

The "always under attack" mindset means:
  - Assume systems are *already* being probed.
  - Assume credentials, APIs, services can be targeted *at any moment*.
  - Focus on reducing risk and early detection, not just reacting after breaches.

### Defense in Depth: Swiss Cheese Model

Defense in Depth:  
  Multiple independent layers of security, so even if one fails, others still protect.

Swiss Cheese Model:  
  Every defense layer has holes (weaknesses), but when layered, holes are less likely to align and create a clear path for attackers.

Layers might include:
- Firewall
- Application security
- Authentication policies
- Monitoring and alerting
- Encryption

### Indicators of Compromise (IoCs)

IoCs are signs that a system may have been breached. Used for incident detection and threat hunting.

Examples:
- Unexpected outgoing traffic
- Unusual user behavior
- Presence of known malware files
- Unauthorized configuration changes










