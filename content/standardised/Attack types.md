---
tags: 
category: 
---
Related notes:
- [[Attack mitigation]]
### Cache Poisoning and Denial of Service

| Attack | Idea | Example |
|:------|:-----|:--------|
| Cache Poisoning | Attacker manipulates cache content to serve malicious responses. | Poisoning a CDN cache to distribute bad scripts. |
| Denial of Service (DoS) | Overwhelm servers so they can't respond to legitimate requests. | Botnet floods a login page until it crashes. |

### Credential Stuffing and Password Risks

Credential Stuffing:  
  Attackers use previously leaked usernames/passwords from breaches to try logging into other sites.

Why it works:  
  People reuse the same passwords across multiple accounts.

Mitigation/Defenses:
- Enforce strong password policies.
- Deploy bot detection (e.g., CAPTCHA, behavior analysis).
- Use MFA (Multi-Factor Authentication) to require an extra step beyond password.