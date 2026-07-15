---
name: waf
description: "Configures Web Application Firewall protection with ModSecurity, CRS rules, and blocking policies."
category: security
tags: [waf, modsecurity, firewall, rules, protection]
models: [sonnet, opus]
version: 1.0.0
created: 2026-05-14
---
# WAF (Web Application Firewall)
> Protect web applications from common attacks.
## Quick Start
```bash
sudo apt-get install libnginx-mod-modsecurity
sudo cp /etc/modsecurity/modsecurity.conf-recommended /etc/modsecurity/modsecurity.conf
```
## OWASP CRS & Custom Rules
```conf
Include /etc/modsecurity/crs/crs-setup.conf.example
Include /etc/modsecurity/crs/rules/*.conf
SecRule ARGS "@detectSQLi" "id:1000,phase:2,deny,status:403,msg:'SQL Injection blocked'"
SecRule ARGS "@detectXSS" "id:1001,phase:2,deny,status:403,msg:'XSS blocked'"
SecRule IP:REQUEST_RATE "@gt 100" "id:2000,phase:2,deny,status:429,msg:'Rate limit exceeded'"
```
## When to Use
- Production web app protection; PCI DSS; OWASP Top 10; DDoS mitigation
## Validation
1. ModSecurity loads; 2. Attack payloads blocked (403); 3. Legitimate traffic passes
